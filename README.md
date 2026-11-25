# Hackathon QE&TA con Kiro, Bari, 26 novembre

Questo è il repository di partenza del vostro gruppo. Qui trovate il goal, i documenti, le regole della checklist, il formato del report e come si svolge la giornata.

La giornata la conduce Maurizio Pinto, Senior Solutions Architect di AWS. Con lui c'è Andrea Soria, Technical Account Manager di AWS che segue Fastweb. Per qualunque problema potete chiedere a uno dei due.

## Il goal

Entro le 17:30 ogni gruppo costruisce un revisore automatico per SD e User Story. Gli date un documento Word, e il revisore scrive un report che dice:

- se il documento può entrare nella Knowledge Base (KB), cioè l'archivio di documenti buoni da riusare che Fastweb vuole costruire;
- quali problemi ha, e dove: la sezione della SD oppure la storia e il criterio.

Il revisore ha due parti:

- la mattina scrivete con Kiro un programma Python che controlla le quattro regole di forma, per esempio "la SD ha la sezione Scopo compilata?". Con lo stesso documento dà sempre la stessa risposta, e si può testare;
- il pomeriggio scrivete una skill, cioè un file di istruzioni con esempi che Kiro segue, per la quinta regola: Kiro legge ogni criterio di accettazione e decide se un tester può verificarne l'esito.

Quanto ci si può fidare del revisore lo misurate confrontando i suoi report con i risultati attesi, che sono nelle buste. I risultati attesi sono, per ogni documento, il report che il revisore dovrebbe scrivere: il semaforo giusto e i problemi che il documento ha davvero, con il punto esatto. Li abbiamo preparati applicando la checklist a ogni documento.

## Cosa fate, passo per passo

Qui trovate ogni passo della giornata: dove cliccare in Kiro e il testo da incollare nella chat. Il facilitatore vi dà gli stessi passi, uno alla volta.

### Prima di cominciare: due sessioni di chat

Per tutta la giornata tenete aperte due sessioni di chat di Kiro, una accanto all'altra:

- una con il facilitatore, che vi dice a che punto siete e qual è il passo successivo;
- una per costruire il revisore.

Come si fa:

1. Aprite la chat di Kiro: `Ctrl+L` (su Mac `Cmd+L`), oppure l'icona della chat in alto a destra.
2. Cliccate il nome dell'agente in fondo alla chat, dove c'è scritto "Default". Nell'elenco, sotto **Workspace**, scegliete **facilitatore** e scrivete "Siamo il gruppo 2" (con il vostro numero).
3. Per la seconda sessione cliccate `+` in alto nel pannello della chat. Si apre una sessione nuova, con la schermata "Let's build".

Nel terminale lo stesso si fa con `kiro-cli chat --v3 --agent facilitatore` per il facilitatore e `kiro-cli` per la seconda sessione.

### Passo 1. La spec: i requisiti (10:15)

1. Nella seconda sessione, nella schermata "Let's build", scegliete **Spec**.
2. Kiro chiede se state costruendo una funzione nuova o correggendo un bug: scegliete **Feature**.
3. Incollate questo testo e premete Invio. Quando Kiro chiede da dove partire, scegliete **Requirements-First**:

   ```
   Voglio un programma Python che faccia da revisore automatico dei documenti Word nella cartella dataset/: le SD in dataset/sd/ e le User Story in dataset/user_story/.
   Per ogni documento il programma applica le quattro regole di forma descritte nel README, nella sezione "Le regole della checklist", e legge la gravità di ogni regola dal file config/qualita_doc.yaml, senza scriverla nel codice.
   La regola criteri_misurabili non la applica il programma: la applicherà una skill di Kiro nel pomeriggio.
   Per ogni documento il programma scrive in report/ un file .md da leggere e un file .json nel formato descritto nel README, nella sezione "Il report". Scrive anche il testo del documento in testo/<documento>.md, che servirà alla skill.
   Il programma usa solo la libreria standard di Python e non cita mai i nomi dei documenti: deve funzionare su qualunque documento.
   ```

4. Kiro scrive il file `requirements.md` in `.kiro/specs/<nome>/`. Leggetelo e controllate che ci siano le quattro regole di forma, la gravità letta dal file YAML e il formato del report. Se manca qualcosa, chiedetelo a Kiro in chat.

Fatto quando: `requirements.md` contiene tutte e tre le cose.

Nel terminale: `/spec new revisore`, poi lo stesso testo.

### Passo 2. Le domande di Kiro, il design e i task (10:30)

