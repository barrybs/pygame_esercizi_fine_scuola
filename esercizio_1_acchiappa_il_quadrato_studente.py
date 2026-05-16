import random

import pygame


LARGHEZZA = 800
ALTEZZA = 600
FPS = 60
DURATA_PARTITA = 30

DIMENSIONE_BERSAGLIO = 60

BIANCO = (245, 245, 245)
NERO = (30, 30, 30)
ROSSO = (220, 60, 60)
BLU = (70, 130, 220)


def crea_bersaglio():
    """Restituisce un rettangolo che rappresenta il bersaglio."""
    # TODO 1:
    # Scegli x e y casuali in modo che il quadrato resti dentro la finestra.
    # Suggerimento:
    # x = random.randint(0, LARGHEZZA - DIMENSIONE_BERSAGLIO)
    # y = random.randint(0, ALTEZZA - DIMENSIONE_BERSAGLIO)
    x = 350
    y = 250
    return pygame.Rect(x, y, DIMENSIONE_BERSAGLIO, DIMENSIONE_BERSAGLIO)


def disegna_testo(superficie, testo, x, y, font, colore=NERO):
    immagine = font.render(testo, True, colore)
    superficie.blit(immagine, (x, y))


def mostra_schermata_finale(schermo, font_grande, font, punteggio):
    schermo.fill(BIANCO)
    titolo = font_grande.render("Tempo scaduto!", True, NERO)
    risultato = font.render(f"Punteggio finale: {punteggio}", True, BLU)
    suggerimento = font.render("Premi ESC o chiudi la finestra", True, NERO)

    schermo.blit(titolo, titolo.get_rect(center=(LARGHEZZA // 2, 230)))
    schermo.blit(risultato, risultato.get_rect(center=(LARGHEZZA // 2, 300)))
    schermo.blit(suggerimento, suggerimento.get_rect(center=(LARGHEZZA // 2, 360)))
    pygame.display.flip()


def main():
    pygame.init()
    schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
    pygame.display.set_caption("Esercizio 1 - Acchiappa il quadrato")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    font_grande = pygame.font.SysFont(None, 64)

    bersaglio = crea_bersaglio()
    punteggio = 0
    inizio = pygame.time.get_ticks()
    partita_attiva = True
    running = True

    while running:
        clock.tick(FPS)

        secondi_passati = (pygame.time.get_ticks() - inizio) // 1000
        tempo_rimasto = max(0, DURATA_PARTITA - secondi_passati)
        if tempo_rimasto == 0:
            partita_attiva = False

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                running = False
            elif partita_attiva and evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1 and bersaglio.collidepoint(evento.pos):
                    # TODO 2:
                    # Aumenta il punteggio di 1.
                    pass

                    # TODO 3:
                    # Sposta il bersaglio creando un nuovo rettangolo.
                    pass

        if partita_attiva:
            schermo.fill(BIANCO)
            pygame.draw.rect(schermo, ROSSO, bersaglio, border_radius=8)

            # TODO 4:
            # Mostra sullo schermo il punteggio e il tempo rimasto.
            # Suggerimento:
            # disegna_testo(schermo, f"Punti: {punteggio}", 20, 20, font)

            pygame.display.flip()
        else:
            mostra_schermata_finale(schermo, font_grande, font, punteggio)

    pygame.quit()


if __name__ == "__main__":
    main()

