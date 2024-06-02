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
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


class Tile:
    TILE_COLORS = [
        (237, 229, 218),  # 2
        (238, 225, 201),  # 4
        (243, 178, 122),  # 8
        (246, 150, 101),  # 16
        (247, 124, 95),   # 32
        (250, 128, 114),  # 64
        (255, 219, 88),   # 128 
        (253, 218, 13),   # 256
        (255, 210, 0),    # 512
        (175, 225, 175),  # 1,024
        (114, 204, 114),  # 2,048
        (65, 170, 90),    # 4,096
        (173, 216, 230),  # 8,192
        (120, 179, 227),  # 16,384
        (89, 140, 235),   # 32,768
        (204, 181, 230),  # 65,536
        (187, 149, 215),  # 131,072
        (123, 77, 141),   # 262,144
        (52, 52, 52),     # 524,288
        (26, 26, 26),     # 1,048,576
        (0, 0, 0),        # 2,097,152
    ]


    def __init__(self, value: int, row: int, col: int):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * TILE_WIDTH
        self.y = row * TILE_HEIGHT


    def get_color(self):
        # Equasion to get the correct tile color for each score
        # If the tile value (score) is 2, the index is 0 (1st color)
        # If the tile value is 4, the index is 1 (2nd color), and so on
        color_index = int(math.log2(self.value)) - 1
        
        # get the color RGB value
        tile_color = self.TILE_COLORS[color_index]
        return tile_color


    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, TILE_WIDTH, TILE_HEIGHT))
    
        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(
            text, 
            (
                self.x + (TILE_WIDTH / 2 - text.get_width() / 2),
                self.y + (TILE_HEIGHT / 2 - text.get_height() / 2),
            )
        )


    def set_pos(self):
        pass


    def move(self, delta):
        pass


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


def draw(window, tiles):
    window.fill(BG_COLOR)  # set background color

    for tile in tiles.values():
        tile.draw(window)
    
    draw_grid(window)

    pygame.display.update()
     

def get_random_pos(tiles):
    row, col = None, None

    while True:
        row = random.randrange(0, ROWS)
        col = random.randrange(0, COLS)

        if f"{row}{col}" not in tiles:
            break

    return row, col


def generate_tiles():
    tiles = {}
    for _ in range(2):
        row, col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Tile(2, row, col)

    return tiles

# game loop
def main(window):
    clock = pygame.time.Clock()
    run = True

    # locate the tiles very quicly by their "row" and "col"
    tiles = generate_tiles()


    while run:
        clock.tick(FPS)  # run at the set FPS

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

        draw(window, tiles)

    pygame.quit()  # exit the game window


# run the game
if __name__ == "__main__":
    main(WINDOW)
