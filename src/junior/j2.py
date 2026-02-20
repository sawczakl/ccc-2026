# We could do 5 inputs but might as well just put them in a list right away
scores = []
for _ in range(5):
    scores.append(int(input()))

D = int(input()) # difficulty factor

# Python makes this easy...
highest = max(scores)
lowest = min(scores)

# This too. The list.remove method removes exactly one instance
scores.remove(highest)
scores.remove(lowest)

# Sum and multiply by difficulty factor
print(sum(scores) * D)

# Note that the problem is underspecified.
# Suppose all judges gave the same score. Now the highest
# and lowest scores are identical. Do we remove one instance
# or two? Oh well.
