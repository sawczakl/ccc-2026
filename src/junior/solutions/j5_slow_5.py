N = int(input()) # number of spots
L = int(input()) # number of lights
Q = int(input()) # number of spots to be questioned about

# Reminder that spots are numbered from 1, not from 0
# First spot is a dummy (spot 0 will never be asked about)
spots = '_' + ('N' * N)

spots = ['_'] + ([False] * N)

inserts = {}

# Read the lights
for _ in range(L):
    vals = input().split()
    light_spot, spread = int(vals[0]), int(vals[1])

    # Bound the start and end of the range
    lower = max(1, light_spot - spread)
    upper = min(N, light_spot + spread)

    n = (upper - lower) + 1
    
    insert = inserts.setdefault(n, ([True] * n))
        
    spots[lower:lower + n] = insert

spots = tuple(('Y' if item else 'N') for item in spots)

# Go through questions and print illumination status
for _ in range(Q):
    spot = int(input())
    print(spots[spot])

"""
Example of the string interpolation:

10 spots, 3 lights

start

0123456789A
_NNNNNNNNNN

8 0     lower 8 upper 8 n 1 = splice [:8] + 'Y' + [9:]

0123456789A
_NNNNNNNYNN

1 1     lower 1 upper 2 n 2 = splice [:1] + 'YY' + [3:]

0123456789A
_YYNNNNNYNN

4 2     lower 2 upper 6 n 5 = splice [:2] + 'YYYYY' + [7:]

0123456789A
_YYYYYYNYNN
"""