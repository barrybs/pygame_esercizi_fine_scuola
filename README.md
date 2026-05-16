# Esercizi PyGame per gli ultimi giorni di scuola

Due mini-giochi pensati per studenti che conoscono variabili, condizioni,
cicli, liste e funzioni di base.

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

## Esercizio 1: Acchiappa il quadrato

Obiettivo: cliccare il quadrato prima che finisca il tempo.

File:

- `esercizio_1_acchiappa_il_quadrato_studente.py`
- `soluzione_1_acchiappa_il_quadrato.py`

Concetti usati:

- finestra PyGame
- `pygame.Rect`
- eventi del mouse
- collisione con `collidepoint`
- punteggio e timer

TODO principali per gli studenti:

1. Posizionare il quadrato in un punto casuale.
2. Aumentare il punteggio quando il giocatore clicca il quadrato.
3. Spostare il quadrato dopo ogni click corretto.
4. Mostrare punteggio e tempo rimasto.

Varianti facili:

- far diventare il quadrato piu piccolo ogni 5 punti
- togliere un punto se il giocatore clicca fuori
- cambiare colore al quadrato a ogni click

## Esercizio 2: Schiva gli ostacoli

Obiettivo: muovere il giocatore a sinistra/destra e schivare i blocchi che
cadono dall'alto.

File:

- `esercizio_2_schiva_gli_ostacoli_studente.py`
- `soluzione_2_schiva_gli_ostacoli.py`

Concetti usati:

- lettura della tastiera
- lista di ostacoli
- movimento di rettangoli
- collisione con `colliderect`
- difficolta crescente

TODO principali per gli studenti:

1. Muovere il giocatore con le frecce o con A/D.
2. Creare nuovi ostacoli a intervalli regolari.
3. Far cadere gli ostacoli.
4. Controllare la collisione tra giocatore e ostacoli.
5. Aumentare il punteggio quando un ostacolo esce dallo schermo.

Varianti facili:

- aggiungere vite invece di terminare subito
- aumentare la velocita ogni 10 punti
- aggiungere ostacoli di colore diverso con punteggi diversi

## Esercizio 3: Difesa spaziale

Obiettivo: muovere la navicella, sparare verso l'alto e colpire tutti gli
alieni prima che arrivino in basso.

File:

- `esercizio_3_difesa_spaziale_studente.py`
- `soluzione_3_difesa_spaziale.py`

Concetti usati:

- lettura della tastiera
- liste di proiettili e nemici
- movimento orizzontale di gruppo
- collisione con `colliderect`
- schermata di vittoria o game over

TODO principali per gli studenti:

1. Muovere la navicella a sinistra/destra.
2. Sparare un proiettile premendo SPAZIO.
3. Far salire i proiettili e rimuoverli quando escono dallo schermo.
4. Controllare le collisioni tra proiettili e alieni.
5. Far muovere gli alieni come gruppo.
6. Stabilire vittoria e sconfitta.

Varianti facili:

- dare 3 vite alla navicella
- aumentare la velocita degli alieni dopo ogni riga eliminata
- aggiungere un alieno speciale che vale piu punti
- limitare il numero massimo di proiettili sullo schermo