1. Quando i requisiti sono pronti, scegliete **Analyze Requirements**. Lo trovate in chat tra le opzioni per continuare, oppure nel menu **Continue** dell'editor, accanto a **Proceed to Design**.
2. L'analisi dura qualche minuto. Poi in chat arrivano le domande di Kiro, una alla volta, ognuna con delle soluzioni proposte. Per esempio: quando una sezione è "vuota"?
3. Per ogni domanda scegliete una soluzione o scrivete la vostra risposta. Kiro aggiorna `requirements.md`. Decidere come si interpreta la checklist è lavoro da QA: dite al facilitatore le domande che vi sembrano importanti, le annota nel registro.
4. Scegliete **Proceed to Design**: Kiro scrive `design.md`. Leggetelo e approvatelo.
5. Kiro scrive `tasks.md`, la lista dei lavori da fare.

Fatto quando: tutte le domande hanno una risposta, e in `.kiro/specs/<nome>/` ci sono `requirements.md`, `design.md` e `tasks.md`.

Nel terminale: `/spec analyze_requirements revisore`.

### Passo 3. Codice e test (11:00)

1. Aprite `tasks.md` e cliccate sul primo task. Kiro lo esegue e lo segna come in corso, poi come fatto. Poi passate al successivo.
2. Kiro scrive il codice e i test, e vi chiede conferma prima di creare file o lanciare comandi: leggete cosa vuole fare, poi approvate.
3. Create l'hook che rilancia i test. Nella barra laterale aprite la vista **Kiro**; nella sezione **Agent Hooks** cliccate `+`, scegliete **Ask Kiro to create a hook** e scrivete:

   ```
   Crea un hook che lanci i test ogni volta che modifichi un file .py o il file config/qualita_doc.yaml.
   ```

   Kiro vi chiede conferma prima di salvare l'hook in `.kiro/hooks/`: è normale. L'hook parte solo quando è Kiro a modificare un file, non quando lo modificate voi a mano.

Fatto quando: i test passano, con almeno un test per ogni regola bloccante.

Nel terminale: `/spec run revisore` per eseguire i task; l'hook lo chiedete in chat con lo stesso testo.

### Passo 4. I report (12:00)

1. Scrivete in chat:

   ```
   Fai girare il programma su tutti i documenti di dataset/ e mostrami il semaforo di ognuno.
   ```

2. Controllate la cartella `report/`: per ognuno degli 8 documenti ci sono un file `.md` e un file `.json`.
3. Aprite due report e confrontateli con il documento Word: il problema segnalato c'è davvero, nel punto indicato?
4. Provate che le regole stanno davvero nel file YAML. Chiedete a Kiro: "Nel file config/qualita_doc.yaml rendi bloccante il Glossario e rifai girare il programma". Se un documento ha il Glossario vuoto, diventa rosso. Poi chiedetegli di rimettere il valore com'era.

Fatto quando: c'è un report per ognuno degli 8 documenti e i test passano.

### Passo 5. Busta 1: i risultati attesi e le correzioni (14:00)

1. Quando Maurizio condivide la password, nel terminale scrivete `python3 strumenti/apri_busta.py 1` e inserite la password.
2. Lanciate `python3 strumenti/confronta.py giornata` e leggete la parte 1, "Il programma".
3. Per ogni problema nell'elenco "Mancate", scrivete a Kiro:

   ```
   Il confronto dice che il programma non ha trovato questo problema: <incollate la riga>. Correggi il programma in modo che valga per qualunque documento, poi rilancia i test e il programma.
   ```

4. Rilanciate il confronto, finché in fondo alla parte 1 c'è scritto "C4: raggiunto".

Fatto quando: "C4: raggiunto".

### Passo 6. La skill (14:30)

1. Scrivete in chat:

   ```
   Crea una skill di Kiro in .kiro/skills/criteri-misurabili/, con un file SKILL.md e un file references/regole.md. La skill legge i criteri di accettazione delle User Story e segnala quelli con un esito che un tester non può verificare. In references/regole.md lascia lo spazio per la regola e per gli esempi giusti e sbagliati: li scriviamo noi.
   ```

2. Aprite `references/regole.md` e scrivete voi la regola: quando l'esito di un criterio si può verificare, e quando no.
3. Aggiungete almeno tre esempi sbagliati e tre giusti, inventati da voi. Non copiateli dai documenti del dataset: un esempio copiato insegna quel documento, non la regola.
4. Scrivete come deve essere segnalato un problema: nel file JSON del documento, con `regola` `criteri_misurabili`, `gravita` `Bloccante`, `chi` `kiro`, la `posizione` del criterio e come `evidenza` la frase esatta.

