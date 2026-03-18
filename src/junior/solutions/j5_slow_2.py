N = int(input()) # number of spots
L = int(input()) # number of lights
Q = int(input()) # number of spots to be questioned about

# This one uses ranges instead of spots; it makes adding faster,
# but lookups slower.

# Reminder that spots are numbered from 1, not from 0
illumined_ranges = set()

# Read the lights
for _ in range(L):
    vals = input().split()
    light_spot, spread = int(vals[0]), int(vals[1])

    # Bound the start and end of the range
    lower = max(0, light_spot - spread)
    upper = min(N, light_spot + spread)

    # Go through the range and mark affected spots as illumined
    illumined_ranges.add((lower, upper))

# Go through questions and print illumination status
for _ in range(Q):
    spot = int(input())
    if any((lower <= spot <= upper) for (lower, upper) in illumined_ranges):
        print('Y')
    else:
        print('N')
