
from cube import Cube
from rotation import Directions, Rotation


def maxcalls():
    global MAXDEPTH
    summa = 0
    for d in range(MAXDEPTH):
        summa += 12**d
    return summa


# TODO
allowed_sequences = [
    "R U R' U R U2 R'", 
    "R U2 R' U' R U' R'", 
    "R' F R F'", 
    "R U R' U'", 
    "U R U' R'", 
    "M2 U M U2 M' U M2", 
    "M2 U' M U2 M' U' M2", 
    "R U R' U R' F R2 U' R' U' R U R' F'",
    "R' U L' U2 R U' R' U2 R L", 
    "L' U' L F L' U' L U L F' L2' U L U", 
    "R U R' F' R U R' U' R' F R2 U' R' U'", 
    "M2' U' M2' U2' M2' U' M2'", 
    "R U R' U' R' F R F'", 
    "F R U R' U' F'", 
    "F (R U R' U') (R U R' U') F'", 
    "F U R U' R' U R U' R' F'", 
    "M2 E2 S2", 
    "R2 L2 U2 D2 F2 B2", 
    "M' U' M2' U' M2' U' M' U2 M2' U", 
]

class Solution:


    def __init__(self):
        self.directions = []
        self.achieved = False
        self.count = 0 

    def as_string(self):
        s = [d.value for d in self.directions]
        return ' '.join(s)
    
    def print(self):
        print(self.as_string())

    def compare_with(self, solution):
        
        if type(solution) != Solution:
            raise TypeError('')
        if self.count < solution.count:
            self.directions = solution.directions
            self.count = max(self.count, solution.count)

    def extend(self, another_solution):
        if type(another_solution) != Solution:
            raise TypeError('Solution.extend() expects a Solution object.')
        self.directions.extend(another_solution.directions)

    def next_rotate_direcion_is_ok(self, d0):
     
        def equal(*directions):
            return all(x.value == directions[0].value for x in directions[1:])

        def is_back(d1, d2):
            return d1.value == d2.value + "'" or d1.value + "'" == d2.value

        def are_opposite_faces(d1, d2):
            if d1.name.startswith('F') and d2.name.startswith('B'):
                return True
            elif d1.name.startswith('L') and d2.name.startswith('R'):
                return True
            elif d1.name.startswith('U') and d2.name.startswith('D'):
                return True
            return False

        if self.achieved:
            return False

        if len(self.directions) >= 1:
            d1 = self.directions[-1]

            if is_back(d0, d1):
                return False

            if len(self.directions) >= 2:
                d2 = self.directions[-2]

                if equal(d0, d1, d2):
                    return False
                if are_opposite_faces(d0, d1) and is_back(d0, d2):
                    return False

                if len(self.directions) >= 3:
                    d3 = self.directions[-3]

                    if equal(d0, d2, d3) and are_opposite_faces(d0, d1):
                        return False
                    if equal(d0, d1, d3) and are_opposite_faces(d0, d2):
                        return False

                    if is_back(d0, d3) and are_opposite_faces(d0, d1) and are_opposite_faces(d0, d2):
                        return False

                    if len(self.directions) >= 4:
                        d4 = self.directions[-4]

                        if equal(d0, d3, d4) and are_opposite_faces(d0, d1) and are_opposite_faces(d0, d2):
                            return False

        return True


MAXDEPTH = 5 
MAXROTATIONS = 12**MAXDEPTH 
MAXCALLS = maxcalls() 
total_rotations = 0 
total_calls = 0 
total_depth = 0 
best_solution = Solution()
longest_formula = Solution()


def solve(cube, solution=Solution(), depth=1):

    global longest_formula

    global best_solution
    if cube.is_assembled():
        solution.achieved = True
        solution.count = cube.count()
        best_solution.compare_with(solution)
        return solution

    global MAXDEPTH, total_depth
    total_depth = max(total_depth, depth)

    global MAXCALLS, total_calls
    if total_calls >= MAXCALLS:
        return
    else:
        total_calls += 1

    global MAXROTATIONS, total_rotations
    for d in list(Directions):

        if total_rotations >= MAXROTATIONS:
            continue
        else:

            if not solution.next_rotate_direcion_is_ok(d):
                continue

            total_rotations += 1
            r = Rotation(cube, d)
            c = r.run()

            s = Solution()
            s.directions = solution.directions + [d]
            s.count = c.count() 
            best_solution.compare_with(s)

            if len(s.directions) > len(longest_formula.directions):
                longest_formula = s

            if c.is_assembled():
                s.achieved = True
                best_solution = s
                return s
            else:
                if depth + 1 > MAXDEPTH:
                    continue 
                else:
                    s = solve(c, s, depth + 1)
                    if s is not None and s.achieved:
                        return s


def run(c=Cube()):

    import time
    start_time = time.perf_counter()

    s = solve(c)
    if total_depth > MAXDEPTH:
        print('DEEP MAX,', total_depth)
    if total_calls > MAXCALLS:
        print('CALL MAX,', total_calls)
    if total_rotations > MAXROTATIONS:
        print('ROTA MAX,', total_rotations)

    print('Optimal sol - {} colours in place:'.format(best_solution.count))
    print(len(best_solution.directions), 'rot')
    print(best_solution.as_string())

    if s is None or not s.achieved:
        print('Fail.')
    else:
        print('Success', s.achieved)

    print('Upper End:')
    print(longest_formula.as_string())

    print()
    print('Height:', total_depth)
    print('Attempts: {} of max {}'.format(total_calls, maxcalls()))
    print('Rota: {} of max {}'.format(total_rotations, 12**total_depth))
    print('Elapsed: {:.1f} seconds.\n'
        .format(time.perf_counter() - start_time))

    print('Var:\n', pow(12, 20))


if __name__ == '__main__':
    run()
