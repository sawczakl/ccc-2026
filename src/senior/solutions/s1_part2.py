A = int(input()) # starting pad
B = int(input()) # ending pad
K = int(input()) # giant hop size
T = int(input()) # nth-smallest number of hops sought (1 or 2)

# OK, now let's return here and do the second-fewest ("runner-up").

# First of all, we have an upper bound on the runner-up of optimal + 2.
# This is because we can do -1 +1 ("flip-flop") followed by the optimal.
# So we only need to consider cases where the runner-up is optimal + 1.

# This could happen if:
# (1) Optimal involves overhopping, but baby hops would have been
#     only 1 more than optimal.
# (2) Optimal does not involve overhopping, but overhopping would have been
#     only 1 more than optimal.

# Example cases:
# D = 3. K = 4. Optimal (overhop) 2. Babyhop 3. Flip-flop 4. Runner-up: Babyhop.
# D = 5. K = 6. Optimal (overhop) 2. Babyhop 5. Flip-flop 4. Runner-up: Flip-flop.
# D = 3. K = 6. Optimal (babyhop) 3. Overhop 4. Flip-flop 5. Runner-up: Overhop.
# D = 3. K = 8. Optimal (babyhop) 3. Overhop 6. Flip-flop 5. Runner-up: Flip-flop.

# It seems to me that the easiest way to do this is probably to get to our decision
# point about overhop vs. baby; try both; add 2 to the optimal one; sort; and return
# either the lowest or second-lowest depending on T.

# This part is the same -- approaching our decision point
D = abs(B - A)
n = D // K
D = D % K

# Create options
overhop = n + 1 + (K - D)
babyhop = n + D
options = [overhop, babyhop]

# Create flip-flop option
options.append(min(options) + 2)

# Sort and pick the T-th one
# (Note: T is 1-based, so subtract 1 to make it 0-based as an index...)
options.sort()
n = options[T - 1]

print(n)
