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
            self.f = 'W'
            self.b = 'Y'
            self.l = 'O'
            self.r = 'R'
            self.u = 'B'
            self.d = 'G'
        self.state = state
        self.f = state[0][4]
        self.b = state[5][4]
        self.l = state[2][4]
        self.r = state[3][4]
        self.u = state[4][4]
        self.d = state[1][4]

    '''
    L L'
    F F'
    B B'
    D D'
    U U'
    zmiana w plaszczyznie XYZ(aktualnie face to W)
    '''

    def faces(self):
        return '-----------------\n' \
               'Face: ' + str(self.f) + ' Back: ' + str(self.b)\
               + '\nLeft: ' + str(self.l) + ' Right: ' + str(self.r)\
               + '\nUp: ' + str(self.u) + ' Down: ' + str(self.d)\
               + '\n-----------------'

    def rotate_x(self):
        """rotacja X"""
        old_state = copy.deepcopy(self.state)
        self.f = old_state[3][4]
        self.b = old_state[2][4]
        self.l = old_state[0][4]
        self.r = old_state[5][4]
        self.u = old_state[4][4]
        self.d = old_state[1][4]
        self.state[0] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.f][0]]
        self.state[1] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.d][0]]
        self.state[2] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.l][0]]
        self.state[3] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.r][0]]
        self.state[4] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.u][0]]
        self.state[5] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.b][0]]

    def rotate_y(self):
        """rotacja X"""
        old_state = copy.deepcopy(self.state)
        self.f = old_state[1][4]
        self.b = old_state[4][4]
        self.l = old_state[2][4]
        self.r = old_state[3][4]
        self.u = old_state[0][4]
        self.d = old_state[5][4]
        self.state[0] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.f][0]]
        self.state[1] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.d][0]]
        self.state[2] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.l][0]]
        self.state[3] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.r][0]]
        self.state[4] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.u][0]]
        self.state[5] = old_state[[i for i in range(len(old_state)) if old_state[i][4] == self.b][0]]

    def rotate_r(self):
        """rotacja R' """
        old_state = copy.deepcopy(self.state)
        self.state[0][2] = old_state[1][2]
        self.state[0][5] = old_state[1][5]
        self.state[0][8] = old_state[1][8]
        self.state[1][2] = old_state[5][2]
        self.state[1][5] = old_state[5][5]
        self.state[1][8] = old_state[5][8]
        self.state[3][0] = old_state[3][2]
        self.state[3][1] = old_state[3][5]
        self.state[3][2] = old_state[3][8]
        self.state[3][3] = old_state[3][1]
        self.state[3][5] = old_state[3][7]
        self.state[3][6] = old_state[3][0]
        self.state[3][7] = old_state[3][3]
        self.state[3][8] = old_state[3][6]
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
        self.state[3][0] = old_state[3][6]
        self.state[3][1] = old_state[3][3]
        self.state[3][2] = old_state[3][0]
        self.state[3][3] = old_state[3][7]
        self.state[3][5] = old_state[3][1]
        self.state[3][6] = old_state[3][8]
        self.state[3][7] = old_state[3][5]
        self.state[3][8] = old_state[3][2]
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
        # Brak calej sciany O

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
        # Brak calej sciany O
