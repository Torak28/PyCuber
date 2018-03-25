from draw import CubeDraw
from PIL import Image

size_of_tile = 50
state = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
         ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
         ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
         ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']]


cube_draw = CubeDraw(size_of_tile)
cube_draw = cube_draw.draw_state(state).show()
