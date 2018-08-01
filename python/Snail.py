def snail(array):
    rows, cols = len(array), len(array[0])
    seens = []

    i = 0 # row index
    j = 0 # column index
    
    while i < rows and j < cols:
        
        for n in range(j, cols):
            seens.append(array[i][n])
        i += 1 
        
        for n in range(i, rows):
            seens.append(array[n][cols - 1])
        cols -= 1 
        
        if rows > cols:
            for n in range(cols - 1, j - 1, -1):
                seens.append(array[rows - 1][n])
                
            rows -= 1 
            
        if rows <= cols:
            for n in range(rows - 1, i - 1, -1):
                seens.append(array[n][j])
            j += 1
            
    return seens


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]    
print(snail(array))



""""""""""""""""""""""""""""""""""""""""""
# Good solution
""""""""""""""""""""""""""""""""""""""""""

def snail(array):
    mission = Game(array)
    path = []
    while mission.we_are_not_done:
        path.append(mission.dig_at_location())
        if mission.it_is_safe_to_slither:
            mission.slither_onwards_good_soldier()
        else:
            mission.turn_away_from_fire()
            mission.slither_onwards_good_soldier()
    return path


class Game(object):
    def __init__(self, array):
        self.map = array
        self.moves_left = len(array) * len(array[0])
        self.coords = {"x": 0, "y": len(array)-1}  # start in NW area.
        self.dir = "E"  # slitherin' east.
        self.fire = {"min_x": -1, "min_y": -1, "max_x": len(array),
                     "max_y": len(array)}  # the carpet is lava.
        self.rules = {"N": {"x": 0, "y": 1, "turn": "E"},
                      "E": {"x": 1, "y": 0, "turn": "S"},
                      "S": {"x": 0, "y": -1, "turn": "W"},
                      "W": {"x": -1, "y": 0, "turn": "N"}}

    def slither_onwards_good_soldier(self):
        self.coords["x"] = self.next_x
        self.coords["y"] = self.next_y
        self._subtract_move()

    def turn_away_from_fire(self):
        self._become_aware_that_the_world_is_closing_in()
        self.dir = self.rules[self.dir]["turn"]

    def dig_at_location(self):
        # have to invert the y location for the purpose of the array.
        return self.map[len(self.map)-self.coords["y"]-1][self.coords["x"]]

    def report_in(self):
        print("Dear Sir! I'm stationed @ x: %s, y: %s, heading %s." %
              (self.coords["x"], self.coords["y"], self.dir))

    @property
    def it_is_safe_to_slither(self):
        x = self.next_x
        y = self.next_y
        if x != self.fire["min_x"] and \
           x != self.fire["max_x"] and \
           y != self.fire["min_y"] and \
           y != self.fire["max_y"]:
            return True

    @property
    def we_are_not_done(self):
        if self.moves_left > 0:
            return True

    @property
    def next_x(self):
        return self.coords["x"] + self.rules[self.dir]["x"]

    @property
    def next_y(self):
        return self.coords["y"] + self.rules[self.dir]["y"]

    def _become_aware_that_the_world_is_closing_in(self):
        if self.dir == "N":
            self.fire["min_x"] += 1
        if self.dir == "E":
            self.fire["max_y"] -= 1
        if self.dir == "S":
            self.fire["max_x"] -= 1
        if self.dir == "W":
            self.fire["min_y"] += 1

    def _subtract_move(self):
        self.moves_left -= 1