Fatto quando: `SKILL.md` e `references/regole.md` sono scritti, con la regola e gli esempi.

### Passo 7. Provate la skill (15:00)

1. Aprite una sessione nuova con `+`, con l'agente Default. Una sessione nuova non sa niente di quello che avete detto prima, quindi il risultato dipende solo dalla skill.
2. Scrivete:

   ```
   /criteri-misurabili Leggi i criteri di accettazione delle User Story nei file della cartella testo/. Per ogni criterio con un esito che non si può verificare, aggiungi il problema al file .json del documento in report/, come dice la skill, e aggiorna il semaforo e il file .md.
   ```

3. Lanciate `python3 strumenti/confronta.py giornata` e leggete la parte 2, "Criteri misurabili": quanti criteri non verificabili Kiro trova, quanti ne manca e quanti ne segnala in più.
4. Cambiate una cosa alla volta nella skill, rifate i punti 1, 2 e 3 e annotate i numeri con il facilitatore.

Fatto quando: avete i numeri di almeno un giro della skill.

### Passo 8. I documenti nuovi e la consegna (15:30 e 16:00)

1. Alle 15:30, quando Maurizio condivide la password, scrivete `python3 strumenti/apri_busta.py 2`. I 6 documenti nuovi sono in `buste/busta_2/`.
2. Scrivete in chat:

   ```
   Fai girare il programma sui documenti in buste/busta_2/sd/ e buste/busta_2/user_story/, scrivendo report e testo nelle stesse cartelle degli altri documenti.
   ```

3. Aprite una sessione nuova con `+`, con l'agente Default, e scrivete:

   ```
   /criteri-misurabili Leggi i criteri di accettazione delle User Story nei file di testo/ dei documenti che sono in buste/busta_2/user_story/. Per ogni criterio con un esito che non si può verificare, aggiungi il problema al file .json del documento in report/, come dice la skill, e aggiorna il semaforo e il file .md.
   ```

   È un solo giro: dopo non si corregge niente.
4. Alle 16:00, quando Maurizio condivide la password, scrivete `python3 strumenti/apri_busta.py 3` e poi `python3 strumenti/confronta.py nuovi`. Scrivete i numeri con il facilitatore, anche se sono peggiori di quelli della mattina.
5. Scaricate il lavoro: `python3 strumenti/consegna.py 2` (con il vostro numero), poi nell'esplorazione file dell'IDE tasto destro su `consegna/gruppo-2.zip` e **Download**.

Fatto quando: i numeri sono nel registro e lo zip è sul vostro computer.

## Cosa c'è nel repository

| Percorso | Contenuto |
|----------|-----------|
| `dataset/sd/` | 4 Solution Design in Word, da `sd_01.docx` a `sd_04.docx` |
| `dataset/user_story/` | 4 documenti di User Story in Word, da `us_01.docx` a `us_04.docx` |
| `config/qualita_doc.yaml` | Le regole della checklist e la loro gravità. Il programma le legge da qui |
| `.kiro/steering/` | Template della SD, formato della User Story e glossario. Kiro li legge in ogni conversazione |
| `.kiro/agents/`, `.kiro/skills/facilitatore-hackathon/` | Il facilitatore della giornata |
| `report/` | Dove il revisore scrive i report. Contiene un esempio inventato (`us_90`), in Markdown e nel formato comune |
| `kb/` | Un esempio inventato di scheda KB |
| `buste/` | Tre zip protetti da password, da aprire solo all'ora indicata, e una busta di aiuto |
| `strumenti/` | `apri_busta.py` apre una busta, `confronta.py` calcola i numeri, `consegna.py` prepara lo zip del lavoro |
| `registro/` | Il registro del gruppo, tenuto dal facilitatore |
| `risultati/` | I confronti con i risultati attesi |
| `presentazione/slide-apertura.html` | Le slide dell'apertura. Per rivederle: tasto destro sul file nell'esplorazione file dell'IDE, **Download**, poi apritelo nel browser del vostro computer. Si cambia slide con le frecce |

I documenti sono inventati, ma costruiti sui template reali. Quali problemi hanno non è scritto da nessuna parte: trovarli è il lavoro del vostro revisore.

## I documenti

