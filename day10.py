from functools import reduce

class register():
    x = 1
    cycle = 1
    vals = []
    pic = []

    def addx(self, V):

        self.tick()
        self.tick()

        self.x += V

        return


    def noop(self):

        self.tick()

        return

    
    def get_signal_strength(self):
        return self.x * self.cycle


    def read_instruction(self, instruct):
        func = instruct[:4]

        match func:
            case 'addx':
                V = int(instruct[4:])
                self.addx(V)
            case 'noop':
                self.noop()

        return


    def tick(self):
        self.check_sprite()
        #self.print()

        #if self.cycle in [20,60,100,140,180,220]:
         #   self.vals.append(self.get_signal_strength())
        #else: return 0

        self.cycle += 1
        return
    
    
    def print(self):

        print("x =", self.x)
        print("cycle =", self.cycle)
        print("vals =", self.vals)
        print()


    def check_sprite(self):
        x = self.x + 1
        cycle = self.cycle

        if cycle in range(x-1,x+2):
            print("#",end='')
            #self.pic.append('#')
        else: 
            print('.',end='')
            #self.pic.append('.')

        if cycle in range(40,240,40):
            self.cycle -= 40
            print()
        
        return


with open("day10.txt", 'r') as f:
    instructions = [line.strip() for line in f.readlines()]
    reg = register()

    for instruct in instructions: 
        reg.read_instruction(instruct)
    
    #reg.draw()