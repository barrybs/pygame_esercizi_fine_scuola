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