SD e User Story sono due tipi di documento indipendenti. Le SD vengono dai progetti waterfall, le User Story dai progetti agile. Una User Story non dipende da nessuna SD e viceversa: ogni documento si valuta da solo, con il proprio semaforo e la propria idoneità alla KB.

Leggere i file Word fa parte del lavoro del programma. Un `.docx` è uno zip di file XML, quindi si legge anche senza librerie esterne.

## Le regole della checklist

La gravità di ogni regola sta in `config/qualita_doc.yaml`. Il programma deve leggerla da lì e non scriverla nel codice: se il file cambia, il risultato cambia senza toccare il codice.

Solution Design:

| Regola | Cosa controlla | Gravità oggi | Chi la controlla |
|--------|----------------|--------------|------------------|
| `sezioni_obbligatorie_sd` | Le sezioni Scopo, Requisiti, Ambiente e Glossario ci sono e non sono vuote | Bloccante per Scopo e Requisiti, non bloccante per Ambiente e Glossario | Programma |

User Story:

| Regola | Cosa controlla | Gravità oggi | Chi la controlla |
|--------|----------------|--------------|------------------|
| `formato_come_voglio_affinche` | La storia dichiara ruolo, azione e beneficio: "Come..., voglio..., affinché..." | Non bloccante | Programma |
| `criteri_accettazione_presenti` | La storia ha almeno un criterio di accettazione | Bloccante | Programma |
| `criteri_formato_dato_quando_allora` | Ogni criterio è nel formato Given/When/Then, in italiano: "Dato..., quando..., allora...". Il criterio può cominciare con Dato, Data, Dati o Date, secondo la parola che segue ("Dato un tecnico...", "Data una fascia oraria..."): sono corrette tutte e quattro | Non bloccante | Programma |
| `criteri_misurabili` | L'esito di ogni criterio è un valore, una soglia o un risultato che un tester può osservare | Bloccante | Kiro, con la skill del pomeriggio |

Un criterio può essere nel formato giusto e avere un esito vago. "Allora il tecnico riceve l'appuntamento in pochi minuti" rispetta il formato ma non è misurabile; "entro 5 minuti" sì. Il programma non può accorgersene: per questo la regola la applica Kiro.

## Semaforo e idoneità alla KB

| Semaforo | Quando | Idoneità alla KB |
|----------|--------|------------------|
| Rosso | Almeno una non conformità bloccante, trovata dal programma o dalla skill. Prevale su tutto | Non idoneo |
| Giallo | Solo non conformità non bloccanti | Idoneo con riserva |
| Verde | Nessuna non conformità | Idoneo |

## Il report

Per ogni documento il revisore scrive due file nella cartella `report/`:

- `<documento>.md`, per le persone, come `report/modello_report.md`;
- `<documento>.json`, nel formato comune, come `report/modello_report.json`.

Il formato comune è uguale per tutti i gruppi, così lo script di confronto calcola i numeri di tutti nello stesso modo. Contiene:

| Campo | Valori |
|-------|--------|
| `documento` | Il nome del file senza estensione, per esempio `sd_02` o `us_03` |
| `tipo` | `sd` oppure `user_story` |
| `semaforo` | `Verde`, `Giallo` oppure `Rosso` |
| `idoneita_kb` | `Idoneo`, `Idoneo con riserva` oppure `Non idoneo` |
| `non_conformita` | L'elenco delle non conformità, vuoto se non ce ne sono |

Ogni non conformità ha questi campi:

| Campo | Valori |
|-------|--------|
| `regola` | Il nome della regola, come nel file `config/qualita_doc.yaml` |
| `gravita` | `Bloccante` oppure `Non bloccante` |
| `posizione` | `SD/<Sezione>` per una sezione della SD, per esempio `SD/Scopo`; `US-03` per una storia; `US-03/CA-03.2` per un criterio |
| `chi` | `programma` oppure `kiro` |
| `evidenza` | La frase esatta del documento, o cosa manca |

## Le buste con password

Nella cartella `buste/` ci sono tre zip protetti da password. Le password le condivide Maurizio all'ora indicata. Ogni busta si apre dal terminale, e la apre il gruppo, non Kiro:

```
python3 strumenti/apri_busta.py 1
```

Lo script chiede la password e mette il contenuto in `buste/busta_1/` (o `busta_2/`, `busta_3/`).

