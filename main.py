import random

import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
TITLE_COLOR = (0, 128, 0)
BLUE = (0, 0, 255)
FPS = 60
TIMER = pygame.time.Clock()
TIMERCOUNT = pygame.time.Clock()

background_sound2 = pygame.mixer.Sound('./sons-musicas/a-blue-day-150.mp3')
notification_sound = pygame.mixer.Sound('./sons-musicas/game-notification.wav')
background_sound = pygame.mixer.music.load('./sons-musicas/a-blue-day-150.mp3')
winner_sound = pygame.mixer.Sound('./sons-musicas/winnermusic.wav')
pygame.mixer.music.play(-1)


rows = 6
cols = 8
correct = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]

rows2 = 4
cols2 = 4
correct2 = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

rows3 = 6
cols3 = 6
correct3 = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]


options_list = []
spaces = []
used = []
new_board = True
first_guess = False
second_guess = False
first_guess_num = 0
second_guess_num = 0
score = 0
best_score = 0
matches = 0
game_over = False

# Criando a tela
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Jogo da Memória')
title_font = pygame.font.Font('freesansbold.ttf', 56)
small_font = pygame.font.Font('freesansbold.ttf', 26)
smaller_font = pygame.font.Font('freesansbold.ttf', 14)

bg = pygame.image.load("fundo.jpg")


def generate_board():
    global options_list
    global spaces
    global used
    for item in range(rows3 * cols3 // 2):
        options_list.append(item)

    for item in range(rows3 * cols3):
        piece = options_list[random.randint(0, len(options_list) - 1)]
        spaces.append(piece)
        if piece in used:
            used.remove(piece)
            options_list.remove(piece)
        else:
            used.append(piece)


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


def draw_backgrounds(time):
    tempo = convert(time)
    top_menu = pygame.draw.rect(screen, BLACK, [0, 0, WIDTH, 100], 0)
    title_text = title_font.render('JOGO DA MEMORIA', True, TITLE_COLOR)
    screen.blit(title_text, (10, 20))
    title_timer = smaller_font.render(
        f'Tempo de jogo: {tempo}', True, TITLE_COLOR)
    screen.blit(title_timer, (420, 80))
    board_space = pygame.draw.rect(
        screen, GRAY, [0, 100, WIDTH, HEIGHT - 200], 0)
    screen.blit(bg, (0, 100))
    bottom_menu = pygame.draw.rect(
        screen, BLACK, [0, HEIGHT - 100, WIDTH, 100], 0)
    restart_button = pygame.draw.rect(
        screen, GRAY, [5, HEIGHT - 90, 130, 40], 0, 5)
    score_text = small_font.render(
        f'Movimentos realizados: {score}', True, WHITE)
    screen.blit(score_text, (250, 520))
    best_text = small_font.render(
        f'Melhor ponto: { best_score }', True, WHITE)
    screen.blit(best_text, (250, 560))
    restart_text = small_font.render('Reiniciar', True, WHITE)
    screen.blit(restart_text, (10, 520))

    return restart_button


def draw_board():
    global rows3
    global cols3
    global correct3

    board_list = []
    for i in range(cols3):
        for j in range(rows3):
            piece = pygame.draw.rect(
                screen, WHITE, [i * 75 + 82, j * 65 + 112, 50, 50], 0, 4)
            board_list.append(piece)
            piece_text = small_font.render(
                f'{spaces[i * rows3 + j]}', True, GRAY)
            screen.blit(piece_text, (i * 75 + 86, j * 65 + 120))

    for r in range(rows3):
        for c in range(cols3):
            if correct3[r][c] == 1:
                pygame.draw.rect(
                    screen, GREEN, [c * 75 + 82, r * 65 + 110, 54, 54], 3, 4)
                piece_text = small_font.render(
                    f'{spaces[c * rows3 + r]}', True, BLACK)
                screen.blit(piece_text, (c * 75 + 86, r * 65 + 120))

    return board_list


def check_guesses(first, second):
    global spaces
    global correct3
    global score
    global matches

    if spaces[first] == spaces[second]:
        col1 = first // rows3
        col2 = second // rows3
        row1 = first - (first // rows3 * rows3)
        row2 = second - (second // rows3 * rows3)
        if correct3[row1][col1] == 0 and correct3[row2][col2] == 0:
            notification_sound.play()
            correct3[row1][col1] = 1
            correct3[row2][col2] = 1
            score += 1
            matches += 1
            print(correct3)
    else:
        score += 1


running = True
starttime = pygame.time.get_ticks()
while running:
    TIMER.tick(FPS)
    seconds = (pygame.time.get_ticks() - starttime) / 100
    screen.fill(WHITE)
    if new_board:
        generate_board()
        print(spaces)
        new_board = False
    restart = draw_backgrounds(seconds)
    board = draw_board()

    if first_guess and second_guess:
        check_guesses(first_guess_num, second_guess_num)
        pygame.time.delay(1000)
        first_guess = False
        second_guess = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(board)):
                button = board[i]
                if not game_over:
                    if button.collidepoint(event.pos) and not first_guess:
                        first_guess = True
                        first_guess_num = i
                    if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                        second_guess = True
                        second_guess_num = i
            if restart.collidepoint(event.pos):
                options_list = []
                used = []
                spaces = []
                new_board = True
                score = 0
                matches = 0
                first_guess = False
                second_guess = False
                second_guess = False
                correct = [[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
                correct3 = [[0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]
                game_over = False
                seconds = 0
                starttime = pygame.time.get_ticks()

    if matches == rows3 * cols3 // 2:
        game_over = True
        winner = pygame.draw.rect(
            screen, GRAY, [10, HEIGHT - 300, WIDTH - 20, 80], 0, 5)
        winner_text = title_font.render(
            f'Você ganhou com {score} movimentos !', True, WHITE)
        screen.blit(winner_text, (10, HEIGHT - 290))
        winner_sound.play()

        if best_score > score or best_score == 0:
            best_score = score

    if first_guess:
        piece_text = small_font.render(
            f'{spaces[first_guess_num]}', True, BLUE)
        location = (first_guess_num // rows3 * 75 + 86,
                    (first_guess_num - (first_guess_num // rows3 * rows3)) * 65 + 120)
        screen.blit(piece_text, (location))

    if second_guess:
        piece_text = small_font.render(
            f'{spaces[second_guess_num]}', True, BLUE)
        location = (second_guess_num // rows3 * 75 + 86,
                    (second_guess_num - (second_guess_num // rows3 * rows3)) * 65 + 120)
        screen.blit(piece_text, (location))

    pygame.display.flip()

pygame.quit()
