N = int(input()) # number of spots
L = int(input()) # number of lights
Q = int(input()) # number of spots to be questioned about

# This one uses ranges instead of spots; it makes adding faster,
# but lookups slower.

# Reminder that spots are numbered from 1, not from 0
lower_to_upper = {}
upper_to_lower = {}

# Read the lights
for _ in range(L):
    vals = input().split()
    light_spot, spread = int(vals[0]), int(vals[1])

    # Bound the start and end of the range
    lower = max(0, light_spot - spread)
    upper = min(N, light_spot + spread)

    # Go through the range and mark affected spots as illumined
    lower_to_upper[lower] = max(upper, lower_to_upper.get(lower, upper))
    upper_to_lower[upper] = min(lower, upper_to_lower.get(upper, upper))

lowers = sorted(lower_to_upper)
uppers = sorted(upper_to_lower)

# Go through questions and print illumination status
if not L:
    for _ in range(Q):
        print('N')

else:
    for _ in range(Q):
        spot = int(input())

        if spot < lowers[0]:
            print('N')
        
        box = lowers[0]
        for lower in lowers:
            if spot < lower:
                break
            else:
                box = lower
        
        if box <= spot <= lower_to_upper[box]:
            print('Y')
        else:
            print('N')
