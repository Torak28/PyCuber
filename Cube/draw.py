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

    W = 'W'
    G = 'G'
    O = 'O'
    R = 'R'
    B = 'B'
    Y = 'Y'

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

    def draw_tile_debug(self, img, coord, color, number, face):
        """Wyrysowanie pojedynczej plytki - coord to gorny lewy rog"""
        print(coord, number, face)
        draw = ImageDraw.Draw(img)
        xy = (coord, (coord[0] + self.size_of_tile, coord[1] + self.size_of_tile))
        font = ImageFont.truetype("arial.ttf", size=20)
        draw.rectangle(xy, fill=color, outline=self.blackC)
        if face is 0:
            face = 'F'
        elif face is 1:
            face = 'D'
        elif face is 2:
            face = 'L'
        elif face is 3:
            face = 'R'
        elif face is 4:
            face = 'U'
        elif face is 5:
            face = 'B'
        if number is 4:
            number = face
        draw.text((coord[0] + self.size_of_tile//3, coord[1] + self.size_of_tile//3),
                  str(number), font=font, fill=self.blackC)
        return img

    @staticmethod
    def draw_sign(img):
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
                if state[i][j] is self.W:
                    self.draw_tile(self.img, all_coord[i][j], self.whiteC)
                elif state[i][j] is self.G:
                    self.draw_tile(self.img, all_coord[i][j], self.greenC)
                elif state[i][j] is self.O:
                    self.draw_tile(self.img, all_coord[i][j], self.orangeC)
                elif state[i][j] is self.R:
                    self.draw_tile(self.img, all_coord[i][j], self.redC)
                elif state[i][j] is self.B:
                    self.draw_tile(self.img, all_coord[i][j], self.blueC)
                elif state[i][j] is self.Y:
                    self.draw_tile(self.img, all_coord[i][j], self.yellowC)

        return self.draw_sign(self.img)

    def draw_state_debug(self, state):
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
                if state[i][j] is self.W:
                    self.draw_tile_debug(self.img, all_coord[i][j], self.whiteC, j, i)
                elif state[i][j] is self.G:
                    self.draw_tile_debug(self.img, all_coord[i][j], self.greenC, j, i)
                elif state[i][j] is self.O:
                    self.draw_tile_debug(self.img, all_coord[i][j], self.orangeC, j, i)
                elif state[i][j] is self.R:
                    self.draw_tile_debug(self.img, all_coord[i][j], self.redC, j, i)
                elif state[i][j] is self.B:
                    self.draw_tile_debug(self.img, all_coord[i][j], self.blueC, j, i)
                elif state[i][j] is self.Y:
                    self.draw_tile_debug(self.img, all_coord[i][j], self.yellowC, j, i)

        return self.draw_sign(self.img)
