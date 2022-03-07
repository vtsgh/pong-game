import pygame
import sys
import random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        ball_restart()
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        ball_restart()
        opponent_score += 1
        score_time =pygame.time.get_ticks()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    global ball_speed_x, ball_speed_y

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)
    score_time = 2100


    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0
    else:
       ball_speed_y = 7 * random.choice((1, -1))
       ball_speed_x = 7 * random.choice((1, -1))
       score_time = None

# general set up
pygame.init()
clock = pygame.time.Clock()

# display window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('pong')

# game rectangles
ball = pygame.Rect(630, 430, 20, 20)
player = pygame.Rect(1270, 400, 10, 100)
opponent = pygame.Rect(0, 400, 10, 100)

# colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# game variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 10

# text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 32)

# score timer
score_time = None


# player inputs
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 10
            if event.key == pygame.K_UP:
                player_speed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 10
            if event.key == pygame.K_UP:
                player_speed += 10

    #game logic
    ball_animation()
    player_animation()
    opponent_ai()

    # visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    if score_time:
        ball_restart()

    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (650, 450))

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(player_text, (615, 450))

    # updating window
    pygame.display.flip()
    clock.tick(60)

