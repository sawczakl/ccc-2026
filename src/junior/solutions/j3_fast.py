# This is the fast version.
# The thing that will make the other one slow
# when the parties have "an absurd amount of candy"
# is that removing the first eelemenet of the string
# means re-indexing all remaining elements, which is slow.
# Instead, we'll use indices to keep track of our position
# in the two candy lines, rather than actually changing size.

ngoc = input() # Ngoc's candy as a string
minh = input() # Minh's candy as a string
# Start of the string = first candy to be eaten

# Track their candy
ngoc_eaten = 0
minh_eaten = 0

# The outcomes would be hard to do elegantly.
# The standard approach would involve a ton of if statements.
# Not impossible or even hard, just ugly...
# I prefer a table of outcomes that we can just look up

# This table maps (N candy, M candy) to (N wins, M wins)
OUTCOMES = {
    # Ties = both win
    ('R', 'R'): (True, True),
    ('G', 'G'): (True, True),
    ('B', 'B'): (True, True),

    # R > G     G > B       B > R
    ('R', 'G'): (True, False),
    ('R', 'B'): (False, True),

    ('G', 'R'): (False, True),
    ('G', 'B'): (True, False),

    ('B', 'R'): (True, False),
    ('B', 'G'): (False, True),
}

# Indices for positions
i_ngoc = 0
i_minh = 0

# Use index < len to check end now
# We will also use indices to get the candies
while (i_ngoc < len(ngoc)) and (i_minh < len(minh)):
    candies = (ngoc[i_ngoc], minh[i_minh])
    results = OUTCOMES[candies]
    
    # Unpack into two variables for clarity
    ngoc_wins, minh_wins = results

    # Here we increment the indices rather than slice
    if ngoc_wins:
        ngoc_eaten += 1
        i_minh += 1
    
    if minh_wins:
        minh_eaten += 1
        i_ngoc += 1

# When either line runs out, remaining candy is eaten
# by the owner of the line. Since the length of the lists
# has not changed, we have to subtract the indices

ngoc_eaten += len(ngoc) - i_ngoc
minh_eaten += len(minh) - i_minh

print(ngoc_eaten)
print(minh_eaten)
