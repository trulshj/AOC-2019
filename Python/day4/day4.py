
# Range from puzzle input
minimum = 197487
maximum = 673251


# Check whether the number has similar adjacent digits
def has_adjacent(n):
    n = str(n)
    for idx, c in enumerate(n):
        if idx+1 < len(n) and c == n[idx+1]:
            return True
    return False


# Check if a number is strictly increasing
def is_rising(n):
    n = str(n)
    for idx, c in enumerate(n):
        if idx+1 < len(n) and int(c) > int(n[idx + 1]):
            return False
    return True


# Make another function to not cannibalize part 1
# Checks if there is strictly a pair of similar digits
def has_adjacent_p2(n):
    n = str(n)
    groups = {}
    for idx, c in enumerate(n):
        if idx+1 < len(n) and c == n[idx+1]:
            if c not in groups.keys():
                groups[c] = 1
            groups[c] += 1
    if 2 in groups.values():
        return True
    else:
        return False


part1, part2 = 0, 0

# Brute force because it's only 6 digits ;P
for i in range(minimum, maximum + 1):
    if has_adjacent(i):
        if is_rising(i):
            part1 += 1
            if has_adjacent_p2(i):
                part2 += 1

print(" Day 4 ".center(64, "-"))
print(f"Possible passwords Part 1: {part1}".center(64))
print(f"Possible passwords Part 2: {part2}".center(64))
print("".center(64, "-"))
