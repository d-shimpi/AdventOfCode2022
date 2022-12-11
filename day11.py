class Monkey:
    def __init__(self, num, starting_items, op, op_num, test_num):
        self.num = num
        self.items = starting_items
        self.op = op
        self.op_num = op_num
        self.test_num = test_num
        self.inspections = 0

    def takeTurn(self, relief, modulo):
        for i in range(0,len(self.items)):
            worry_item = self.items.pop(0) % modulo
            worry_level = 0
            inspect_num = 0

            # Set up the inspection number/operation and inspect the item
            if (self.op_num == 'old'):
                inspect_num = worry_item
            else:
                inspect_num = int(self.op_num)
            if self.op == '*':
                worry_level = worry_item * inspect_num
            else:
                worry_level = worry_item + inspect_num

            # Factor in relief
            if (relief):
                worry_level = worry_level // 3

            # Test and throw
            
            if (worry_level % self.test_num == 0):
                self.true_mon.items.append(worry_level)
            else:
                self.false_mon.items.append(worry_level)
            
            # Increase inspection number
            self.inspections = self.inspections + 1


    def addTestMonkeys(self, true_mon, false_mon):
        self.true_mon = true_mon
        self.false_mon = false_mon

monkeyList = []
day11text = open('day11.txt','r')
monkeyLines = day11text.readlines()

# Initialize Monkeys
for i in range(0,8):
    monkey_num = i
    itemLine = monkeyLines[i*7 + 1]
    itemLine = itemLine[18:-1].split(', ')
    startingItems = [int(i) for i in itemLine]
    inspectLine = monkeyLines[i*7 + 2].split()
    op = inspectLine[4]
    op_num = inspectLine[5]
    testLine = monkeyLines[i*7 + 3].split()
    test_num = int(testLine[3])
    tempMonk = Monkey(monkey_num,startingItems,op,op_num,test_num)
    monkeyList.append(tempMonk)

# Set up true and false test monkeys
for i in range(0,8):
    temp_monkey = monkeyList[i]
    trueLine = monkeyLines[i*7 + 4]
    falseLine = monkeyLines[i*7 + 5]
    trueMon = monkeyList[int(trueLine.split()[5])]
    falseMon = monkeyList[int(falseLine.split()[5])]
    temp_monkey.addTestMonkeys(trueMon,falseMon)

# I am lazy so all I am doing is changing the range from 20 to 10000 for star 2 and also changing the parameter
# Since all the memory is kept I can't just do the loop again at the bottom

# Modular math trick thingy from number theory to keep numbers low and pretty
modulo = 1
for monkey in monkeyList:
    modulo = modulo * monkey.test_num


# Run through 10000 rounds
for i in range(0,10000):
    for monkey in monkeyList:
        monkey.takeTurn(False, modulo)
    #if (i % 100 == 0):
    #    print ("Round " + str(i))

# Find top two monkeys
inspectionList = []
for monkey in monkeyList:
    inspectionList.append(monkey.inspections)
inspectionList.sort(reverse=True)
monkeyBusiness = inspectionList[0] * inspectionList[1]
print("Monkey Business Level: " + str(monkeyBusiness))