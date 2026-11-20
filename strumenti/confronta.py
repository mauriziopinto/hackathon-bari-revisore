"""Confronta i report del gruppo con i risultati attesi e calcola i numeri della giornata.

Uso, dalla cartella del repository:
    python3 strumenti/confronta.py giornata     dopo le 14:00, quando è aperta la busta 1
    python3 strumenti/confronta.py nuovi        dopo le 16:00, quando è aperta la busta 3

Legge i report del gruppo nel formato comune (un file .json per documento, nella cartella report/,
descritto nel README) e i risultati attesi della busta. Stampa i numeri e li salva anche in
risultati/confronto-<insieme>-<ora>.md. Usa solo la libreria standard di Python.

Tre viste, nello stesso ordine della giornata:
    1. il programma: le quattro regole di forma, controllate dal programma della mattina;
    2. criteri misurabili: la regola che applica la skill del pomeriggio;
    3. il revisore completo: tutte le regole insieme, con il semaforo finale.
"""
import argparse
import json
import math
import re
import sys
from datetime import datetime
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
INSIEMI = {
    "giornata": ("buste/busta_1/riferimento_giornata.json", "documenti della giornata", 1),
    "nuovi": ("buste/busta_3/riferimento_nuovi.json", "documenti nuovi delle 15:30", 3),
}
MECCANICHE = {"sezioni_obbligatorie_sd", "formato_come_voglio_affinche",
              "criteri_accettazione_presenti", "criteri_formato_dato_quando_allora"}
GIUDIZIO = {"criteri_misurabili"}
SEMAFORI = {"verde": "Verde", "giallo": "Giallo", "rosso": "Rosso"}
GRAVITA = {"bloccante": "Bloccante", "non bloccante": "Non bloccante"}
FORMA_POSIZIONE = re.compile(r"^(sd/.+|us-\d+(/ca-\d+\.\d+)?)$")
C4_QUOTA = 0.75  # 3 documenti su 4 nella prima versione: 6 su 8 con SD e User Story separate


def norm_posizione(p):
    """'US-05, CA-05.2', 'us-05 / ca-05.2' e 'US-05/CA-05.2' diventano la stessa chiave."""
    p = str(p).strip().lower()
    p = re.sub(r"\s*[,/]\s*", "/", p)
    p = re.sub(r"(us-\d+)\s+(ca-)", r"\1/\2", p)
    p = re.sub(r"\s+", " ", p)
    if p.startswith("sd/"):
        return "sd/" + p[3:].replace("sezione ", "").strip()
    return p.replace(" ", "")


def semaforo(non_conformita):
    gravita = {n["gravita"] for n in non_conformita}
    if "Bloccante" in gravita:
        return "Rosso"
    return "Giallo" if gravita else "Verde"


def leggi_riferimento(percorso):
    if not percorso.exists():
        sys.exit(f"Non trovo {percorso.relative_to(RADICE)}.\n"
                 f"La busta si apre all'ora stabilita con: python3 strumenti/apri_busta.py <numero>")
    dati = json.loads(percorso.read_text(encoding="utf-8"))
    rif = {}
    for d in dati:
        nc = [{"regola": n["regola"], "gravita": n["gravita"], "posizione": norm_posizione(n["posizione"]),
               "descrizione": n.get("descrizione", "")} for n in d["non_conformita"]]
        rif[d["documento"]] = {"tipo": d["tipo"], "semaforo_meccanico": d["semaforo_meccanico"],
                               "semaforo_finale": d["semaforo_finale"], "non_conformita": nc}
    return rif


