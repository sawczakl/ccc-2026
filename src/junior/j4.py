M = int(input()) # of movements

# numbers for initial position is arbitrary
# (x, y). increment x for east, increment y for north
pos = (0, 0)

# slime positions. starting pos starts in there.
# may cause memory issue... let's see
slimes = {pos}

n_slime_crossings = 0

# Table for differences to unify logic and reduce repeated code
# This table maps direction to (x, y) difference for position shift per step
DIRECTIONS = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

for _ in range(M):
    val = input()
    direction, n = val[0], int(val[1:])

    # Get shifts for this direction and unpack for clarity
    shifts = DIRECTIONS[direction]
    dx, dy = shifts

    # Take steps one at a time (inefficient)
    for i in range(1, n + 1):

        # New pos by applying the shifts
        pos = (pos[0] + dx, pos[1] + dy)

        # If it's in the slime set
        if pos in slimes:
            n_slime_crossings += 1

        # Add it to the slime set
        slimes.add(pos)

print(n_slime_crossings)
