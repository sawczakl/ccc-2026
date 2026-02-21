A = int(input()) # starting pad
B = int(input()) # ending pad
K = int(input()) # giant hop size
T = int(input()) # nth-smallest number of hops sought (1 or 2)

# Consider that we always have 4 possible hops: +K, +1, -K, -1.
# Let's think about when we would want each one.

# First, for simplicity, note that the question as stated could involve
# hopping in either direction since B could be < A. However, we will just
# track from 0 to D (distance) instead in order to avoid flipping signs
# all the time. Given this...

# +K seems like intuitively the best, at least until it overshoots.
# Presumably, our algorithm should start with +K until it would overshoot.
# However, it can still be optimal when overshooting, as long as it does
# not overshoot by more than the # of -1 hops. For example, if K = 5
# and D = 4, the best strategy is +K -1. But if K = 5 and D = 2,
# the best strategy is +1 +1. Thus, use +K until ((K - D) < D).
# (When ((K - D) == D), the strategies are equivalent.)

# +1 should obviously only be used to close a gap smaller than K.

# -1 should obviously only be used if we overshot using K.

# -K should never be used. We would never be that far on the "wrong side"
# of our target unless we had already made suboptimal moves.

# This should be pretty easy to code, but we'll have to come back and think
# about the second-fewest hops aspect.

D = abs(B - A)

# Note that no loop is needed. We can just do math.
# Example: K = 3, D = 10. After this operation, n = 3, D = 1.
n = D // K # The number of +Ks to approach K range
D = D % K # The number of steps left after n giant hops

# Overhop advantageous?
if (K - D) < D:
    n += 1 + (K - D) # the 1 extra is for the K hop itself

# Otherwise, just do +1 till the target is reached
else:    
    n += D

print(n)
