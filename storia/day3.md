--- Giorno 3: Rapporti di Trasmissione ---

Tu e l'elfo raggiungete infine una stazione della funivia; dice che la funivia ti porterà fino alla fonte d'acqua, ma questo purtroppo questo è il punto più lontano dove ti puo accompagnare. Entri all interno della stazione.

Non ci vuole molto per trovare le cabine della funivia, ma sembra esserci un problema: non si stanno muovendo.

"Ah!"

Ti giri per vedere un elfo leggermente unto con una chiave inglese e un'espressione di sorpresa. "Scusa, non mi aspettavo nessuno! La funivia non sta funzionando in questo momento; ci vorrà ancora un po' prima che io possa sistemarla." Ti offri di aiutare.

L'ingegnere spiega che manca una componente del motore e nessuno riesce a capire quale sia. Se riesci a sommare tutti i numeri delle componenti nello schema del motore, dovrebbe essere facile capire quale componente manca.

Lo schema del motore (il tuo input del puzzle) consiste in una rappresentazione visiva del motore. Ci sono molti numeri e simboli che non capisci davvero, ma apparentemente ogni numero adiacente a un simbolo, anche diagonalmente, è un "numero di una componente" e dovrebbe essere incluso nella tua somma. (I punti (.) non contano come simboli.)

Ecco uno schema del motore di esempio:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In questo schema, due numeri NON sono numeri di una componente perché non sono adiacenti a un simbolo: 114 (in alto a destra) e 58 (in mezzo a destra). Ogni altro numero è adiacente a un simbolo e quindi è un numero di una componente; la loro somma è 4361.

Naturalmente, lo schema del motore effettivo è molto più grande. Qual è la somma di tutti i numeri di componenti nello schema del motore?

--- Parte Due ---

L'ingegnere trova la parte mancante e la installa nel motore! Mentre il motore prende vita, sali nella gondola della funivia più vicina, finalmente pronto ad ascendere alla fonte d'acqua.

Tuttavia, sembra che tu non stia andando molto veloce. Forse c'è ancora qualcosa che non va? Fortunatamente, la gondola ha un telefono con l'etichetta "aiuto", quindi lo prendi e l'ingegnere risponde.

Prima che tu possa spiegare la situazione, lei suggerisce di guardare fuori dalla finestra. Davanti alla finestra vedi l'ingegnere, che tiene un telefono in una mano e saluta con l'altra. Stai procedendo così lentamente che non hai nemmeno lasciato la stazione. Esci dalla gondola.

La parte mancante non era l'unico problema: uno degli ingranaggi nel motore è sbagliato. Un ingranaggio è qualsiasi simbolo * che è adiacente esattamente a due numeri. Il suo rapporto di trasmissione è il risultato della moltiplicazione di questi due numeri.

Questa volta, devi trovare il rapporto di trasmissione di ogni ingranaggio e sommarli tutti in modo che l'ingegnere possa capire quale ingranaggio deve essere sostituito.

Considera di nuovo lo schema del motore:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..


In questo schema, ci sono due ingranaggi. Il primo è in alto a sinistra; ha i numeri 467 e 35, quindi il suo rapporto di trasmissione è 16345. Il secondo ingranaggio è in basso a destra; il suo rapporto di trasmissione è 451490. (Il * adiacente a 617 non è un ingranaggio perché è adiacente solo a un numero di parte.) Sommando tutti i rapporti di trasmissione si ottiene 467835.

Qual è la somma di tutti i rapporti di trasmissione nel tuo schema motore?