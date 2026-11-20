# Le buste e il confronto con i risultati attesi: passi 5 e 8

I risultati attesi sono, per ogni documento, il report che il revisore dovrebbe scrivere: il semaforo giusto e i problemi che il documento ha davvero, con il punto esatto. Li ha preparati chi ha organizzato la giornata, applicando la checklist. Stanno nelle buste, cioè zip protetti da password nella cartella `buste/`. Il gruppo apre una busta da solo, nel terminale, quando Maurizio condivide la password. Tu non apri e non leggi le buste; puoi lanciare lo script di confronto, che legge i risultati attesi e stampa i numeri.

Molti partecipanti non hanno mai usato il terminale dell'IDE. Se un gruppo non lo trova, digli di chiamare Maurizio o Andrea, che lo mostrano nell'ambiente. I comandi si incollano nel terminale e si lanciano con Invio.

## Passo 5: busta 1 e correzioni (14:00)

Cosa dici al gruppo:

1. Quando Maurizio condivide la password, nel terminale scrivete `python3 strumenti/apri_busta.py 1` e inserite la password. Lo script mette i risultati attesi in `buste/busta_1/`.
2. Scrivete `python3 strumenti/confronta.py giornata`. Lo script stampa i numeri e li salva in `risultati/`.
3. Leggete la parte 1, "Il programma". In fondo dice se C4 è raggiunto.
4. Per ogni riga dell'elenco "Mancate", nella seconda chat scrivete il testo del passo 5 del README, con la riga incollata: Kiro corregge il programma e rilancia test e programma.
5. Rilanciate il confronto, finché in fondo alla parte 1 c'è scritto "C4: raggiunto".

Come si leggono le altre parti dell'uscita:

- Avvisi sui report: vanno sistemati per primi, perché un nome di regola o una posizione sbagliati fanno contare un problema come mancato.
- Gravità diversa: quasi sempre il programma non legge la gravità dal file YAML.
- Non previste: le guarda una persona del gruppo. Se è un difetto vero che i risultati attesi non hanno, lo dice a Maurizio o ad Andrea; se è un falso allarme, si corregge il programma. La decisione va nel registro.
- Parte 2, criteri misurabili: alle 14:00 è normale che sia a zero, la skill arriva dopo.

Le correzioni devono valere per qualunque documento: niente condizioni sui nomi dei file. Ogni giro (correzione e numeri) va nel registro.

C4 con prova: hai lanciato tu `python3 strumenti/confronta.py giornata` e dice "C4: raggiunto".

## Passo 8: i documenti nuovi e la consegna (15:30 e 16:00)

Cosa dici al gruppo:

1. Alle 15:30, quando Maurizio condivide la password: `python3 strumenti/apri_busta.py 2`. I 6 documenti nuovi sono in `buste/busta_2/sd/` e `buste/busta_2/user_story/`.
2. Nella seconda chat scrivete il primo testo del passo 8 del README: il programma gira sui documenti nuovi e scrive report e testo nelle stesse cartelle degli altri.
3. Aprite una sessione nuova con `+`, con l'agente Default, e scrivete il secondo testo del passo 8 del README, quello che comincia con `/criteri-misurabili`: Kiro usa la skill sui criteri dei documenti nuovi.
4. È un solo giro: dopo non si corregge niente. Il numero vale perché è il primo.
5. Alle 16:00, quando Maurizio condivide la password: `python3 strumenti/apri_busta.py 3`, poi `python3 strumenti/confronta.py nuovi`.
6. Scrivete i numeri nel registro come sono, anche se sono peggiori di quelli della mattina. È un'informazione utile: dice quanto il revisore vale su documenti mai visti. Se peggiorano molto, chiedi al gruppo quale scelta potrebbe essere troppo legata ai documenti della mattina, e annota la risposta.
7. Scaricate il lavoro: `python3 strumenti/consegna.py <numero del gruppo>`, poi nell'esplorazione file dell'IDE tasto destro su `consegna/gruppo-<n>.zip` e **Download**. Dettagli in `consegna.md`.

Ricorda al gruppo che tu non puoi leggere i documenti nuovi: il giro lo fa la seconda chat.

C6 con prova: c'è il confronto sui documenti nuovi in `risultati/` e i numeri sono nel registro.
