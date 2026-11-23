# Formato standard della User Story

Questo file di steering definisce il formato atteso delle User Story. Le User Story in input sono file Word (.docx). Una User Story è un documento a sé: non dipende da una Solution Design e si valuta da sola.

## Formato della storia

Ogni User Story dichiara ruolo, azione e beneficio:

> Come <ruolo>, voglio <azione>, affinché <beneficio>.

## Formato dei criteri di accettazione

Ogni User Story ha almeno un criterio di accettazione. Ogni criterio ha un ID nella forma `CA-nn.m` e segue il formato Given/When/Then, che nei nostri documenti si scrive in italiano:

> Dato <contesto>, quando <azione o evento>, allora <esito>.

Il criterio può cominciare con Dato, Data, Dati o Date, secondo il genere e il numero della parola che segue: "Dato un tecnico...", "Data una fascia oraria...", "Dati due tecnici...", "Date tre richieste...". Sono corrette tutte e quattro le forme. Le tre parti devono comparire in quest'ordine: il contesto, poi "quando", poi "allora".

L'esito deve essere misurabile: un valore, una soglia o un risultato che un tester può osservare. "Il sistema funziona correttamente" non è un esito misurabile.

## Struttura del documento delle User Story

- In apertura, il titolo "User Story - <nome dell'iniziativa>".
- Per ogni User Story:
  - un titolo nella forma `US-nn - <titolo>`;
  - il testo della storia;
  - la voce "Criteri di accettazione:" seguita dall'elenco dei criteri.

Quali regole sono bloccanti non è scritto qui ma nel file `config/qualita_doc.yaml`.
