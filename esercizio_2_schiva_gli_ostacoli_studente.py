import random

import pygame


LARGHEZZA = 800
ALTEZZA = 600
FPS = 60

LARGHEZZA_GIOCATORE = 70
ALTEZZA_GIOCATORE = 25

# TODO STUDENTE 1:
# Cambia la velocita del giocatore. Prova 5, 8 oppure 10.
VELOCITA_GIOCATORE = 7

# TODO STUDENTE 2:
# Cambia il numero di vite iniziali.
VITE_INIZIALI = 3

LARGHEZZA_OSTACOLO = 60
ALTEZZA_OSTACOLO = 35
VELOCITA_OSTACOLO = 5
TEMPO_NUOVO_OSTACOLO = 800

# TODO STUDENTE 3:
# Cambia quanti punti vale ogni ostacolo evitato.
PUNTI_PER_OSTACOLO = 1

# TODO STUDENTE 4:
# Cambia da quale punteggio parte il livello 2.
SOGLIA_LIVELLO_2 = 10

# TODO STUDENTE 5:
# Cambia il messaggio del livello 2.
MESSAGGIO_LIVELLO_2 = "Livello 2!"

BIANCO = (245, 245, 245)
NERO = (30, 30, 30)
VERDE = (70, 170, 95)
ROSSO = (220, 60, 60)
BLU = (70, 130, 220)
VIOLA = (130, 85, 190)


def crea_ostacolo():
    x = random.randint(0, LARGHEZZA - LARGHEZZA_OSTACOLO)
    y = -ALTEZZA_OSTACOLO
    return pygame.Rect(x, y, LARGHEZZA_OSTACOLO, ALTEZZA_OSTACOLO)


def disegna_testo(superficie, testo, x, y, font, colore=NERO):
    immagine = font.render(testo, True, colore)
    superficie.blit(immagine, (x, y))


def main():
    pygame.init()
    schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
    pygame.display.set_caption("Esercizio 2 - Schiva gli ostacoli")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    font_grande = pygame.font.SysFont(None, 64)

    giocatore = pygame.Rect(
        LARGHEZZA // 2 - LARGHEZZA_GIOCATORE // 2,
        ALTEZZA - 60,
        LARGHEZZA_GIOCATORE,
        ALTEZZA_GIOCATORE,
    )
    ostacoli = []
    punteggio = 0
    vite = VITE_INIZIALI
    ultimo_ostacolo = pygame.time.get_ticks()
    game_over = False
    running = True

    while running:
        clock.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                running = False

        if not game_over:
            tasti = pygame.key.get_pressed()
            if tasti[pygame.K_LEFT] or tasti[pygame.K_a]:
                giocatore.x -= VELOCITA_GIOCATORE
            elif tasti[pygame.K_RIGHT] or tasti[pygame.K_d]:
                giocatore.x += VELOCITA_GIOCATORE

            if giocatore.left < 0:
                giocatore.left = 0
            elif giocatore.right > LARGHEZZA:
                giocatore.right = LARGHEZZA

            ora = pygame.time.get_ticks()
            if ora - ultimo_ostacolo > TEMPO_NUOVO_OSTACOLO:
                ostacoli.append(crea_ostacolo())
                ultimo_ostacolo = ora

            velocita_attuale = VELOCITA_OSTACOLO
            if punteggio >= SOGLIA_LIVELLO_2:
                velocita_attuale += 2

            for ostacolo in ostacoli[:]:
                ostacolo.y += velocita_attuale

                if ostacolo.colliderect(giocatore):
                    ostacoli.remove(ostacolo)
                    vite -= 1
                    if vite == 0:
                        game_over = True

                elif ostacolo.top > ALTEZZA:
                    ostacoli.remove(ostacolo)
                    punteggio += PUNTI_PER_OSTACOLO

        schermo.fill(BIANCO)

        pygame.draw.rect(schermo, VERDE, giocatore, border_radius=8)
        for ostacolo in ostacoli:
            pygame.draw.rect(schermo, ROSSO, ostacolo, border_radius=8)

        disegna_testo(schermo, f"Punti: {punteggio}", 20, 20, font)
        disegna_testo(schermo, f"Vite: {vite}", 180, 20, font)

        if punteggio >= SOGLIA_LIVELLO_2 and not game_over:
            disegna_testo(schermo, MESSAGGIO_LIVELLO_2, 330, 20, font, VIOLA)

        if game_over:
            testo = font_grande.render("Game over", True, NERO)
            info = font.render("Premi ESC o chiudi la finestra", True, BLU)
            schermo.blit(testo, testo.get_rect(center=(LARGHEZZA // 2, 260)))
            schermo.blit(info, info.get_rect(center=(LARGHEZZA // 2, 330)))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
