# La giornata

Giovedì 26 novembre 2026, sede Fastweb di Bari, dalle 9:30 alle 17:30. Da 15 a 16 persone del QA in quattro gruppi. Maurizio Pinto (Senior Solutions Architect di AWS) conduce la giornata, chiama i checkpoint e condivide le password delle buste. Con lui c'è Andrea Soria (Technical Account Manager di AWS che segue Fastweb): per qualunque problema il gruppo può chiedere a uno dei due. Gli orari sono di massima: se Maurizio li cambia, seguite i suoi.

## Le fasi

Le fasi corrispondono ai passi del README, sezione "Cosa fate, passo per passo".

| Passo | Orario | Cosa si fa | Fatto quando | Criterio |
|---|---|---|---|---|
| 0 Le due chat | 10:00 | Seconda chat aperta con `+`, registro creato, ruoli scelti | la seconda chat è aperta e il registro ha nomi e ruoli | |
| 1 I requisiti | 10:15 | Spec, Feature, testo del passo 1, Requirements-First | `requirements.md` contiene le quattro regole di forma, la gravità letta dal file YAML e il formato del report | |
| 2 Domande, design, task | 10:30 | Analyze Requirements, risposte alle domande, Proceed to Design | ci sono `requirements.md`, `design.md` e `tasks.md`, e le domande sulla checklist sono nel registro | C1 |
| 3 Codice e test | 11:00 | Task eseguiti uno alla volta da `tasks.md`, hook dei test | i test passano, almeno uno per ogni regola bloccante; l'hook c'è | C2 |
| 4 I report | 12:00 | Programma sugli 8 documenti di `dataset/`, controllo dei report, prova del Glossario bloccante | un `.md` e un `.json` per documento in `report/`, e il testo in `testo/` | C3 |
| Pranzo | 13:00 | | | |
| 5 Busta 1 | 14:00 | `apri_busta.py 1`, `confronta.py giornata`, correzioni | il confronto dice "C4: raggiunto" | C4 |
| 6 La skill | 14:30 | Skill in `.kiro/skills/criteri-misurabili/`, regola ed esempi inventati | `SKILL.md` e `references/regole.md` scritti | |
| 7 Prova della skill | 15:00 | Sessione nuova, `/criteri-misurabili`, confronto parte 2 | i numeri di almeno un giro sono nel registro | C5 |
| 8 Documenti nuovi e consegna | 15:30 e 16:00 | `apri_busta.py 2`, un solo giro; `apri_busta.py 3`, `confronta.py nuovi`; `consegna.py` | i numeri sono nel registro anche se peggiorano, e lo zip è scaricato | C6 |
| Demo | 16:45 | 5 minuti per gruppo | il gruppo ha presentato | |
| Decisione | 17:10 | Pietro Ricciardi e Giuseppe De Marzo, come giudici, dicono quali idee si portano avanti | | |

Il goal è raggiunto con i criteri da C1 a C4. C5 e C6 sono la skill e la misura sui documenti nuovi.

## Ruoli nel gruppo

Proponi questi ruoli all'inizio. Il gruppo può scambiarli quando vuole; in un gruppo di tre, gli ultimi due ruoli li fa la stessa persona.

- chi guida Kiro: scrive le istruzioni e approva le operazioni;
- chi controlla: legge codice, test e report, e dice se il risultato è giusto;
- chi tiene le regole: decide come si interpreta un criterio della checklist e annota i casi dubbi;
- chi tiene il registro e il tempo: aggiorna il registro con te e guarda l'orologio.

## Se il gruppo è in ritardo

- Passo 2 oltre le 11:15: rispondete solo alle domande di Kiro sulla checklist, approvate il design così com'è e passate ai task.
- Programma che alle 12:30 non legge ancora i .docx: chiamate Maurizio o Andrea. C'è una busta `aiuto` con uno script che estrae il testo; la password la danno loro.
- Report non pronti alle 13:00: producete i report per i documenti che il programma legge già, gli altri dopo pranzo.
- Confronto oltre le 14:45: correggete solo le non conformità bloccanti mancate e passate alla skill.
- Skill non pronta alle 15:30: usatela così com'è sui documenti nuovi. Un numero basso è un risultato, una skill mai provata no.
- Alle 16:30 in ogni caso: scaricate la cartella del gruppo prima di tutto il resto.

## Le regole del gioco

- Le buste si aprono solo all'ora stabilita, dal terminale, dal gruppo. Kiro non le apre e non le legge prima.
- Il programma e la skill non citano i nomi dei documenti: devono valere per qualunque documento.
- I documenti delle 15:30 si usano una volta sola: un run, poi si guardano i numeri, senza correggere e rifare.
- Una segnalazione non prevista dai risultati attesi non è per forza sbagliata: la guarda una persona e decide se è un difetto vero.
- Si lavora solo sui documenti del repository. Niente documenti reali: gli ambienti sono temporanei e fuori da Fastweb.
