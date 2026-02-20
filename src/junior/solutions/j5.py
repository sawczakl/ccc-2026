N = int(input()) # number of spots
L = int(input()) # number of lights
Q = int(input()) # number of spots to be questioned about

# Reminder that spots are numbered from 1, not from 0
illumined_spots = set()

# Read the lights
for _ in range(L):
    vals = input().split()
    light_spot, spread = int(vals[0]), int(vals[1])

    # Bound the start and end of the range
    lower = max(0, light_spot - spread)
    upper = min(N, light_spot + spread)

    # Go through the range and mark affected spots as illumined
    for spot in range(lower, upper + 1):
        illumined_spots.add(spot)

# Go through questions and print illumination status
for _ in range(Q):
    spot = int(input())
    if spot in illumined_spots:
        print('Y')
    else:
        print('N')
