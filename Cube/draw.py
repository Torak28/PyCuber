from PIL import Image, ImageDraw, ImageFont


class CubeDraw:
    greenC = (127, 255, 0)
    whiteC = (255, 255, 255)
    blueC = (0, 0, 255)
    yellowC = (255, 255, 0)
    orangeC = (255, 127, 0)
    redC = (255, 0, 0)
    grayC = (127, 127, 127)
    blackC = (0, 0, 0)

    img = None

    def __init__(self, size_of_tile=None):
        if size_of_tile is None:
            size_of_tile = 50
        self.size_of_tile = size_of_tile

    def draw_init(self):
        """Przygotowanie plotna - dobranie odpowiednich rozmiarow"""
        self.img = Image.new('RGB', (self.size_of_tile * 12, self.size_of_tile * 9), self.grayC)
        return self.img

    def draw_tile(self, img, coord, color):
        """Wyrysowanie pojedynczej plytki - coord to gorny lewy rog"""
        draw = ImageDraw.Draw(img)
        xy = (coord, (coord[0] + self.size_of_tile, coord[1] + self.size_of_tile))
        draw.rectangle(xy, fill=color, outline=self.blackC)
        return img

    def draw_sign(self, img):
        """Podpisanie  rysunku"""
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", size=15)
        draw.text((460, 425), "PyCube by Torak28", font=font)
        return img

    def draw_state(self, state):
        """Rysowanie calej kostki"""
        white_coord = [(3 * self.size_of_tile, 3 * self.size_of_tile), (4 * self.size_of_tile, 3 * self.size_of_tile), (5 * self.size_of_tile, 3 * self.size_of_tile),
                       (3 * self.size_of_tile, 4 * self.size_of_tile), (4 * self.size_of_tile, 4 * self.size_of_tile), (5 * self.size_of_tile, 4 * self.size_of_tile),
                       (3 * self.size_of_tile, 5 * self.size_of_tile), (4 * self.size_of_tile, 5 * self.size_of_tile), (5 * self.size_of_tile, 5 * self.size_of_tile)]

        green_coord = [(0 * self.size_of_tile, 3 * self.size_of_tile), (1 * self.size_of_tile, 3 * self.size_of_tile), (2 * self.size_of_tile, 3 * self.size_of_tile),
                       (0 * self.size_of_tile, 4 * self.size_of_tile), (1 * self.size_of_tile, 4 * self.size_of_tile), (2 * self.size_of_tile, 4 * self.size_of_tile),
                       (0 * self.size_of_tile, 5 * self.size_of_tile), (1 * self.size_of_tile, 5 * self.size_of_tile), (2 * self.size_of_tile, 5 * self.size_of_tile)]

        orange_coord = [(3 * self.size_of_tile, 0 * self.size_of_tile), (4 * self.size_of_tile, 0 * self.size_of_tile), (5 * self.size_of_tile, 0 * self.size_of_tile),
                        (3 * self.size_of_tile, 1 * self.size_of_tile), (4 * self.size_of_tile, 1 * self.size_of_tile), (5 * self.size_of_tile, 1 * self.size_of_tile),
                        (3 * self.size_of_tile, 2 * self.size_of_tile), (4 * self.size_of_tile, 2 * self.size_of_tile), (5 * self.size_of_tile, 2 * self.size_of_tile)]

        red_coord = [(3 * self.size_of_tile, 6 * self.size_of_tile), (4 * self.size_of_tile, 6 * self.size_of_tile), (5 * self.size_of_tile, 6 * self.size_of_tile),
                     (3 * self.size_of_tile, 7 * self.size_of_tile), (4 * self.size_of_tile, 7 * self.size_of_tile), (5 * self.size_of_tile, 7 * self.size_of_tile),
                     (3 * self.size_of_tile, 8 * self.size_of_tile), (4 * self.size_of_tile, 8 * self.size_of_tile), (5 * self.size_of_tile, 8 * self.size_of_tile)]

        blue_coord = [(6 * self.size_of_tile, 3 * self.size_of_tile), (7 * self.size_of_tile, 3 * self.size_of_tile), (8 * self.size_of_tile, 3 * self.size_of_tile),
                      (6 * self.size_of_tile, 4 * self.size_of_tile), (7 * self.size_of_tile, 4 * self.size_of_tile), (8 * self.size_of_tile, 4 * self.size_of_tile),
                      (6 * self.size_of_tile, 5 * self.size_of_tile), (7 * self.size_of_tile, 5 * self.size_of_tile), (8 * self.size_of_tile, 5 * self.size_of_tile)]

        yellow_coord = [(9 * self.size_of_tile, 3 * self.size_of_tile), (10 * self.size_of_tile, 3 * self.size_of_tile), (11 * self.size_of_tile, 3 * self.size_of_tile),
                        (9 * self.size_of_tile, 4 * self.size_of_tile), (10 * self.size_of_tile, 4 * self.size_of_tile), (11 * self.size_of_tile, 4 * self.size_of_tile),
                        (9 * self.size_of_tile, 5 * self.size_of_tile), (10 * self.size_of_tile, 5 * self.size_of_tile), (11 * self.size_of_tile, 5 * self.size_of_tile)]

        all_coord = [white_coord, green_coord, orange_coord, red_coord, blue_coord, yellow_coord]

        self.img = self.draw_init()
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 'W':
                    self.draw_tile(self.img, all_coord[i][j], self.whiteC)
                elif state[i][j] == 'G':
                    self.draw_tile(self.img, all_coord[i][j], self.greenC)
                elif state[i][j] == 'O':
                    self.draw_tile(self.img, all_coord[i][j], self.orangeC)
                elif state[i][j] == 'R':
                    self.draw_tile(self.img, all_coord[i][j], self.redC)
                elif state[i][j] == 'B':
                    self.draw_tile(self.img, all_coord[i][j], self.blueC)
                elif state[i][j] == 'Y':
                    self.draw_tile(self.img, all_coord[i][j], self.yellowC)

        return self.draw_sign(self.img)
