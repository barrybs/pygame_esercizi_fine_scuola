import pygame


LARGHEZZA = 800
ALTEZZA = 600
FPS = 60

LARGHEZZA_NAVE = 70
ALTEZZA_NAVE = 28

# TODO STUDENTE 1:
# Cambia la velocita della navicella. Prova 5, 8 oppure 10.
VELOCITA_NAVE = 7

LARGHEZZA_ALIENO = 46
ALTEZZA_ALIENO = 30

# TODO STUDENTE 2:
# Cambia il numero di righe o colonne di alieni.
RIGHE_ALIENI = 3
COLONNE_ALIENI = 6

SPAZIO_ALIENI = 18
VELOCITA_ALIENI = 2
SCATTO_IN_BASSO = 24

LARGHEZZA_PROIETTILE = 6
ALTEZZA_PROIETTILE = 16
VELOCITA_PROIETTILE = 9
TEMPO_TRA_SPARI = 350

# TODO STUDENTE 3:
# Cambia quanti punti vale ogni alieno colpito.
PUNTI_PER_ALIENO = 10

# TODO STUDENTE 4:
# Cambia soglia e messaggio bonus.
SOGLIA_BONUS = 80
MESSAGGIO_BONUS = "Bonus raggiunto!"

# TODO STUDENTE 5:
# Cambia i messaggi finali.
MESSAGGIO_VITTORIA = "Hai vinto!"
MESSAGGIO_SCONFITTA = "Game over"

BIANCO = (245, 245, 245)
NERO = (25, 25, 25)
BLU = (70, 130, 220)
VERDE = (70, 175, 95)
ROSSO = (220, 60, 60)
VIOLA = (130, 85, 190)


def crea_alieni():
    alieni = []
    partenza_x = 120
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
                        proiettile = pygame.Rect(
                            nave.centerx - LARGHEZZA_PROIETTILE // 2,
                            nave.top - ALTEZZA_PROIETTILE,
                            LARGHEZZA_PROIETTILE,
                            ALTEZZA_PROIETTILE,
                        )
                        proiettili.append(proiettile)
                        ultimo_sparo = ora

        if stato == "gioco":
            tasti = pygame.key.get_pressed()
            if tasti[pygame.K_LEFT] or tasti[pygame.K_a]:
                nave.x -= VELOCITA_NAVE
            elif tasti[pygame.K_RIGHT] or tasti[pygame.K_d]:
                nave.x += VELOCITA_NAVE

            if nave.left < 0:
                nave.left = 0
            elif nave.right > LARGHEZZA:
                nave.right = LARGHEZZA

            for proiettile in proiettili[:]:
                proiettile.y -= VELOCITA_PROIETTILE
                if proiettile.bottom < 0:
                    proiettili.remove(proiettile)

            bordo_toccato = False
            for alieno in alieni:
                alieno.x += VELOCITA_ALIENI * direzione_alieni
                if alieno.left <= 0 or alieno.right >= LARGHEZZA:
                    bordo_toccato = True

            if bordo_toccato:
                direzione_alieni *= -1
                for alieno in alieni:
                    alieno.y += SCATTO_IN_BASSO

            for proiettile in proiettili[:]:
                for alieno in alieni[:]:
                    if proiettile.colliderect(alieno):
                        if proiettile in proiettili:
                            proiettili.remove(proiettile)
                        alieni.remove(alieno)
                        punteggio += PUNTI_PER_ALIENO
                        break

            if len(alieni) == 0:
                stato = "vittoria"
            else:
                alieno_arrivato = False
                for alieno in alieni:
                    if alieno.bottom >= nave.top:
                        alieno_arrivato = True

                if alieno_arrivato:
                    stato = "sconfitta"

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

        if punteggio >= SOGLIA_BONUS and stato == "gioco":
            disegna_testo(schermo, MESSAGGIO_BONUS, 270, 20, font, VERDE)

        if stato != "gioco":
            if stato == "vittoria":
                messaggio = MESSAGGIO_VITTORIA
                colore = VERDE
            else:
                messaggio = MESSAGGIO_SCONFITTA
                colore = ROSSO

            testo = font_grande.render(messaggio, True, colore)
            info = font.render("Premi ESC o chiudi la finestra", True, NERO)
            schermo.blit(testo, testo.get_rect(center=(LARGHEZZA // 2, 275)))
            schermo.blit(info, info.get_rect(center=(LARGHEZZA // 2, 340)))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
