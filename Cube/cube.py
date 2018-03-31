import copy

class Cube:
    size_of_tile = 50

    def __init__(self, state=None):
        if state is None:
            state = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                     ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                     ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
                     ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
                     ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']]
        self.state = state

    '''
    R R'
    L L'
    F F'
    B B'
    D D'
    U U'
    '''

    def rotate_r(self):
        """rotacja R"""
        old_state = copy.deepcopy(self.state)
        self.state[0][2] = old_state[4][2]
        self.state[0][5] = old_state[4][5]
        self.state[0][8] = old_state[4][8]
        self.state[1][2] = old_state[0][2]
        self.state[1][5] = old_state[0][5]
        self.state[1][8] = old_state[0][8]
        self.state[4][2] = old_state[5][2]
        self.state[4][5] = old_state[5][5]
        self.state[4][8] = old_state[5][8]
        self.state[5][2] = old_state[1][2]
        self.state[5][5] = old_state[1][5]
        self.state[5][8] = old_state[1][8]

    def rotate_r_prime(self):
        """rotacja R' """
        old_state = copy.deepcopy(self.state)
        self.state[0][2] = old_state[1][2]
        self.state[0][5] = old_state[1][5]
        self.state[0][8] = old_state[1][8]
        self.state[1][2] = old_state[5][2]
        self.state[1][5] = old_state[5][5]
        self.state[1][8] = old_state[5][8]
        self.state[4][2] = old_state[0][2]
        self.state[4][5] = old_state[0][5]
        self.state[4][8] = old_state[0][8]
        self.state[5][2] = old_state[4][2]
        self.state[5][5] = old_state[4][5]
        self.state[5][8] = old_state[4][8]