def leggi_report(cartella, documenti, avvisi):
    """I report del gruppo per i documenti del riferimento. Se un documento ha più file, vale il più recente."""
    trovati = {}
    for f in sorted(cartella.rglob("*.json"), key=lambda x: x.stat().st_mtime):
        if f.name.startswith("modello_report"):
            continue
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            avvisi.append(f"{f.relative_to(RADICE)}: non è un JSON valido ({e}).")
            continue
        voci = d if isinstance(d, list) else [d]
        for v in voci:
            if not isinstance(v, dict) or "documento" not in v:
                avvisi.append(f"{f.relative_to(RADICE)}: manca il campo 'documento'.")
                continue
            nome = Path(str(v["documento"])).stem
            if nome not in documenti:
                continue
            if nome in trovati:
                avvisi.append(f"{nome}: più di un report, uso il più recente ({f.relative_to(RADICE)}).")
            trovati[nome] = (f, v)
    report = {}
    for nome, (f, v) in trovati.items():
        nc = []
        for i, n in enumerate(v.get("non_conformita", []), start=1):
            dove = f"{nome}, non conformità {i}"
            regola = str(n.get("regola", "")).strip()
            gravita = GRAVITA.get(str(n.get("gravita", "")).strip().lower())
            posizione = norm_posizione(n.get("posizione", ""))
            if regola not in MECCANICHE | GIUDIZIO:
                avvisi.append(f"{dove}: regola '{regola}' sconosciuta. Usate i nomi del file config/qualita_doc.yaml.")
            if gravita is None:
                avvisi.append(f"{dove}: gravità '{n.get('gravita')}' non valida. Valori: Bloccante, Non bloccante.")
                gravita = "Non bloccante"
            if not FORMA_POSIZIONE.match(posizione):
                avvisi.append(f"{dove}: posizione '{n.get('posizione')}' non nella forma SD/<Sezione>, US-nn o US-nn/CA-nn.m.")
            nc.append({"regola": regola, "gravita": gravita, "posizione": posizione,
                       "chi": str(n.get("chi", "")).strip().lower(), "evidenza": n.get("evidenza", "")})
        dichiarato = SEMAFORI.get(str(v.get("semaforo", "")).strip().lower())
        calcolato = semaforo(nc)
        if dichiarato and dichiarato != calcolato:
            avvisi.append(f"{nome}: il report dichiara {dichiarato}, ma le sue non conformità danno {calcolato}. "
                          f"Conta il semaforo calcolato dalle non conformità.")
        report[nome] = nc
    return report


def confronta_vista(rif, report, regole, campo_semaforo):
    """Numeri di una vista: semaforo, non conformità trovate, mancate, non previste."""
    r = {"documenti": [], "semaforo_uguale": 0, "rosso_verde": [], "attese": {"Bloccante": 0, "Non bloccante": 0},
         "trovate": {"Bloccante": 0, "Non bloccante": 0}, "mancate": [], "non_previste": [], "gravita_diversa": []}
    for nome, d in rif.items():
        atteso = [n for n in d["non_conformita"] if n["regola"] in regole]
        if campo_semaforo:
            sem_atteso = d[campo_semaforo]
        else:
            sem_atteso = semaforo(atteso)
        gruppo = [n for n in report.get(nome, []) if n["regola"] in regole]
        sem_gruppo = semaforo(gruppo) if nome in report else "manca"
        uguale = sem_gruppo == sem_atteso
        r["semaforo_uguale"] += uguale
        if sem_atteso == "Rosso" and sem_gruppo == "Verde":
            r["rosso_verde"].append(nome)
        chiavi_gruppo = {(n["regola"], n["posizione"]): n for n in gruppo}
        chiavi_attese = {(n["regola"], n["posizione"]) for n in atteso}
        for n in atteso:
            r["attese"][n["gravita"]] += 1
            g = chiavi_gruppo.get((n["regola"], n["posizione"]))
            if g is None:
                r["mancate"].append((nome, n))
            else:
                r["trovate"][n["gravita"]] += 1
                if g["gravita"] != n["gravita"]:
                    r["gravita_diversa"].append((nome, n, g["gravita"]))
        for chiave, g in chiavi_gruppo.items():
            if chiave not in chiavi_attese:
                r["non_previste"].append((nome, g))
        r["documenti"].append((nome, d["tipo"], sem_atteso, sem_gruppo, uguale))
    return r


