class chamber:
    def __init__(self,gas):
        self.rocks = []     # list of coords of settled rocks
        self.next_rock = 1
        
        self.gas = gas
        self.next_gas_index = 0

    def print_map(self):

        if self.rocks == []:
            print('.......')

        else:
            for y in range(self.find_height(),-1,-1):
                for x in range(7):

                    if [x,y] in self.rocks: print('#',end='')
                    else: print('.',end='')
                print()
        print()

    def drop_rock(self):

        # find y placement
        starting_y = self.find_height() + 3

        # initialize rock
        falling = rock(self.next_rock,starting_y)

        # while rock isn't settled
            # see where rock wants to blow
                # if it can go there, move it
                # if not, don't
            # see if rock can fall
                # if it can, let it
                # if not, settle it

        while not self.check_down(falling):
            direction = self.get_next_direction()

            match direction:
                case '>':
                    if not self.check_right(falling):
                        falling.blow_right()

                case '<':
                    if not self.check_left(falling):
                        falling.blow_left()

            falling.fall()
            
        self.rocks.extend(falling.coords)

        self.get_next_rock()

    # returns highest unoccupied y level
    def find_height(self):
        if self.rocks == []: return 0
        
        y_vals = [rock[1] for rock in self.rocks] 
        
        return max(y_vals)+1

    def get_next_rock(self):
        if self.next_rock == 4:
            self.next_rock = 1
        else:
            self.next_rock += 1

    def check_down(self, rock):
        for coord in rock.coords:
            next_coord = [coord[0],coord[1]-1]

            if next_coord in self.rocks or next_coord[1] == -1:
                return 1
                
        return 0

    def check_right(self, rock):
        for coord in rock.coords:
            next_coord = [coord[0]+1,coord[1]]

            if next_coord in self.rocks or next_coord[0] == 7:
                return 1
                
        return 0

    def check_left(self, rock):
        for coord in rock.coords:
            next_coord = [coord[0]-1,coord[1]]

            if next_coord in self.rocks or next_coord[0] == -1:
                return 1
                
        return 0

    def get_next_direction(self):
        if self.next_gas_index == len(self.gas)-1:
            self.next_gas_index = 0
        else: self.next_gas_index += 1

        return self.gas[self.next_gas_index]

class rock:
    def __init__(self,type,starting_y):
        self.coords = self.get_coords(type, starting_y)

    def get_coords(self, type, y):

        match type:
            case 1:
                return [[2,y],[3,y],[4,y],[5,y]]

            case 2:
                return [[3,y],[2,y+1],[3,y+1],[4,y+1],[3,y+2]]

            case 3:
                return [[2,y],[3,y],[4,y],[4,y+1],[4,y+2]]

            case 4:
                return [[2,y],[2,y+1],[2,y+2],[2,y+3]]

            case 5:
                return [[2,y],[3,y],[2,y+1],[3,y+1]]
    

    def fall(self):
        for x in self.coords:
            x[1] -= 1
        return

    def blow_right(self):
        for x in self.coords:
            x[0] += 1
        return

    def blow_left(self):
        for x in self.coords:
            x[0] -= 1
        return
        
with open('helper.txt', 'r') as f:
#with open('day17.txt', 'r') as f:
    gas = [push for push in f.read() if push == '>' or push == '<']

cave = chamber(gas)

for _ in range(2):
    cave.drop_rock()
    cave.print_map()

#for _ in range(2022):
#    cave.drop_rock()
#print(cave.find_height())