| Ora | Busta | Cosa contiene | Cosa fate |
|-----|-------|---------------|-----------|
| 14:00 | 1 | I risultati attesi sugli 8 documenti della giornata | `python3 strumenti/confronta.py giornata`, poi correggete dove il revisore sbaglia |
| 15:30 | 2 | 6 documenti nuovi, 3 SD e 3 User Story, mai visti da nessun gruppo | Un solo run, con programma e skill così come sono. I report vanno in `report/` come gli altri |
| 16:00 | 3 | I risultati attesi sui documenti nuovi | `python3 strumenti/confronta.py nuovi`, e scrivete i numeri anche se peggiorano |

`confronta.py` stampa i numeri in tre parti (il programma, la skill, il revisore completo) e li salva in `risultati/`. Per il confronto delle 14:00 dice anche se C4 è raggiunto.

Né voi né Kiro dovete aprire una busta prima dell'ora: il confronto non direbbe più niente. Per lo stesso motivo le regole e la skill non devono citare i nomi dei documenti: devono valere per qualunque documento.

C'è anche una busta `aiuto`. Si apre solo se ve lo dicono Maurizio o Andrea, che vi danno la password.

## La giornata

| Ora | Cosa |
|-----|------|
| 9:30 | Apertura: goal, Kiro e regole del gioco |
| 10:00 | Gruppi e ambienti, primo contatto con il facilitatore |
| 10:15 | Spec del programma, con Analyze Requirements |
| 11:00 | Codice, test e report sugli 8 documenti della giornata |
| 13:00 | Pranzo |
| 14:00 | Busta 1: confronto con i risultati attesi |
| 14:30 | La skill sui criteri misurabili, scritta, provata e corretta |
| 15:30 | Busta 2: documenti mai visti, un solo run |
| 16:00 | Busta 3: numeri e limiti. Poi si prepara la demo e si scarica il lavoro |
| 16:45 | Demo, 5 minuti per gruppo |
| 17:10 | Dopo oggi: cosa prosegue, chi lo porta avanti, su quali documenti veri |
| 17:30 | Fine |

Alle 11:00, 13:00, 15:30 e 16:30 c'è un checkpoint: chiedete al facilitatore "a che punto siamo?", perché l'agente non vede l'orologio.

## Quando avete finito

| | Criterio | La prova |
|---|----------|----------|
| C1 | Spec completa: requisiti, design, task | I tre file in `.kiro/specs/` |
| C2 | Test verdi, almeno uno per ogni regola bloccante | L'output dei test |
| C3 | Report per ogni documento: semaforo, idoneità KB, dove sta ogni problema | I report in `report/` |
| C4 | Alle 14:00 il programma trova tutte le non conformità bloccanti, nessun documento Rosso risulta Verde, e il semaforo è giusto su almeno 6 documenti su 8 | Il confronto con la busta 1 |
| C5 | La skill sui criteri misurabili, scritta e misurata | La skill e i suoi numeri |
| C6 | Documenti mai visti: un run, numeri riportati | Il report del run |

In C4 conta solo il programma, perché la skill arriva dopo: lo script confronta il semaforo che danno le quattro regole del programma. Il facilitatore segna un criterio come fatto solo quando vede la prova.

Per tutti i gruppi, sempre: l'elenco dei criteri della checklist che non siete riusciti a trasformare in regola, con il motivo. Per il QA è uno dei risultati più utili della giornata.

Se finite prima: una scheda KB per ogni documento idoneo, come `kb/esempio_scheda_kb.yaml`, oppure una seconda versione della skill da confrontare con la prima.

## Il facilitatore

Nella chat di Kiro scegliete l'agente "facilitatore" e scrivete chi siete, per esempio "Siamo il gruppo 2". Nel terminale: `kiro-cli chat --v3 --agent facilitatore`. Il facilitatore vi dice a che punto siete, vi aiuta con una domanda, poi con il riferimento alla regola, poi con un esempio minimo, e tiene il registro del gruppo in `registro/`. Non scrive il revisore al posto vostro e non può aprire le buste. Per costruire il revisore usate l'agente normale di Kiro.

Per un problema di ambiente, o se siete bloccati da più di 20 minuti, chiamate Maurizio o Andrea.

## Regole dell'ambiente

- Si lavora solo sui documenti di questo repository. Niente documenti reali: questi ambienti sono temporanei e fuori da Fastweb.
- Nessuna scrittura su sistemi esterni.
- L'ambiente si chiude dopo l'evento. Dalle 16:00, e comunque entro le 16:30, create lo zip del lavoro con `python3 strumenti/consegna.py <numero del gruppo>` e scaricatelo dall'esplorazione file dell'IDE: tasto destro su `consegna/gruppo-<n>.zip`, Download.
