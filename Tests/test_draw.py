import unittest
from Cube import CubeDraw
from PIL import Image, ImageStat


class TestCubeDraw(unittest.TestCase):
    def setUp(self):
        self.Tstate = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                       ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                       ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                       ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
                       ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
                       ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']]
        self.Tsize_of_tile = 50
        self.Timg = CubeDraw(self.Tsize_of_tile)
        self.TgreenC = (127, 255, 0)
        self.TwhiteC = (255, 255, 255)
        self.TblueC = (0, 0, 255)
        self.TyellowC = (255, 255, 0)
        self.TorangeC = (255, 127, 0)
        self.TredC = (255, 0, 0)
        self.TgrayC = (127, 127, 127)
        self.TblackC = (0, 0, 0)
        self.T_img = None

    def test_variables(self):
        self.assertEqual(self.Timg.size_of_tile, self.Tsize_of_tile)
        self.assertEqual(self.Timg.greenC, self.TgreenC)
        self.assertEqual(self.Timg.whiteC, self.TwhiteC)
        self.assertEqual(self.Timg.blueC, self.TblueC)
        self.assertEqual(self.Timg.yellowC, self.TyellowC)
        self.assertEqual(self.Timg.orangeC, self.TorangeC)
        self.assertEqual(self.Timg.redC, self.TredC)
        self.assertEqual(self.Timg.grayC, self.TgrayC)
        self.assertEqual(self.Timg.blackC, self.TblackC)
        self.assertEqual(self.Timg.img, self.T_img)

    def test_draw_init(self):
        self.assertEqual(type(self.Timg.draw_init()), type(Image.new('RGB', (10, 10))))
        self.assertEqual(self.Timg.draw_init(), Image.new('RGB', (self.Tsize_of_tile * 12, self.Tsize_of_tile * 9), self.TgrayC))
        self.assertEqual(tuple(ImageStat.Stat(self.Timg.draw_init()).median), self.TgrayC)

    def test_draw_tile(self):
        self.T_img = self.Timg.draw_init()
        self.assertEqual(type(self.Timg.draw_tile(self.T_img, (0, 0), self.TwhiteC)), type(Image.new('RGB', (10, 10))))

    def test_draw_sign(self):
        self.T_img = self.Timg.draw_init()
        self.assertEqual(type(self.Timg.draw_sign(self.T_img)), type(Image.new('RGB', (10, 10))))

    def test_draw_state(self):
        self.assertEqual(type(self.Timg.draw_state(self.Tstate)), type(Image.new('RGB', (10, 10))))
        self.assertEqual(self.Timg.draw_state(self.Tstate).size, (self.Tsize_of_tile * 12, self.Tsize_of_tile * 9))
        self.assertEqual(tuple(ImageStat.Stat(self.Timg.draw_init()).median), self.TgrayC)
