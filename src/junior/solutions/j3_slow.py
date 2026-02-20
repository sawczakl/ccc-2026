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

# Note that in Python, lists are considered True
# as long as they are non-empty
while ngoc and minh:
    candies = (ngoc[0], minh[0])
    results = OUTCOMES[candies]
    
    # Unpack into two variables for clarity
    ngoc_wins, minh_wins = results

    # This slice works in Python; on a list with 1 item,
    # it produces an empty list and so ends the loop.
    # In other languages it would probably raise an error
    if ngoc_wins:
        ngoc_eaten += 1
        minh = minh[1:]
    
    if minh_wins:
        minh_eaten += 1
        ngoc = ngoc[1:]

# When either line runs out, remaining candy is eaten
# by the owner of the line. We can just do both because
# the finished one will be length 0 and have no effect.

ngoc_eaten += len(ngoc)
minh_eaten += len(minh)

print(ngoc_eaten)
print(minh_eaten)
