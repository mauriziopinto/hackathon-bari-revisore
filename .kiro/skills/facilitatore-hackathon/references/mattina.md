# La mattina: passi da 0 a 4

I passi sono gli stessi del README, sezione "Cosa fate, passo per passo". Il testo da incollare in chat è nel README: indicalo con il numero del passo, oppure ricopialo identico. Dai un passo alla volta, nell'ordine, e passa al successivo solo quando il "fatto quando" è vero.

Molti partecipanti non hanno mai usato Kiro. Ogni volta che chiedi di fare qualcosa in Kiro, di' in quale chat (la vostra con il facilitatore, oppure la seconda chat) e cosa cliccare, con il nome esatto che si vede sullo schermo.

## Passo 0: le due chat (10:00)

Il gruppo tiene aperte due sessioni di chat di Kiro per tutta la giornata: questa, con te, e una seconda per costruire il revisore. Se il gruppo ti scrive da una chat sola, spiega come aprire la seconda:

1. In alto nel pannello della chat cliccate `+`: si apre una sessione nuova, con la schermata "Let's build".
2. Lì costruite il revisore. Con me continuate a parlare in questa chat.

Chiedi anche chi fa cosa nel gruppo (ruoli in `giornata.md`) e i nomi dei partecipanti, e scrivili nel registro.

Fatto quando: la seconda chat è aperta e il registro ha nomi e ruoli.

## Passo 1: i requisiti (10:15)

Cosa dici al gruppo:

1. Nella seconda chat, nella schermata "Let's build", scegliete **Spec**, poi **Feature**.
2. Incollate il testo del passo 1 del README e premete Invio. Quando Kiro chiede da dove partire, scegliete **Requirements-First**.
3. Kiro scrive `requirements.md` in `.kiro/specs/<nome>/`. Leggetelo insieme.

Quando il gruppo ti dice che `requirements.md` è pronto, leggilo tu e controlla che dica in modo esplicito queste cose. Se una manca, fai la domanda al gruppo ("Dove dice il requisito che la gravità si legge dal file YAML?"), non scrivere tu il requisito:

- le gravità si leggono dal file `config/qualita_doc.yaml` e non sono scritte nel codice;
- la regola `criteri_misurabili` non la applica il programma: la applica la skill del pomeriggio;
- come si riconoscono una sezione della SD, una storia e un criterio di accettazione;
- quando una sezione è "vuota" e quando "manca";
- il formato della posizione: `SD/<Sezione>`, `US-nn`, `US-nn/CA-nn.m`;
- come si calcolano il semaforo e l'idoneità alla KB;
- il testo di ogni documento scritto in `testo/<documento>.md`, che servirà alla skill;
- cosa fa il programma con un file che non riesce a leggere.

Fatto quando: `requirements.md` contiene le quattro regole di forma, la gravità letta dal file YAML e il formato del report.

Nel terminale il passo si fa con `/spec new revisore` e lo stesso testo.

## Passo 2: le domande di Kiro, il design e i task (10:30)

Cosa dici al gruppo:

1. Nella seconda chat scegliete **Analyze Requirements**. Lo trovate in chat, tra le opzioni per continuare, oppure nel menu **Continue** dell'editor, accanto a **Proceed to Design**.
2. Aspettate: l'analisi dura qualche minuto. Poi in chat arrivano le domande di Kiro, una alla volta, ognuna con delle soluzioni proposte.
3. Per ogni domanda scegliete una soluzione o scrivete la vostra risposta. Kiro aggiorna `requirements.md`.
4. Quando le domande sono finite, scegliete **Proceed to Design**: Kiro scrive `design.md`. Leggetelo e approvatelo. Poi Kiro scrive `tasks.md`, la lista dei lavori da fare.

Le domande di Kiro sulla checklist sono il materiale più utile per il QA. Chiedi al gruppo di dirti quelle che riguardano il significato di una regola, con la risposta scelta, e scrivile nel registro sotto "Criteri ambigui".

C1 con prova: hai letto `requirements.md`, `design.md` e `tasks.md` in `.kiro/specs/<nome>/`, e i requisiti coprono i punti del passo 1.

Nel terminale: `/spec analyze_requirements revisore`.

## Passo 3: codice, test e hook (11:00)

Cosa dici al gruppo:

1. Aprite `tasks.md` e cliccate sul primo task. Kiro lo esegue e lo segna come in corso, poi come fatto. Poi passate al successivo.
2. Prima di creare file o lanciare comandi Kiro vi chiede conferma. Leggete cosa vuole fare, poi approvate. Se una richiesta non vi è chiara, chiedetemela.
3. Per l'hook: nella barra laterale aprite la vista **Kiro**. Nella sezione **Agent Hooks** cliccate `+` e scegliete **Ask Kiro to create a hook**.
4. Scrivete il testo del passo 3 del README: "Crea un hook che lanci i test ogni volta che modifichi un file .py o il file config/qualita_doc.yaml." Kiro chiede conferma prima di salvare l'hook in `.kiro/hooks/`: è normale, approvate.

Cose da sapere per rispondere alle domande:

- Un .docx è uno zip di file XML: si legge anche con la sola libreria standard di Python.
- I test: almeno uno per ogni regola bloccante. Un buon test usa un esempio piccolo e inventato. Un test che dice "questo documento del dataset è rosso" impara il dataset, non la regola.
- Per sapere se c'è pytest: `python3 -m pytest --version`. Se non c'è, Kiro scrive i test con `unittest` e si lanciano con `python3 -m unittest`.
- L'hook parte solo quando è Kiro a modificare un file. Se il gruppo modifica a mano nell'editor, i test vanno lanciati a mano.

C2 con prova: hai lanciato tu i test (`python3 -m pytest -q` oppure `python3 -m unittest`), sono verdi, e c'è almeno un test per ogni regola bloccante.

Nel terminale: `/spec run revisore` esegue i task.

## Passo 4: i report (12:00)

Cosa dici al gruppo:

1. Nella seconda chat scrivete: "Fai girare il programma su tutti i documenti di dataset/ e mostrami il semaforo di ognuno."
2. Nella cartella `report/` controllate che per ognuno degli 8 documenti ci siano un file `.md` e un file `.json`, e che ci sia la cartella `testo/` con il testo dei documenti.
3. Aprite due report e confrontateli con il documento Word: il problema c'è davvero, nel punto indicato?
4. Chiedete a Kiro: "Nel file config/qualita_doc.yaml rendi bloccante il Glossario e rifai girare il programma". Un documento con il Glossario vuoto diventa rosso: è la prova che le regole stanno nel file. Poi chiedetegli di rimettere il valore com'era.

Controlla tu con il gruppo:

- nei JSON i nomi delle regole sono quelli del file YAML, la gravità è `Bloccante` o `Non bloccante`, la posizione è nella forma giusta, `chi` è `programma`;
- ogni non conformità ha un'evidenza: la frase del documento o cosa manca.

C3 con prova: hai letto almeno due report JSON e due Markdown, e sono completi.

Se alle 12:30 il programma non legge ancora i file Word, il gruppo chiama Maurizio o Andrea: c'è una busta `aiuto` con uno script che estrae il testo.
