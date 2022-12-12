from time import time

class monkey():

    inspections = 0

    def __init__(self, items, operation, test, throw_tos):
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_tos = throw_tos

    def inspect(self,n):
        self.inspections += 1

        item = self.items[0]
        operation = self.operation
        test = self.test
        throw_tos = self.throw_tos

        new_worry = operation(item)
        #new_worry = relieve(new_worry)     # part 1
        new_worry = new_worry % n
        self.items[0] = new_worry
        
        if test(self.items[0]) == 0: return int(throw_tos[0])
        else: return int(throw_tos[1])

    def throw(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item
    
    def catch(self,item):
        items = self.items
        items.append(item)
        self.items = items

    def peek(self):
        print(' items: ' + str(self.items))
        print(' operation: ' + str(self.operation))
        print(' test: ' + str(self.test))
        print(' throw_tos: ' + str(self.throw_tos))
        print(' inspections: ' + str(self.inspections) + '\n')

class barrel():
    monkies = []
    product_of_divisors = 1

    def peek(self):
        for i in range(len(self.monkies)):
            monkey = self.monkies[i]
            print('Monkey ' + str(i))
            monkey.peek()

    def execute_round(self):
        for monkey in self.monkies:
            while monkey.items != []:    # executes 1 turn

                #thrower_num = int(monkey.inspect())    # part 1
                thrower_num = monkey.inspect(self.product_of_divisors)
                to = self.monkies[thrower_num]
                self.handle_throw(to,monkey)

            

    def handle_throw(self, to, frm):
        item = frm.throw()
        to.catch(item)


    def make_monkey(self, attributes):

        # items
        instruction = attributes[1]
        items = [int(item.replace(',','')) for item in instruction.split(' ')[2:]]

        # operation
        instruction = attributes[2]
        operation_instruction = instruction.split(' ')[4:6]
        
        match operation_instruction[0]:
            case '*':
                if operation_instruction[1] == 'old': operation = lambda x: x * x
                else: operation = lambda x: x * int(operation_instruction[1])
            case '+':
                if operation_instruction[1] == 'old': operation = lambda x: x + x
                else: operation = lambda x: x + int(operation_instruction[1])

        # test
        instruction = attributes[3]
        n = int(instruction[19:])
        self.product_of_divisors *= n
        test = lambda x: x % n

        # throw_tos
        throw_tos = []
        for instruction in attributes[4:]:
            throw_tos.append(instruction[-1])


        new_monkey = monkey(items, operation, test, throw_tos)

        self.monkies.append(new_monkey)
        return

    def monkey_business_level(self):
        monkies = self.monkies

        activity = [m.inspections for m in monkies]
        record = [max(activity)]
        activity.remove(record[0])
        record.append(max(activity))
        
        #mbus = [i for i in range(len(monkies)) if monkies[i].inspections in record]
        return record[0] * record[1]


def relieve(x):
    return x // 3

with open('day11.txt','r') as f:
    lines = f.readlines()

    brl = barrel()

    for i in range(0, 50, 7):

        attributes = [line.strip() for line in lines[i:i+6]]
        brl.make_monkey(attributes)

    #brl.peek()
    for _ in range(10000):
        #t = time()
        brl.execute_round()
        #print('Took ' + str(time() - t) + 'sec')

    print(brl.monkey_business_level())
    #brl.peek()