
from cube import Cube
from rotation import Rotation, recognize_rotations
import solver


def main():
    """Test cube's rotations."""
    c = Cube()
    x = input()
    string = "D' F U L' U"
    directions = recognize_rotations(string)
    for d in directions:
        r = Rotation(c, d)
        c = r.run()
   # c.inputCube(x)
    solver.run(c)
    

if __name__ == '__main__':
    main()
