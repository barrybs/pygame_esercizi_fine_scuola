import pygame


LARGHEZZA = 800
ALTEZZA = 600
FPS = 60

LARGHEZZA_NAVE = 70
ALTEZZA_NAVE = 28
VELOCITA_NAVE = 7

LARGHEZZA_ALIENO = 46
ALTEZZA_ALIENO = 30
RIGHE_ALIENI = 3
COLONNE_ALIENI = 8
SPAZIO_ALIENI = 18
VELOCITA_ALIENI = 2
SCATTO_IN_BASSO = 24

LARGHEZZA_PROIETTILE = 6
ALTEZZA_PROIETTILE = 16
VELOCITA_PROIETTILE = 9
TEMPO_TRA_SPARI = 350

BIANCO = (245, 245, 245)
NERO = (25, 25, 25)
BLU = (70, 130, 220)
VERDE = (70, 175, 95)
ROSSO = (220, 60, 60)
VIOLA = (130, 85, 190)


def crea_alieni():
    alieni = []
    partenza_x = 90
    partenza_y = 70

    for riga in range(RIGHE_ALIENI):
        for colonna in range(COLONNE_ALIENI):
            x = partenza_x + colonna * (LARGHEZZA_ALIENO + SPAZIO_ALIENI)
            y = partenza_y + riga * (ALTEZZA_ALIENO + SPAZIO_ALIENI)
            alieni.append(pygame.Rect(x, y, LARGHEZZA_ALIENO, ALTEZZA_ALIENO))

    return alieni


def disegna_testo(superficie, testo, x, y, font, colore=NERO):
    immagine = font.render(testo, True, colore)
    superficie.blit(immagine, (x, y))


def disegna_nave(superficie, nave):
    punta = (nave.centerx, nave.top)
    sinistra = (nave.left, nave.bottom)
    destra = (nave.right, nave.bottom)
    pygame.draw.polygon(superficie, BLU, [punta, sinistra, destra])


def main():
    pygame.init()
    schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
    pygame.display.set_caption("Esercizio 3 - Difesa spaziale")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 34)
    font_grande = pygame.font.SysFont(None, 64)

    nave = pygame.Rect(
        LARGHEZZA // 2 - LARGHEZZA_NAVE // 2,
        ALTEZZA - 60,
        LARGHEZZA_NAVE,
        ALTEZZA_NAVE,
    )
    alieni = crea_alieni()
    proiettili = []
    direzione_alieni = 1
    ultimo_sparo = 0
    punteggio = 0
    stato = "gioco"
    running = True

    while running:
        clock.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                running = False
            elif stato == "gioco" and evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    ora = pygame.time.get_ticks()
                    if ora - ultimo_sparo > TEMPO_TRA_SPARI:
                        # TODO 2:
                        # Crea un rettangolo piccolo sopra la nave e aggiungilo
                        # alla lista proiettili.
                        # Suggerimento:
                        # proiettile = pygame.Rect(...)
                        # proiettili.append(proiettile)
                        ultimo_sparo = ora

        if stato == "gioco":
            tasti = pygame.key.get_pressed()

            # TODO 1:
            # Muovi la nave a sinistra con freccia sinistra o A.
            # Muovi la nave a destra con freccia destra o D.
            # Poi impedisci alla nave di uscire dalla finestra.

            for proiettile in proiettili[:]:
                # TODO 3:
                # Fai salire il proiettile.
                # Se esce dallo schermo, rimuovilo dalla lista.
                pass

            bordo_toccato = False
            for alieno in alieni:
                # TODO 5:
                # Sposta ogni alieno in orizzontale.
                # Se un alieno tocca il bordo sinistro o destro,
                # imposta bordo_toccato = True.
                pass

            if bordo_toccato:
                # TODO 5:
                # Cambia direzione agli alieni e falli scendere un po'.
                pass

            for proiettile in proiettili[:]:
                for alieno in alieni[:]:
                    # TODO 4:
                    # Se proiettile e alieno si toccano:
                    # - rimuovi il proiettile
                    # - rimuovi l'alieno
                    # - aumenta il punteggio
                    pass

            # TODO 6:
            # Se non ci sono piu alieni, stato diventa "vittoria".
            # Se un alieno arriva vicino alla nave, stato diventa "sconfitta".

        schermo.fill(BIANCO)

        disegna_nave(schermo, nave)

        for alieno in alieni:
            pygame.draw.rect(schermo, VERDE, alieno, border_radius=8)
            occhio = pygame.Rect(alieno.centerx - 5, alieno.centery - 5, 10, 10)
            pygame.draw.rect(schermo, NERO, occhio, border_radius=4)

        for proiettile in proiettili:
            pygame.draw.rect(schermo, ROSSO, proiettile, border_radius=3)

        disegna_testo(schermo, f"Punti: {punteggio}", 20, 20, font)
        disegna_testo(schermo, "ESC per uscire", 610, 20, font, VIOLA)

        if stato != "gioco":
            if stato == "vittoria":
                messaggio = "Hai vinto!"
                colore = VERDE
            else:
                messaggio = "Game over"
                colore = ROSSO

            testo = font_grande.render(messaggio, True, colore)
            info = font.render("Premi ESC o chiudi la finestra", True, NERO)
            schermo.blit(testo, testo.get_rect(center=(LARGHEZZA // 2, 275)))
            schermo.blit(info, info.get_rect(center=(LARGHEZZA // 2, 340)))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
