import time
from datastructures.array2d import Array2D
from projects.project2.Grid import Grid
from projects.project2.kbhit import KBHit

class Game_Control:
    def __init__(self, grid: Grid) -> None:
        print("from the constructor")
        self.grid = grid
        self.history = []

    def run(self, max_iter : int) -> None:
        kb = KBHit()
        print("Press 'Q' to quit.")
        print("Press 'S' to step to the next generation.")
        print("Press 'C' to continue.")
        generation = 0
        step_mode = False
        while generation < max_iter:
            print(f'Generation: {generation}')
            generation += 1
            self.grid.display()
            time.sleep(1)
            self.history.append(self.grid)
            new_grid = self.grid.next_gen()
            if len(self.history) > 5:
                if self.history[-1] == new_grid or self.history[-2] == new_grid or self.history[-3] == new_grid:
                    break
                del self.history[0]
            self.grid = new_grid
            if kb.kbhit() or step_mode:
                c = (kb.getch()).upper()
                print(c)
                time.sleep(2)
                if c == 'Q':
                    break
                print(c)
                if c == 'S':
                    step_mode = True
                print(c)
                if c == 'C':
                    step_mode = False
                else:
                    continue
                print("The colony is either alive or dead for infinity")
                kb.set_normal_term()
            else:
                continue

    def eq(self, other: object) -> bool:
        if not isinstance(other, Array2D) or len(self.array2d) != len(other.array2d):
            return False
        return self.array2d == other.array2d

