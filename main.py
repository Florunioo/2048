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


    def __init__(self, value: int, row: int, col: int) -> None:
        self.value = value
        self.row = row
        self.col = col
        self.x = col * TILE_WIDTH
        self.y = row * TILE_HEIGHT


    def get_color(self) -> tuple[int, int, int]:
        # Equasion to get the correct tile color for each score
        # If the tile value (score) is 2, the index is 0 (1st color)
        # If the tile value is 4, the index is 1 (2nd color), and so on
        color_index = int(math.log2(self.value)) - 1
        
        # get the color RGB value
        tile_color = self.TILE_COLORS[color_index]
        return tile_color


    def draw(self, window) -> None:
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


    def set_pos(self, ceil=False):
        if ceil:
            self.row = math.ceil(self.y / TILE_HEIGHT)
            self.col = math.ceil(self.x / TILE_WIDTH)
        else:
            self.row = math.floor(self.y / TILE_HEIGHT)
            self.col = math.floor(self.x / TILE_WIDTH)


    def move(self, delta) -> None:
        self.x += delta[0]
        self.y += delta[1]


def draw_grid(window) -> None:
    
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


def move_tiles(window, tiles, clock, direction):
    updated = True
    blocks = set()  # tell which tile has alredy merged in a single movement

    if direction == "left":
        sort_func = lambda x: x.col  # x.col is a dictionary key (the tiles are going left, so sort them by their column)
        reverse = False  # whether to sort in reverse or correct order
        delta = (-TILE_MOVE_SPEED, 0)  # -vel == move to the left
        boundary_check = lambda tile: tile.col == 0  # check if tile is max to the left
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col - 1}")  # return either "None" or the tile to the left
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + TILE_MOVE_SPEED  # check if both tiles are in the postion to merge
        move_check = lambda tile, next_tile: tile.x > next_tile.x + TILE_WIDTH + TILE_MOVE_SPEED  # stop moving if reached the border of the tile
        ceil = True  # round the numbers up or down when determining the location of the tile after a move
    elif direction == "right":
        sort_func = lambda x: x.col
        reverse = True 
        delta = (TILE_MOVE_SPEED, 0)
        boundary_check = lambda tile: tile.col == COLS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col + 1}")  
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - TILE_MOVE_SPEED  
        move_check = lambda tile, next_tile: tile.x + TILE_WIDTH + TILE_MOVE_SPEED < next_tile.x
        ceil = False
    elif direction == "up":
        sort_func = lambda x: x.row
        reverse = False
        delta = (0, -TILE_MOVE_SPEED)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row - 1}{tile.col}")  
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + TILE_MOVE_SPEED  
        move_check = lambda tile, next_tile: tile.y > next_tile.y + TILE_HEIGHT + TILE_MOVE_SPEED  
        ceil = True
    elif direction == "down":
        sort_func = lambda x: x.row
        reverse = True
        delta = (0, TILE_MOVE_SPEED)
        boundary_check = lambda tile: tile.row == ROWS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row + 1}{tile.col}")  
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - TILE_MOVE_SPEED  
        move_check = lambda tile, next_tile: tile.y + TILE_HEIGHT + TILE_MOVE_SPEED < next_tile.y
        ceil = False

    while updated:
        clock.tick(FPS)
        updated = False
        sorted_tiles = sorted(tiles.values(), key=sort_func, reverse=reverse)

        for idx, tile in enumerate(sorted_tiles):
            if boundary_check(tile):
                continue

            next_tile = get_next_tile(tile)  # get the next tile
            if not next_tile:  # if no next tile
                tile.move(delta)  # move initial tile
            elif (tile.value == next_tile.value # if there is next_tile
             and tile not in blocks # it's value is the same as the initial tile's value
             and next_tile not in blocks):
                if merge_check(tile, next_tile): # initiate merging tiles
                    tile.move(delta)
                else:
                    next_tile.value *= 2
                    sorted_tiles.pop(idx)
                    blocks.add(next_tile) # add to the set (only allows)
            elif move_check(tile, next_tile): # move the tile until reached the next tile's border
                tile.move(delta) # move until (elif statment is) False
            else: # none of the above are true
                continue  # no update occured (don't do anything)
            
            tile.set_pos(ceil)
            updated = True 

        update_tiles(window, tiles, sorted_tiles)

    end_move(tiles)

def end_move(tiles): # check if the game is over + last clean-up operation
    if len(tiles) == 16:
        return "lost"
    
    row, col = get_random_pos(tiles)
    tiles[f"{row}{col}"] = Tile(random.choice([2, 4]), row, col)



def update_tiles(window, tiles, sorted_tiles):
    tiles.clear() # clear the dictionary
    for tile in sorted_tiles:
        tiles[f"{tile.row}{tile.col}"] = tile

    draw(window, tiles)


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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        move_tiles(window, tiles, clock, "left")
                    elif event.key == pygame.K_RIGHT:
                        move_tiles(window, tiles, clock, "right")
                    elif event.key == pygame.K_UP:
                        move_tiles(window, tiles, clock, "up")
                    elif event.key == pygame.K_DOWN:
                        move_tiles(window, tiles, clock, "down")

        draw(window, tiles)

    pygame.quit()  # exit the game window


# run the game
if __name__ == "__main__":
    main(WINDOW)
