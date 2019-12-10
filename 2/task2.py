def processInput(input, noun, verb):
    # input = [1,9,10,3,2,3,11,0,99,30,40,50]
    input[1] = noun
    input[2] = verb

    ipointer = 0
    opcode = input[ipointer]
    while opcode != 99:
        position1 = input[ipointer + 1]
        position2 = input[ipointer + 2]
        position3 = input[ipointer + 3]
        if opcode == 1:
            input[position3] = input[position1] + input[position2]
        elif opcode == 2:
            input[position3] = input[position1] * input[position2]
        else:
            print()
        ipointer += 4
        opcode = input[ipointer]
    return input[0]



inputtext = open('input.txt').read()
list = [int(n) for n in inputtext.split(',')]

# Part 1
print('Part 1:')
print(processInput(list, 12, 2))


# Part 2
print('Part 2:')
for noun in range(99):
    for verb in range(99):
        copyofinput = list.copy()
        try:
            result = processInput(copyofinput, noun, verb)
            if result == 19690720:
                print(noun, verb)
        except:
            print()
print(100*80+18)
