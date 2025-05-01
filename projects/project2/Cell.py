class Cell:
    def __init__(self, is_alive: bool = False) -> None:
        self.alive = is_alive

    def num_neighbors(self):
        pass

    def __eq__(self, other: object) -> bool:
        return self.alive == other.alive

    def __str__(self):
        return "🦠" if self.alive else "⬛"

    @property
    def is_alive(self) -> bool:
        return self.alive

    @is_alive.setter
    def is_alive(self, is_alive: bool) -> None:
        self.alive = is_alive

    #print grid
    #loop until break
    #generate next grid
    #-iterate grid
    #-count neighbors
    #-run rules
    #save current grid to grid history
    #print grid 
    #set grid = new_grid