from math import gcd

N = int(input())
vals = input()
cards = [int(v) for v in vals.split()]

# This first attempt won't deal with the last subtask, the -1 case.

# The first thought that occurs to me is that this is not a matter
# of trying to find all possible ways to make sums, which would be
# impossible at 10^5 in the time constraints. But we don't have to,
# because we can leave as many cards as we want on the table.
# All we have to do is try to add cards until we have a common divisor,
# especially since we can print any valid solution at the end.
# So we have to find the quickest way to identify whether a card
# is helping us to make a divisor or not. The difficulty is that
# it seems to me that we don't know that one card at a time.
# Also, the NO case still might require checking every sum...

# The description of the final subtask indicates that you can
# be sure whether there is a winning pair of combinations in under 100
# guesses, even when N = 10^5. I'm not sure how that's possible, yet.

# Abandoned attempt below:

# Could try a heuristic approach, changing strategy depending on
# the cards, and hope to eventually land on a general-purpose one.

def strategy_1():
    """
    If any two cards already have a GCD, pick them up :)
    """
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if gcd(cards[i], cards[j]) > 1:
                return [i + 1], [j + 1]
            
def strategy_2():
    """
    Count up through divisors (2+).
    """

strategies = [
    strategy_1
]

def run():
    for s in strategies:
        result = s()
        if result:
            a, b = result

            print('YES')
            print(f'{len(a)} {len(b)}')
            print(' '.join(map(str, a)))
            print(' '.join(map(str, b)))

            return

    else:
        print('NO')

run()
