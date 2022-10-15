

import copy
from enum import Enum


class Directions(Enum):
    FCW = "F"; FCC = "F'"
    BCW = "B"; BCC = "B'"
    LCW = "L"; LCC = "L'"
    RCW = "R"; RCC = "R'"
    UCW = "U"; UCC = "U'"
    DCW = "D"; DCC = "D'"


class Rotation:
 

    def __init__(self, cube, direction):
        self.cube = copy.deepcopy(cube)
        self.direction = direction

    def run(self):
      
        fname = f'rotate_{self.direction.name[0]}'
        getattr(self, fname)()
        return self.cube

    def rotate_F(self):
       
        L_col2 = self.cube.LEFT.get_col(2)
        U_row2 = self.cube.UP.get_row(2)
        R_col0 = self.cube.RIGHT.get_col(0)
        D_row0 = self.cube.DOWN.get_row(0)

        if self.direction == Directions.FCW:
            self.cube.FRONT.rotate_cw()
            self.cube.LEFT.set_col(2, D_row0)
            self.cube.UP.set_row(2, L_col2)
            self.cube.RIGHT.set_col(0, U_row2)
            self.cube.DOWN.set_row(0, R_col0)
        elif self.direction == Directions.FCC:
            self.cube.FRONT.rotate_cc()
            self.cube.LEFT.set_col(2, U_row2)
            self.cube.UP.set_row(2, R_col0)
            self.cube.RIGHT.set_col(0, D_row0)
            self.cube.DOWN.set_row(0, L_col2)

    def rotate_B(self):

        R_col2 = self.cube.RIGHT.get_col(2)
        U_row0 = self.cube.UP.get_row(0)
        L_col0 = self.cube.LEFT.get_col(0)
        D_row2 = self.cube.DOWN.get_row(2)

        if self.direction == Directions.BCW:
            self.cube.BACK.rotate_cw()
            self.cube.RIGHT.set_col(2, D_row2)
            self.cube.UP.set_row(0, R_col2)
            self.cube.LEFT.set_col(0, U_row0)
            self.cube.DOWN.set_row(2, L_col0)
        elif self.direction == Directions.BCC:
            self.cube.BACK.rotate_cc()
            self.cube.RIGHT.set_col(2, U_row0)
            self.cube.UP.set_row(0, L_col0)
            self.cube.LEFT.set_col(0, D_row2)
            self.cube.DOWN.set_row(2, R_col2)

    def rotate_L(self):

        B_col0 = self.cube.BACK.get_col(0)
        U_col0 = self.cube.UP.get_col(0)
        F_col0 = self.cube.FRONT.get_col(0)
        D_col0 = self.cube.DOWN.get_col(0)

        if self.direction == Directions.LCW:
            self.cube.LEFT.rotate_cw()
            self.cube.BACK.set_col(0, D_col0)
            self.cube.UP.set_col(0, B_col0)
            self.cube.FRONT.set_col(0, U_col0)
            self.cube.DOWN.set_col(0, F_col0)
        elif self.direction == Directions.LCC:
            self.cube.LEFT.rotate_cc()
            self.cube.BACK.set_col(0, U_col0)
            self.cube.UP.set_col(0, F_col0)
            self.cube.FRONT.set_col(0, D_col0)
            self.cube.DOWN.set_col(0, B_col0)

    def rotate_R(self):
 
        F_col2 = self.cube.FRONT.get_col(2)
        U_col2 = self.cube.UP.get_col(2)
        B_col0 = self.cube.BACK.get_col(0)
        D_col2 = self.cube.DOWN.get_col(2)

        if self.direction == Directions.RCW:
            self.cube.RIGHT.rotate_cw()
            self.cube.FRONT.set_col(2, D_col2)
            self.cube.UP.set_col(2, F_col2)
            self.cube.BACK.set_col(0, U_col2)
            self.cube.DOWN.set_col(2, B_col0)
        elif self.direction == Directions.RCC:
            self.cube.RIGHT.rotate_cc()
            self.cube.FRONT.set_col(2, U_col2)
            self.cube.UP.set_col(2, B_col0)
            self.cube.BACK.set_col(0, D_col2)
            self.cube.DOWN.set_col(2, F_col2)

    def rotate_U(self):
    
        L_row0 = self.cube.LEFT.get_row(0)
        F_row0 = self.cube.FRONT.get_row(0)
        R_row0 = self.cube.RIGHT.get_row(0)
        B_row0 = self.cube.BACK.get_row(0)

        if self.direction == Directions.UCW:
            self.cube.UP.rotate_cw()
            self.cube.LEFT.set_row(0, F_row0)
            self.cube.FRONT.set_row(0, R_row0)
            self.cube.RIGHT.set_row(0, B_row0)
            self.cube.BACK.set_row(0, L_row0)
        elif self.direction == Directions.UCC:
            self.cube.UP.rotate_cc()
            self.cube.LEFT.set_row(0, B_row0)
            self.cube.FRONT.set_row(0, L_row0)
            self.cube.RIGHT.set_row(0, F_row0)
            self.cube.BACK.set_row(0, R_row0)

    def rotate_D(self):

        L_row2 = self.cube.LEFT.get_row(2)
        F_row2 = self.cube.FRONT.get_row(2)
        R_row2 = self.cube.RIGHT.get_row(2)
        B_row2 = self.cube.BACK.get_row(2)

        if self.direction == Directions.DCW:
            self.cube.DOWN.rotate_cw()
            self.cube.LEFT.set_row(2, B_row2)
            self.cube.FRONT.set_row(2, L_row2)
            self.cube.RIGHT.set_row(2, F_row2)
            self.cube.BACK.set_row(2, R_row2)
        elif self.direction == Directions.DCC:
            self.cube.DOWN.rotate_cc()
            self.cube.LEFT.set_row(2, F_row2)
            self.cube.FRONT.set_row(2, R_row2)
            self.cube.RIGHT.set_row(2, B_row2)
            self.cube.BACK.set_row(2, L_row2)


def recognize_rotations(string):

    directions = {d.value:d for d in list(Directions)}
    rotations = []
    for s in string.replace(' ', ''):
        if s in directions or s == "'":
            if s == "'":
                d = directions[rotations[-1].value + "'"]
                rotations[-1] = d
            else:
                d = directions[s]
                rotations.append(d)
        else:
            raise ValueError('Invalid rotation symbol "{}"'.format(s))
    return rotations


if __name__ == '__main__':
    string = "FF'BB'LL'RR'UU'DD'"
    for r in recognize_rotations(string):
        print('{}\t{}'.format(r.value, r))
