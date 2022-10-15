
from enum import Enum


class Color(Enum):
    RED = 'R' 
    ORANGE = 'O' 
    BLUE = 'B' 
    GREEN = 'G' 
    YELLOW = 'Y' 
    WHITE = 'W' 


class Cube:

    def __init__(self):
        self.FRONT = Face(Color.RED)
        self.BACK = Face(Color.ORANGE)
        self.LEFT = Face(Color.BLUE)
        self.RIGHT = Face(Color.GREEN)
        self.UP = Face(Color.YELLOW)
        self.DOWN = Face(Color.WHITE)
        self.faces = [
            self.FRONT, self.BACK,
            self.LEFT, self.RIGHT,
            self.UP, self.DOWN
        ]
        print(Face(Color.RED))

    def count(self):
        return sum(f.count() for f in self.faces)

    def is_assembled(self):
        for f in self.faces:
            if not f.is_assembled():
                return False
        return True

    def print(self):
        print('FRONT    BACK     LEFT     RIGHT    UP       DOWN')
        for row in range(3):
            for f in self.faces:
                f.print_row(row)
            print()
        print()

    def print_colored(self):
        # TODO: implement
        pass

    def inputCube(self, x):
        self.FRONT = Face(Color.RED)
        self.BACK = Face(Color.ORANGE)
        self.LEFT = Face(Color.BLUE)
        self.RIGHT = Face(Color.GREEN)
        self.UP = Face(Color.YELLOW)
        self.DOWN = Face(Color.WHITE)
        self.faces = [
            self.FRONT, self.BACK,
            self.LEFT, self.RIGHT,
            self.UP, self.DOWN
        ]
        self.FRONT.set_face(x[0:9])
        self.BACK.set_face(x[9:18])
        self.LEFT.set_face(x[18:27])
        self.RIGHT.set_face(x[27:36])
        self.UP.set_face(x[36:45])
        self.DOWN.set_face(x[45:54])




class Face:
 
    def __init__(self, color):
        self.colors = [color, ] * 9
        self.origin_color = color
    
    def count(self):
        return sum(1 for c in self.colors if c == self.origin_color)

    def rotate_cw(self):
        l = [
            self.colors[6],
            self.colors[3],
            self.colors[0],
            self.colors[7],
            self.colors[4],
            self.colors[1],
            self.colors[8],
            self.colors[5],
            self.colors[2],
        ]
        self.colors = l

    def rotate_cc(self):
        l = [
            self.colors[2],
            self.colors[5],
            self.colors[8],
            self.colors[1],
            self.colors[4],
            self.colors[7],
            self.colors[0],
            self.colors[3],
            self.colors[6],
        ]
        self.colors = l

    def get_row(self, row):
        return [self.colors[row * 3 + col] for col in range(3)]

    def get_col(self, col):
        return [self.colors[row * 3 + col] for row in range(3)]

    def set_row(self, row, colors):
        for col in range(3):
            self.colors[row * 3 + col] = colors[col]

    def set_col(self, col, colors):
        for row in range(3):
            self.colors[row * 3 + col] = colors[row]
    
    def set_face(self, colors):
        for i in range(9):
            self.colors[i] = colors[i]

    def is_assembled(self):
        c = self.colors[0]
        for i in range(1, len(self.colors)):
            if self.colors[i] != c:
                return False
        return True

    def print_row(self, row):
        s = ' '.join(self.colors[row * 3 + col].value for col in range(3))
        print(s.ljust(9), end='')


if __name__ == '__main__':
    from rotation import Rotation, Directions
    c = Cube()
    d = Directions.FCW
    r = Rotation(c, d)
    c = r.run()
    print(c.count())

   