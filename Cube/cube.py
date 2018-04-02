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
    F F'
    B B'
    D D'
    U U'
    zmiana w plaszczyznie XYZ(aktualnie face to W)
    '''

    def rotate_r(self):
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

    def rotate_r_prime(self):
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

    def rotate_l(self):
        """rotacja L """
        old_state = copy.deepcopy(self.state)
        self.state[0][0] = old_state[1][0]
        self.state[0][3] = old_state[1][3]
        self.state[0][6] = old_state[1][6]
        self.state[1][0] = old_state[5][0]
        self.state[1][3] = old_state[5][3]
        self.state[1][6] = old_state[5][6]
        self.state[4][0] = old_state[0][0]
        self.state[4][3] = old_state[0][3]
        self.state[4][6] = old_state[0][6]
        self.state[5][0] = old_state[4][0]
        self.state[5][3] = old_state[4][3]
        self.state[5][6] = old_state[4][6]

    def rotate_l_prime(self):
        """rotacja L' """
        old_state = copy.deepcopy(self.state)
        self.state[0][0] = old_state[4][0]
        self.state[0][3] = old_state[4][3]
        self.state[0][6] = old_state[4][6]
        self.state[1][0] = old_state[0][0]
        self.state[1][3] = old_state[0][3]
        self.state[1][6] = old_state[0][6]
        self.state[4][0] = old_state[5][0]
        self.state[4][3] = old_state[5][3]
        self.state[4][6] = old_state[5][6]
        self.state[5][0] = old_state[1][0]
        self.state[5][3] = old_state[1][3]
        self.state[5][6] = old_state[1][6]

    def rotate_f(self):
        """rotacja F """
        old_state = copy.deepcopy(self.state)
