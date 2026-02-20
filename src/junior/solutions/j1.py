B = int(input()) # Besa's desired tickets
T = int(input()) # Total available tickets
P = int(input()) # Tickets already purchased

# Since we need the remaining for the 'yes' case,
# we might as well subtract anyway and base our
# check on it being less than 0
remaining = T - P - B

# 0 or more = there were enough for her
if remaining < 0:
    print('N')
else:
    print(f'Y {remaining}')
