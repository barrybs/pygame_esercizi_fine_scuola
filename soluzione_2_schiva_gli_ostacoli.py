import random

import pygame


LARGHEZZA = 800
ALTEZZA = 600
FPS = 60

LARGHEZZA_GIOCATORE = 70
ALTEZZA_GIOCATORE = 25
VELOCITA_GIOCATORE = 7

LARGHEZZA_OSTACOLO = 60
ALTEZZA_OSTACOLO = 35
VELOCITA_OSTACOLO = 5
TEMPO_NUOVO_OSTACOLO = 800

BIANCO = (245, 245, 245)
NERO = (30, 30, 30)
VERDE = (70, 170, 95)
ROSSO = (220, 60, 60)
BLU = (70, 130, 220)


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
    pygame.display.set_caption("Schiva gli ostacoli")
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
            if tasti[pygame.K_RIGHT] or tasti[pygame.K_d]:
                giocatore.x += VELOCITA_GIOCATORE
            giocatore.x = max(0, min(giocatore.x, LARGHEZZA - giocatore.width))

            ora = pygame.time.get_ticks()
            if ora - ultimo_ostacolo > TEMPO_NUOVO_OSTACOLO:
                ostacoli.append(crea_ostacolo())
                ultimo_ostacolo = ora

            velocita_attuale = VELOCITA_OSTACOLO + punteggio // 10

            for ostacolo in ostacoli[:]:
                ostacolo.y += velocita_attuale

                if ostacolo.colliderect(giocatore):
                    game_over = True

                if ostacolo.top > ALTEZZA:
                    ostacoli.remove(ostacolo)
                    punteggio += 1

        schermo.fill(BIANCO)

        pygame.draw.rect(schermo, VERDE, giocatore, border_radius=8)
        for ostacolo in ostacoli:
            pygame.draw.rect(schermo, ROSSO, ostacolo, border_radius=8)

        disegna_testo(schermo, f"Punti: {punteggio}", 20, 20, font)

        if game_over:
            testo = font_grande.render("Game over", True, NERO)
            info = font.render("Premi ESC o chiudi la finestra", True, BLU)
            schermo.blit(testo, testo.get_rect(center=(LARGHEZZA // 2, 260)))
            schermo.blit(info, info.get_rect(center=(LARGHEZZA // 2, 330)))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

