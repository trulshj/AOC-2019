
modules = [int(line.rstrip()) for line in open("input.txt").readlines()]


# Part 1
def get_fuel(n):
    return n//3-2


fuel = sum([get_fuel(m) for m in modules])
print(f"Total fuel required: {fuel}")


# Part 2
total = 0
for mass in modules:
    fuel = get_fuel(mass)
    while fuel > 0:
        total += fuel
        fuel = get_fuel(fuel)

print(f"Total fuel accounting for mass of fuel: {total}")
