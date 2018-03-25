from PIL import Image, ImageDraw

state = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
         ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
         ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
         ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']]

greenC = (127, 255, 0)
whiteC = (255, 255, 255)
blueC = (0, 0, 255)
yellowC = (255, 255, 0)
orangeC = (255, 127, 0)
redC = (255, 0, 0)
grayC = (127, 127, 127)
blackC = (0, 0, 0)

size_of_tile = 50


def draw_init(size_of_tile):
    """Przygotowanie plotna"""
    img = Image.new('RGB', (size_of_tile * 12, size_of_tile * 9), grayC)
    return img


def draw_tile(img, coord, color, size_of_tile):
    """coord to gorny lewy rog"""
    draw = ImageDraw.Draw(img)
    xy = (coord, (coord[0] + size_of_tile, coord[1] + size_of_tile))
    draw.rectangle(xy, fill=color, outline=blackC)
    return img


def draw_state(size_of_tile, state):
    """rysowanie"""
    white_coord = [(3 * size_of_tile, 3 * size_of_tile), (4 * size_of_tile, 3 * size_of_tile), (5 * size_of_tile, 3 * size_of_tile),
                   (3 * size_of_tile, 4 * size_of_tile), (4 * size_of_tile, 4 * size_of_tile), (5 * size_of_tile, 4 * size_of_tile),
                   (3 * size_of_tile, 5 * size_of_tile), (4 * size_of_tile, 5 * size_of_tile), (5 * size_of_tile, 5 * size_of_tile)]

    green_coord = [(0 * size_of_tile, 3 * size_of_tile), (1 * size_of_tile, 3 * size_of_tile), (2 * size_of_tile, 3 * size_of_tile),
                   (0 * size_of_tile, 4 * size_of_tile), (1 * size_of_tile, 4 * size_of_tile), (2 * size_of_tile, 4 * size_of_tile),
                   (0 * size_of_tile, 5 * size_of_tile), (1 * size_of_tile, 5 * size_of_tile), (2 * size_of_tile, 5 * size_of_tile)]

    orange_coord = [(3 * size_of_tile, 0 * size_of_tile), (4 * size_of_tile, 0 * size_of_tile), (5 * size_of_tile, 0 * size_of_tile),
                    (3 * size_of_tile, 1 * size_of_tile), (4 * size_of_tile, 1 * size_of_tile), (5 * size_of_tile, 1 * size_of_tile),
                    (3 * size_of_tile, 2 * size_of_tile), (4 * size_of_tile, 2 * size_of_tile), (5 * size_of_tile, 2 * size_of_tile)]

    red_coord = [(3 * size_of_tile, 6 * size_of_tile), (4 * size_of_tile, 6 * size_of_tile), (5 * size_of_tile, 6 * size_of_tile),
                 (3 * size_of_tile, 7 * size_of_tile), (4 * size_of_tile, 7 * size_of_tile), (5 * size_of_tile, 7 * size_of_tile),
                 (3 * size_of_tile, 8 * size_of_tile), (4 * size_of_tile, 8 * size_of_tile), (5 * size_of_tile, 8 * size_of_tile)]

    blue_coord = [(6 * size_of_tile, 3 * size_of_tile), (7 * size_of_tile, 3 * size_of_tile), (8 * size_of_tile, 3 * size_of_tile),
                  (6 * size_of_tile, 4 * size_of_tile), (7 * size_of_tile, 4 * size_of_tile), (8 * size_of_tile, 4 * size_of_tile),
                  (6 * size_of_tile, 5 * size_of_tile), (7 * size_of_tile, 5 * size_of_tile), (8 * size_of_tile, 5 * size_of_tile)]

    yellow_coord = [(9 * size_of_tile, 3 * size_of_tile), (10 * size_of_tile, 3 * size_of_tile), (11 * size_of_tile, 3 * size_of_tile),
                    (9 * size_of_tile, 4 * size_of_tile), (10 * size_of_tile, 4 * size_of_tile), (11 * size_of_tile, 4 * size_of_tile),
                    (9 * size_of_tile, 5 * size_of_tile), (10 * size_of_tile, 5 * size_of_tile), (11 * size_of_tile, 5 * size_of_tile)]

    all_coord = [white_coord, green_coord, orange_coord, red_coord, blue_coord, yellow_coord]

    img = draw_init(size_of_tile)
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 'W':
                draw_tile(img, all_coord[i][j], whiteC, size_of_tile)
            elif state[i][j] == 'G':
                draw_tile(img, all_coord[i][j], greenC, size_of_tile)
            elif state[i][j] == 'O':
                draw_tile(img, all_coord[i][j], orangeC, size_of_tile)
            elif state[i][j] == 'R':
                draw_tile(img, all_coord[i][j], redC, size_of_tile)
            elif state[i][j] == 'B':
                draw_tile(img, all_coord[i][j], blueC, size_of_tile)
            elif state[i][j] == 'Y':
                draw_tile(img, all_coord[i][j], yellowC, size_of_tile)

    return img

test = draw_state(size_of_tile, state)
test.show()