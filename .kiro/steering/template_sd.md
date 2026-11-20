# Template SD (Solution Design)

Questo file descrive la struttura del template ufficiale delle Solution Design (SD). Le SD in input sono file Word (.docx) costruiti su questo template.

## Frontespizio

- Codice del documento, nella forma `DTWP00000000 (P000000)`.
- Titolo dell'iniziativa e fase (per esempio MVP1).
- La dicitura "Solution Design".
- EMITTENTE, VERSIONE e DATA EMISSIONE.

## Struttura dei capitoli

I capitoli sono titoli di primo livello, le sezioni sono titoli di secondo livello.

1. **Document management**
   - Cronologia: tabella con Versione, Data, Principali variazioni.
   - Ente richiedente: tabella con Nome, Funzione, Note.
   - Team: tabella con Area, Nome.
   - Riferimenti ad altri documenti: tabella con Rif., Data, Documento.
   - Glossario: tabella con Nome, Definizione.
2. **Executive summary**
   - Scopo: obiettivo dell'iniziativa e funzionalità principali in ambito.
   - Una sezione con il nome della fase (per esempio MVP1): cosa rientra nella fase e cosa è rinviato.
   - Milestone di progetto.
3. **Requisiti di dettaglio**
   - Requisiti: tabella con ID, Titolo, Descrizione, Priorità. Gli ID hanno la forma `REQ-nnn`.
4. **Vincoli e assunzioni**
   - ASSUNZIONI, PUNTI DI ATTENZIONE, OPEN POINT, LIMITAZIONI E SVILUPPI IN FASI SUCCESSIVE.
5. **Soluzione User Journey**
   - Una sezione per ogni percorso utente descritto.
6. **Soluzione Tecnica**
   - Architetture.
   - Funzionalità/Servizi: tabella con Servizio, Descrizione.
   - Ambiente: testo e tabella con Ambiente, Sistema, Utilizzo.
   - Interfacce: tabella con Interfaccia, Sistemi coinvolti, Descrizione.
7. **Impatti sui sistemi**
   - Una sezione per ogni sistema impattato, con impatti funzionali e impatti infrastrutturali.
8. **Scenari di accettazione**
   - Scenari che l'ente richiedente prevede di eseguire in UAT.
9. **Piano di rollout**
   - Pianificazione dei rilasci.

## Sezioni controllate dalla checklist

Quali sezioni sono obbligatorie, e quali di queste sono bloccanti, non è scritto qui ma nel file `config/qualita_doc.yaml`. Il programma deve leggere l'elenco da quel file, non da questo.
