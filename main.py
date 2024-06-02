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


class Tile:
    TILE_COLORS = [
        (237, 229, 218),  # 2 - Off White
        (238, 225, 201),  # 4 - Light Beige
        (243, 178, 122),  # 8 - Peach
        (246, 150, 101),  # 16 - Light Orange
        (247, 124, 95),   # 32 - Coral
        (247, 95, 59),    # 64 - Red-Orange
        (237, 208, 115),  # 128 - Light Yellow
        (237, 204, 99),   # 256 - Mustard Yellow
        (236, 202, 80),   # 512 - Goldenrod
        (153, 255, 153),  # 1,024 - Light Green
        (114, 204, 114),  # 2,048 - Green
        (57, 168, 57),    # 4,096 - Dark Green
        (173, 216, 230),  # 8,192 - Light Blue
        (0, 191, 255),    # 16,384 - Deep Sky Blue
        (0, 0, 255),      # 32,768 - Blue
        (75, 0, 130),     # 65,536 - Indigo
        (138, 43, 226),   # 131,072 - Violet
        (160, 32, 240),   # 262,144 - Purple
        (255, 20, 147),   # 524,288 - Deep Pink
        (255, 105, 180),  # 1,048,576 - Hot Pink
        (255, 0, 255),    # 2,097,152 - Magenta
        (148, 0, 211),    # 4,194,304 - Dark Violet
        (75, 0, 130),     # 8,388,608 - Indigo
        (43, 26, 64),     # 16,777,216 - Dark Indigo
        (18, 10, 37),     # 33,554,432 - Almost Black
        (0, 0, 0)         # 67,108,864 - Completely Black
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * TILE_WIDTH
        self.y = row * TILE_HEIGHT


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
