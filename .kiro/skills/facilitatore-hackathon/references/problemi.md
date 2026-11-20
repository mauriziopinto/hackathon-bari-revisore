# Quando qualcosa non va

| Quello che si vede | Cosa fare |
|---|---|
| Nella chat non compare l'agente "facilitatore", oppure Kiro non conosce il template della SD | Il workspace non è considerato affidabile, quindi Kiro non carica agenti, steering e skill del repository. Chiamate Maurizio o Andrea. |
| `python3 -m pytest` dice che pytest non c'è | Usate `python3 -m unittest`, e chiedete a Kiro di scrivere i test in quella forma. |
| L'hook non parte | Parte solo quando è Kiro a modificare un file. Se avete modificato a mano, lanciate i test voi o chiedete a Kiro di fare la modifica. |
| Kiro chiede di approvare la scrittura in `.kiro/hooks/` o `.kiro/agents/` | È normale: Kiro chiede sempre conferma per quelle cartelle. Approvate se è l'hook dei test. |
| Kiro chiede di leggere un file in `buste/` | Rifiutate. Le buste si aprono solo all'ora stabilita. |
| Kiro propone di lanciare `apri_busta.py` | Rifiutate: la busta la apre il gruppo nel terminale, con la password che condivide Maurizio. |
| `confronta.py` dice "Non trovo buste/busta_1/..." | La busta non è ancora aperta: `python3 strumenti/apri_busta.py 1`, con la password. |
| `apri_busta.py` dice "Password sbagliata" | Controllate maiuscole, trattino e numeri, poi riprovate. |
| `confronta.py` mostra degli avvisi sui report | Sistemate prima quelli: un nome di regola o una posizione sbagliati fanno contare una non conformità come mancata. I nomi giusti sono nel README e in `config/qualita_doc.yaml`. |
| `confronta.py` dice che un report dichiara un semaforo diverso da quello delle sue non conformità | Il programma calcola il semaforo in modo diverso dalla regola del README. Conta quello calcolato dalle non conformità. |
| Alle 12:30 il programma non legge ancora i .docx | Chiamate Maurizio o Andrea per la busta `aiuto`. Dopo averla aperta, copiate lo script in `strumenti/` con `cp buste/aiuto/estrai_testo.py strumenti/` (lo dice anche `apri_busta.py`). Poi nella seconda chat chiedete a Kiro di usare `strumenti/estrai_testo.py` per leggere i file Word. |
| Un partecipante vuole provare un documento vero | Non oggi: gli ambienti sono temporanei e fuori da Fastweb. Si prova dopo, dentro Fastweb. |
| Il gruppo è bloccato da più di 20 minuti sullo stesso punto | Chiamate Maurizio o Andrea. |
