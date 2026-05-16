# Esercizi PyGame per gli ultimi giorni di scuola

Mini-giochi gia funzionanti, pensati per studenti che hanno lavorato su:

- variabili
- `print()` e f-string
- condizioni `if`, `if-else`, `elif`
- operatori di confronto
- operatori logici `and`, `or`
- cicli `for` e `while`
- contatori e punteggi

Le parti piu specifiche di PyGame sono gia pronte. Agli studenti vengono
richieste modifiche piccole e guidate: cambiare valori, messaggi, colori,
punteggi e semplici condizioni.

## Preparazione

Installare PyGame:

```bash
python3 -m pip install pygame
```

Eseguire un esercizio:

```bash
python3 esercizio_1_acchiappa_il_quadrato_studente.py
python3 esercizio_2_schiva_gli_ostacoli_studente.py
python3 esercizio_3_difesa_spaziale_studente.py
```

Le soluzioni hanno nome `soluzione_*.py` e sono escluse da Git tramite
`.gitignore`.

## Esercizio 1: Acchiappa il quadrato

Obiettivo del gioco: cliccare il quadrato prima che finisca il tempo.

File:

- `esercizio_1_acchiappa_il_quadrato_studente.py`
- `soluzione_1_acchiappa_il_quadrato.py`

Modifiche semplici richieste:

1. Cambiare la durata della partita.
2. Cambiare la dimensione del bersaglio.
3. Cambiare quanti punti vale un click corretto.
4. Decidere se togliere punti quando si clicca fuori.
5. Cambiare la soglia e il messaggio bonus.

Concetti della dispensa usati dagli studenti:

- assegnamento di variabili
- condizioni `if`
- confronto con `>=`
- f-string per mostrare il punteggio

## Esercizio 2: Schiva gli ostacoli

Obiettivo del gioco: muovere il giocatore a sinistra/destra e schivare i
blocchi che cadono dall'alto.

File:

- `esercizio_2_schiva_gli_ostacoli_studente.py`
- `soluzione_2_schiva_gli_ostacoli.py`

Modifiche semplici richieste:

1. Cambiare il numero di vite.
2. Cambiare la velocita del giocatore.
3. Cambiare quanti punti vale un ostacolo evitato.
4. Cambiare quando parte il livello 2.
5. Cambiare il messaggio mostrato nel livello 2.

Concetti della dispensa usati dagli studenti:

- variabili numeriche
- `if` con confronto `>=`
- contatori per punti e vite
- f-string per visualizzare valori

## Esercizio 3: Difesa spaziale

Obiettivo del gioco: muovere la navicella, sparare verso l'alto e colpire gli
alieni prima che arrivino in basso.

File:

- `esercizio_3_difesa_spaziale_studente.py`
- `soluzione_3_difesa_spaziale.py`

Modifiche semplici richieste:

1. Cambiare il numero di righe o colonne di alieni.
2. Cambiare la velocita della navicella.
3. Cambiare i punti ottenuti per ogni alieno colpito.
4. Cambiare la soglia del messaggio bonus.
5. Cambiare i messaggi di vittoria e sconfitta.

Concetti della dispensa usati dagli studenti:

- variabili
- `if`, `else`
- confronti tra numeri
- cicli `for` gia preparati nel codice
- punteggio come contatore

## Nota per la classe

Le righe segnate con `TODO STUDENTE` sono quelle su cui lavorare. Le altre
parti possono essere considerate codice gia fornito dal docente.
