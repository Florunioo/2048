import pygame
import random
import math


# initialize pygame
pygame.init()


# constants
FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 4, 4

TILE_HEIGHT = HEIGHT // ROWS
TILE_WIDTH = WIDTH // COLS
TILE_MOVE_SPEED = 20

OUTLINE_THICKNESS = 10
OUTLINE_COLOR = (187, 173, 160)

BG_COLOR = (205, 192, 180)
TEXT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


def draw_grid(window):
    
    # draw horizontal gird lines
    for row in range(1, ROWS):
        y = row * TILE_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

    # draw vertical gird lines
    for col in range(1, COLS):
        x = col * TILE_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    # draw an outline around the screen
    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)


def draw(window):
    window.fill(BG_COLOR)  # set background color
    
    draw_grid(window)

    pygame.display.update()
     

# game loop
def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)  # run at the set FPS

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

        draw(window)

    pygame.quit()  # exit the game window


# run the game
if __name__ == "__main__":
    main(WINDOW)
