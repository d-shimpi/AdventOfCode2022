day10txt = open('day10.txt','r')
commands = day10txt.readlines()

x = 1
cycle_vals = {1:1}
cycle = 1

for command in commands:
    command = command[:-1]
    cycle = cycle+1
    if command == 'noop':
        cycle_vals[cycle] = x
        continue
    else:
        cycle_vals[cycle] = x
        add_val = int(command.split()[1])
        x = x + add_val
        cycle_vals[cycle+1] = x
        cycle = cycle+1

sum_sig_strength = 0
for i in range (0,6):
    interest_cycle = 20 + i*40
    sum_sig_strength += interest_cycle*cycle_vals[interest_cycle]
print("The sum of the interesting signal strenghts is: " + str(sum_sig_strength))


crt_screen = ''
for i in range(0,6):
    for j in range(1,41):
        cycle = i*40 + j
        position = (cycle % 40) - 1
        if cycle_vals[cycle] in [position-1,position,position+1]:
            crt_screen += '#'
        else:
            crt_screen += '.'
    crt_screen += '\n'
print(crt_screen)








    