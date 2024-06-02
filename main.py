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


def draw(window):
    window.fill(BG_COLOR)  # Set background color

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
