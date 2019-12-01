def calculatefuel(mass):
    return int(mass / 3) - 2


def recursivecalculatefuel(mass):
    fuel = calculatefuel(mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + recursivecalculatefuel(fuel)


# Part 1
print('Part 1')
print(sum([calculatefuel(int(line)) for line in open('input.txt')]))

# Part 2
print('\nPart 2')
totalFuel = 0
for line in open('input.txt'):
    totalFuel += recursivecalculatefuel(int(line))
print(totalFuel)
