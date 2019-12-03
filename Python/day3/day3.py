
# Parse inputs
wire1 = [[x[0], int(x[1:])] for x in open("wire1.txt").read().split(",")]
wire2 = [[x[0], int(x[1:])] for x in open("wire2.txt").read().split(",")]

# x/y directions for commands
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


# Get all points that a wire visits
def get_points(w):
    x = 0
    y = 0
    length = 0
    ans = {}
    for cmd in w:
        for _ in range(cmd[1]):
            x += DX[cmd[0]]
            y += DY[cmd[0]]
            length += 1
            if (x, y) not in ans:
                ans[(x, y)] = length
    return ans


# Get the points that the wires visit
path1 = get_points(wire1)
path2 = get_points(wire2)

# Get the points that both wires visit
both = set(path1.keys()) & set(path2.keys())

# Shortest distance from (0, 0) to any intersection
part1 = min([abs(x) + abs(y) for (x, y) in both])
# Shortest path to any intersection
part2 = min([path1[p] + path2[p] for p in both])

print(" Day 3 ".center(64, "-"))
print(f"Distance to intersection closest to central port: {part1}".center(64))
print(f"Shortest path to intersection from central port: {part2}".center(64))
print("".center(64, "-"))
