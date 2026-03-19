N = int(input()) # number of spots
L = int(input()) # number of lights
Q = int(input()) # number of spots to be questioned about

# Reminder that spots are numbered from 1, not from 0
# First spot is a dummy (spot 0 will never be asked about)
spots = [0] * (N + 1)

# Read the lights
for _ in range(L):
    spot, spread = (int(v) for v in input().split())

    # Bound the start and end of the range
    lower = max(1, spot - spread)
    upper = min(N, spot + spread)

    # Make the naive sum per the commentary
    spots[lower] += 1
    spots[upper + 1] -= 1

# Make prefix sums
prefix = [0]
for spot in spots[1:]:
    prefix.append(prefix[-1] + spot)

# prefix = prefix[1:]
# Go through questions and print illumination status
for _ in range(Q):
    spot = int(input())
    if prefix[spot]:
        print('Y')
    else:
        print('N')