def righe_vista(titolo, v, n_doc, con_semaforo=True):
    out = [f"## {titolo}", ""]
    if con_semaforo:
        out.append(f"- Semaforo uguale ai risultati attesi: {v['semaforo_uguale']} documenti su {n_doc}")
        out.append(f"- Documenti Rossi nei risultati attesi che per voi sono Verdi: {len(v['rosso_verde'])}"
                   + (f" ({', '.join(v['rosso_verde'])})" if v["rosso_verde"] else ""))
        for g, etichetta in (("Bloccante", "bloccanti"), ("Non bloccante", "non bloccanti")):
            if v["attese"][g] or v["trovate"][g]:
                out.append(f"- Non conformità {etichetta} trovate: {v['trovate'][g]} su {v['attese'][g]}")
    else:
        trovate, attese = sum(v["trovate"].values()), sum(v["attese"].values())
        out.append(f"- Criteri non misurabili trovati: {trovate} su {attese}")
    out.append(f"- Segnalazioni non previste dai risultati attesi: {len(v['non_previste'])}")
    if v["mancate"]:
        out += ["", "Mancate:", ""] + [f"- {nome}, {n['posizione'].upper()}: {n['regola']} ({n['gravita']}). {n['descrizione']}"
                                        for nome, n in v["mancate"]]
    if v["gravita_diversa"]:
        out += ["", "Trovate con una gravità diversa dai risultati attesi:", ""] + [
            f"- {nome}, {n['posizione'].upper()}: {n['regola']}, per voi {g}, nei risultati attesi {n['gravita']}"
            for nome, n, g in v["gravita_diversa"]]
    if v["non_previste"]:
        out += ["", "Non previste, da guardare una per una: difetto vero o falso allarme?", ""] + [
            f"- {nome}, {g['posizione'].upper()}: {g['regola']} ({g['gravita']}). {g['evidenza']}"
            for nome, g in v["non_previste"]]
    out.append("")
    return out


def main():
    p = argparse.ArgumentParser(description="Confronta i report del gruppo con i risultati attesi.")
    p.add_argument("insieme", choices=INSIEMI, help="giornata (busta 1) oppure nuovi (busta 3)")
    p.add_argument("--report", default="report", help="cartella con i report .json del gruppo (default: report)")
    a = p.parse_args()

    file_rif, descrizione, busta = INSIEMI[a.insieme]
    rif = leggi_riferimento(RADICE / file_rif)
    avvisi = []
    report = leggi_report(RADICE / a.report, set(rif), avvisi)
    n_doc = len(rif)
    mancanti = [d for d in rif if d not in report]

    meccanico = confronta_vista(rif, report, MECCANICHE, "semaforo_meccanico")
    skill = confronta_vista(rif, report, GIUDIZIO, None)
    completo = confronta_vista(rif, report, MECCANICHE | GIUDIZIO, "semaforo_finale")

    ora = datetime.now()
    out = [f"# Confronto con i risultati attesi: {descrizione}", "",
           f"Calcolato il {ora:%d/%m/%Y alle %H:%M} sulla busta {busta}. Report letti: {len(report)} su {n_doc}."
           + (f" Mancano: {', '.join(mancanti)}." if mancanti else ""), ""]
    if avvisi:
        out += ["Avvisi sui report:", ""] + [f"- {x}" for x in avvisi] + [""]

    out += righe_vista("1. Il programma: le quattro regole di forma", meccanico, n_doc)
    if a.insieme == "giornata":
        soglia = math.ceil(C4_QUOTA * n_doc)
        manca_bloccanti = meccanico["trovate"]["Bloccante"] < meccanico["attese"]["Bloccante"]
        motivi = []
        if manca_bloccanti:
            motivi.append("manca almeno una non conformità bloccante")
        if meccanico["rosso_verde"]:
            motivi.append("un documento Rosso risulta Verde")
        if meccanico["semaforo_uguale"] < soglia:
            motivi.append(f"semaforo uguale su {meccanico['semaforo_uguale']} documenti, ne servono {soglia}")
        out += [f"C4: {'raggiunto' if not motivi else 'non ancora raggiunto: ' + '; '.join(motivi)}.", ""]

    out += righe_vista("2. Criteri misurabili, la skill del pomeriggio", skill, n_doc, con_semaforo=False)
    out += righe_vista("3. Il revisore completo, con il semaforo finale", completo, n_doc)

    out += ["## Documento per documento", "",
            "| Documento | Tipo | Programma: risultato atteso | Programma: voi | Finale: risultato atteso | Finale: voi |",
            "|---|---|---|---|---|---|"]
    finale = {nome: (sa, sg) for nome, _, sa, sg, _ in completo["documenti"]}
    for nome, tipo, sa, sg, _ in meccanico["documenti"]:
        fa, fg = finale[nome]
        out.append(f"| {nome} | {tipo} | {sa} | {sg} | {fa} | {fg} |")
    out.append("")

    testo = "\n".join(out)
    print(testo)
    cartella = RADICE / "risultati"
    cartella.mkdir(exist_ok=True)
    destinazione = cartella / f"confronto-{a.insieme}-{ora:%H%M}.md"
    destinazione.write_text(testo, encoding="utf-8")
    print(f"Salvato in {destinazione.relative_to(RADICE)}")


if __name__ == "__main__":
    main()
