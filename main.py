import pygame
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()


def draw_x(x_pos, y_pos):
    pygame.draw.lines(background, dark_red, True, [(x_pos-50, y_pos-50), (x_pos+50, y_pos+50)], 15)
    pygame.draw.lines(background, dark_red, True, [(x_pos-50, y_pos+50), (x_pos+50, y_pos-50)], 15)


def draw_o(x_pos, y_pos):
    pygame.draw.circle(background, dark_red, [x_pos, y_pos], 55, 10)


def play_click():
    pygame.mixer.Sound.play(click)


screen_width = 1000
screen_height = 1000
add = 100
screen = screen_width, screen_height
pygame.display.set_caption("TikTakToe")

theme = pygame.mixer.Sound('Sounds/HOTRS.mp3')
click = pygame.mixer.Sound('Sounds/Click.mp3')
theme.set_volume(0.1)

rect = Rect(255 + add, add, 10, 800)
rect2 = Rect(527 + add, add, 10, 800)
rect3 = Rect(add, 255 + add, 800, 10)
rect4 = Rect(add, 527 + add, 800, 10)
background = pygame.display.set_mode((screen_width, screen_height))
background.fill((217, 217, 217))
dark_red = (62, 0, 0)
logo = pygame.image.load("Images/logo_for_hifhafhoe.png").convert_alpha()
match = pygame.image.load("Images/Match.png").convert_alpha()
quit_button = pygame.image.load("Images/Quit.png").convert_alpha()
font = pygame.font.Font('Fonts/Poppins-Bold.ttf', 100)


def play(player):

    pygame.mixer.Sound.play(theme)
    mouse_x, mouse_y = (0, 0)
    running = False
    x = player
    win = True
    tie = False
    load = True
    player_x_score = 0
    player_o_score = 0
    while load:
        count = 0
        background.fill((217, 217, 217))
        up = [0, 0, 0]
        cen = [0, 0, 0]
        down = [0, 0, 0]
        pos_list = [up, cen, down]
        background.blit(logo, (348, 59))
        background.blit(font.render('PLAYER X : '+str(player_x_score), True, dark_red), (201, 379))
        background.blit(font.render('PLAYER 0 : '+str(player_o_score), True, dark_red), (207, 500))
        background.blit(match, (338, 706))
        background.blit(quit_button, (338, 803))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                temp_x, temp_y = pygame.mouse.get_pos()
                if 338 < temp_x < 662 and 706 < temp_y < 786:
                    play_click()
                    running = True
                    background.fill((217, 217, 217))
                if 338 < temp_x < 662 and 803 < temp_y < 883:
                    play_click()
                    load = False
            if event.type == pygame.QUIT:
                load = False

        while running:
            pygame.draw.rect(background,  dark_red, rect)
            pygame.draw.rect(background, dark_red, rect2)
            pygame.draw.rect(background, dark_red, rect3)
            pygame.draw.rect(background, dark_red, rect4)
            pygame.display.update()
            print("------")
            print(up)
            print(cen)
            print(down)
            print("------")
            for i in range(3):
                if up[i] == cen[i] == down[i] != 0:
                    running = False
                    if up[i] == 1:
                        win = True
                        player_x_score += 1
                    else:
                        win = False
                        player_o_score += 1

            for i in pos_list:
                if i[0] == i[1] == i[2] != 0:
                    running = False
                    if i[0] == 1:
                        win = True
                        player_x_score += 1
                    else:
                        win = False
                        player_o_score += 1

            if up[0] == cen[1] == down[2] != 0:
                running = False
                if up[0] == 1:
                    win = True
                    player_x_score += 1
                else:
                    win = False
                    player_o_score += 1

            if up[2] == cen[1] == down[0] != 0:
                running = False
                if up[0] == 1:
                    win = True
                    player_x_score += 1
                else:
                    win = False
                    player_o_score += 1
            if count == 9:
                running = False
                tie = True

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    x = not x
                    if 0 + add < mouse_x < 800 + add and 0 + add < mouse_y < 800 + add:
                        count += 1
                        play_click()
                    if 0 + add < mouse_x < 255 + add and 0 + add < mouse_y < 255 + add and up[0] == 0:
                        if x:
                            draw_x(125 + add, 125 + add)
                            up[0] = 1
                        else:
                            draw_o(125 + add, 125 + add)
                            up[0] = 2
                    elif 265 + add < mouse_x < 527 + add and 0 + add < mouse_y < 255 + add and up[1] == 0:
                        if x:
                            draw_x(398 + add, 125 + add)
                            up[1] = 1
                        else:
                            draw_o(398 + add, 125 + add)
                            up[1] = 2
                    elif 527 + add < mouse_x < 790 + add and 0 + add < mouse_y < 255 + add and up[2] == 0:
                        if x:
                            draw_x(670 + add, 125 + add)
                            up[2] = 1
                        else:
                            draw_o(670 + add, 125 + add)
                            up[2] = 2
                    if 0 + add < mouse_x < 255 + add and 265 + add < mouse_y < 527 + add and cen[0] == 0:
                        if x:
                            draw_x(125 + add, 398 + add)
                            cen[0] = 1
                        else:
                            draw_o(125 + add, 398 + add)
                            cen[0] = 2
                    if 265 + add < mouse_x < 527 + add and 265 + add < mouse_y < 527 + add and cen[1] == 0:
                        if x:
                            draw_x(398 + add, 398 + add)
                            cen[1] = 1
                        else:
                            draw_o(398 + add, 398 + add)
                            cen[1] = 2
                    if 527 + add < mouse_x < 790 + add and 265 + add < mouse_y < 527 + add and cen[2] == 0:
                        if x:
                            draw_x(670 + add, 398 + add)
                            cen[2] = 1
                        else:
                            draw_o(670 + add, 398 + add)
                            cen[2] = 2
                    if 0 + add < mouse_x < 255 + add and 527 + add < mouse_y < 790 + add and down[0] == 0:
                        if x:
                            draw_x(125 + add, 670 + add)
                            down[0] = 1
                        else:
                            draw_o(125 + add, 670 + add)
                            down[0] = 2
                    if 255 + add < mouse_x < 527 + add and 527 + add < mouse_y < 790 + add and down[1] == 0:
                        if x:
                            draw_x(398 + add, 670 + add)
                            down[1] = 1
                        else:
                            draw_o(398 + add, 670 + add)
                            down[1] = 2
                    if 527 + add < mouse_x < 790 + add and 527 + add < mouse_y < 790 + add and down[2] == 0:
                        if x:
                            draw_x(670 + add, 670 + add)
                            down[2] = 1
                        else:
                            draw_o(670 + add, 670 + add)
                            down[2] = 2

                if event.type == pygame.QUIT:
                    running = False
                    load = False


def main():

    who_start = False
    play(who_start)


main()
