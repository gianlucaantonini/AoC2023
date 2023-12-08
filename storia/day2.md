--- Giorno 2: Enigma del Cubo ---

Sei stato lanciato in alto nell'atmosfera! All'apice della tua traiettoria raggiungi la superficie di una grande isola che fluttua nel cielo. Atterri dolcemente in un morbido mucchio di foglie. Fa piuttosto freddo, ma non vedi molta neve. Un elfo corre verso di te.

L'elfo ti spiega che sei arrivato all'Isola della Neve e si scusa per la mancanza di neve. Sarà felice di spiegarti la situazione, ma il tragitto a piedi e lungo, quindi hai del tempo. Qui sopra, non ricevono molti visitatori; vorresti giocare a un gioco nel frattempo?

Mentre cammini, l'elfo ti mostra una piccola borsa e alcuni cubi che possono essere rossi, verdi o blu. Ogni volta che giochi a questo gioco, nasconderà un numero segreto di cubi di ciascun colore nella borsa e il tuo obiettivo è ottenere informazioni sul numero di cubi.

Per ottenere le informazioni, una volta che una borsa è stata caricata con i cubi, l'elfo infilerà la mano nella borsa, prenderà un pugno di cubi a caso, te li mostrerà e poi li rimetterà nella borsa. Farà questo alcune volte per ogni partita.

Giochi a diverse partite e registri le informazioni da ciascuna partita (il tuo input del puzzle). Ogni partita è elencata con il suo numero di identificazione (come l'11 nella Partita 11: ...) seguito da un elenco separato da punto e virgola di sottoinsiemi di cubi che sono stati rivelati dalla borsa (come 3 blu, 5 verdi, 4 blu).

Ad esempio, il resoconto di alcuni giochi potrebbe apparire così:

Partita 1: 3 blu, 4 rossi; 1 rosso, 2 verdi, 6 blu; 2 verdi
Partita 2: 1 blu, 2 verdi; 3 verdi, 4 blu, 1 rosso; 1 verde, 1 blu
Partita 3: 8 verdi, 6 blu, 20 rossi; 5 blu, 4 rossi, 13 verdi; 5 verdi, 1 rosso
Partita 4: 1 verde, 3 rossi, 6 blu; 3 verdi, 6 rossi; 3 verdi, 15 blu, 14 rossi
Partita 5: 6 rossi, 1 blu, 3 verdi; 2 blu, 1 rosso, 2 verdi

Nella Partita 1, tre insiemi di cubi vengono rivelati dalla borsa (e poi rimessi). Il primo set è composto da 3 cubi blu e 4 cubi rossi; il secondo set è composto da 1 cubo rosso, 2 cubi verdi e 6 cubi blu; il terzo set è composto solo da 2 cubi verdi.

L'elfo vorrebbe innanzitutto sapere quali partite sarebbero state possibili se la borsa contenesse solo 12 cubi rossi, 13 cubi verdi e 14 cubi blu?

Nell'esempio sopra, le partite 1, 2 e 5 sarebbero state possibili se la borsa fosse stata caricata con quella configurazione. Tuttavia, la partita 3 sarebbe stata impossibile perché in un momento l'elfo ti ha mostrato 20 cubi rossi; allo stesso modo, la partita 4 sarebbe stata impossibile perché l'elfo ti ha mostrato 15 cubi blu in una volta sola. Se sommi gli ID delle partite che sarebbero state possibili, ottieni 8.

Determina quali partite sarebbero state possibili se la borsa fosse stata caricata solo con 12 cubi rossi, 13 cubi verdi e 14 cubi blu. Qual è la somma degli ID di quelle partite?

--- Parte Due ---

L'elfo dice che hanno smesso di produrre neve perché non stanno ricevendo acqua! Non è sicuro del motivo per cui l'acqua si è fermata; tuttavia, può mostrarti come arrivare alla fonte d'acqua per controllare di persona. È proprio qui vicino!

Mentre continui la tua passeggiata, l'elfo pone una seconda domanda: in ogni partita che hai giocato, qual è il numero minimo di cubi di ciascun colore che potevano essere nella borsa per rendere possibile la partita?

Considera nuovamente gli esempi di partite precedenti:

Partita 1: 3 blu, 4 rossi; 1 rosso, 2 verdi, 6 blu; 2 verdi
Partita 2: 1 blu, 2 verdi; 3 verdi, 4 blu, 1 rosso; 1 verde, 1 blu
Partita 3: 8 verdi, 6 blu, 20 rossi; 5 blu, 4 rossi, 13 verdi; 5 verdi, 1 rosso
Partita 4: 1 verde, 3 rossi, 6 blu; 3 verdi, 6 rossi; 3 verdi, 15 blu, 14 rossi
Partita 5: 6 rossi, 1 blu, 3 verdi; 2 blu, 1 rosso, 2 verdi

Nella partita 1, la partita avrebbe potuto essere giocata con almeno 4 cubi rossi, 2 verdi e 6 blu. Se anche solo un colore avesse avuto un cubo in meno, la partita sarebbe stata impossibile.
La partita 2 avrebbe potuto essere giocata con un minimo di 1 rosso, 3 verdi e 4 blu.
La partita 3 deve essere stata giocata con almeno 20 rossi, 13 verdi e 6 blu.
La partita 4 richiedeva almeno 14 rossi, 3 verdi e 15 blu.
La partita 5 aveva bisogno di non meno di 6 rossi, 3 verdi e 2 blu nella borsa.

La potenza di un insieme di cubi è uguale al prodotto dei numeri di cubi rossi, verdi e blu. La potenza dell'insieme minimo di cubi nella partita 1 è 48. Nelle partite 2-5 era rispettivamente 12, 1560, 630 e 36. Sommando queste cinque potenze si ottiene la somma 2286.

Per ogni partita, trova l'insieme minimo di cubi che doveva essere presente. Qual è la somma delle potenze di questi insiemi?