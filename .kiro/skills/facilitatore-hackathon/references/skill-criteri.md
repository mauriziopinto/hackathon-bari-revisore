# Il pomeriggio: la skill sui criteri misurabili, passi 6 e 7

## Cosa costruisce il gruppo

Una skill di Kiro, cioè una cartella con istruzioni che Kiro segue quando gli serve: `.kiro/skills/criteri-misurabili/`, con dentro

- `SKILL.md`, che comincia con `name: criteri-misurabili` e una `description` che dice cosa fa la skill e quando usarla;
- `references/regole.md`, con la regola, gli esempi e il formato del problema da segnalare.

La regola, come nel README: l'esito di ogni criterio di accettazione è un valore, una soglia o un risultato che un tester può osservare e dire sì o no. Un criterio può essere scritto nel formato "Dato..., quando..., allora..." e avere comunque un esito vago. Un criterio non verificabile è bloccante. La regola vale per i criteri di accettazione, non per il testo della storia.

## Passo 6: scrivere la skill (14:30)

Cosa dici al gruppo:

1. Nella seconda chat scrivete il testo del passo 6 del README. Kiro crea la cartella della skill con `SKILL.md` e `references/regole.md`, e lascia lo spazio per regola ed esempi.
2. Aprite `references/regole.md` e scrivete voi la regola: quando l'esito di un criterio si può verificare, e quando no.
3. Aggiungete almeno tre esempi sbagliati e tre giusti, inventati da voi.
4. Scrivete come Kiro deve segnalare un problema: nel file JSON del documento, con `regola` `criteri_misurabili`, `gravita` `Bloccante`, `chi` `kiro`, la `posizione` del criterio (`US-nn/CA-nn.m`) e come `evidenza` la frase esatta del criterio.

Le scelte che fanno la differenza nei numeri sono queste. Tutti e quattro i gruppi scrivono la stessa regola, quindi la differenza la fanno qui. Falle fare al gruppo, una alla volta, e annota nel registro cosa ha scelto e perché:

1. Come descrive la regola: cosa si guarda, cosa rende un esito verificabile, cosa no.
2. Quali esempi dà a Kiro. Gli esempi sono inventati dal gruppo e non vengono dai documenti del dataset: un esempio copiato da un documento insegna quel documento, non la regola. Ne servono sia sbagliati sia giusti, e vaghi in modi diversi: un tempo senza soglia, un esito che dipende da un giudizio, un esito che non dice cosa succede.
3. Come Kiro riceve il testo: i file in `testo/` scritti dal programma, criterio per criterio, sono più facili da giudicare del documento Word.
4. Come Kiro scrive il problema: sempre la frase esatta del criterio, così una persona lo verifica in pochi secondi.

Una lista di parole vietate da sola non basta: "a breve" e "nel modo più opportuno" sono vaghi in modi diversi, e una lista non trova le frasi che non conosce. Se il gruppo vuole usarla, va bene come primo filtro, ma la decisione resta alla skill.

Fatto quando: `SKILL.md` e `references/regole.md` sono scritti, con la regola, gli esempi e il formato del problema.

## Passo 7: provare e misurare la skill (15:00)

Cosa dici al gruppo:

1. Aprite una sessione nuova con `+` in alto nella chat, con l'agente Default. Una sessione nuova non sa niente di quello che avete detto prima, quindi il risultato dipende solo dalla skill.
2. Scrivete il testo del passo 7 del README. Comincia con `/criteri-misurabili`: è il modo per dire a Kiro di usare la skill.
3. Kiro legge i criteri nei file di `testo/` e aggiunge i problemi trovati ai file JSON e Markdown in `report/`.
4. Nel terminale: `python3 strumenti/confronta.py giornata`, parte 2 "Criteri misurabili": quanti criteri non verificabili Kiro trova, quanti ne manca e quanti ne segnala in più.
5. Cambiate una cosa alla volta nella skill (la descrizione della regola, un esempio, il formato), e rifate i punti da 1 a 4. Ogni versione va nel registro con i suoi numeri.

C5 con prova: hai letto `SKILL.md` e `references/regole.md`, e nel registro ci sono i numeri di almeno un giro misurato.
