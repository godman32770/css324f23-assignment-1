def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    actions = []
    a, b, c = s

    # Pour from the 8-liter bottle to the 5-liter bottle
    if a > 0 and b < 5:
        amount = min(a, 5 - b)
        actions.append(((a - amount, b + amount, c), amount))

    # Pour from the 8-liter bottle to the 3-liter bottle
    if a > 0 and c < 3:
        amount = min(a, 3 - c)
        actions.append(((a - amount, b, c + amount), amount))

    # Pour from the 5-liter bottle to the 8-liter bottle
    if b > 0 and a < 8:
        amount = min(b, 8 - a)
        actions.append(((a + amount, b - amount, c), amount))

    # Pour from the 5-liter bottle to the 3-liter bottle
    if b > 0 and c < 3:
        amount = min(b, 3 - c)
        actions.append(((a, b - amount, c + amount), amount))

    # Pour from the 3-liter bottle to the 8-liter bottle
    if c > 0 and a < 8:
        amount = min(c, 8 - a)
        actions.append(((a + amount, b, c - amount), amount))

    # Pour from the 3-liter bottle to the 5-liter bottle
    if c > 0 and b < 5:
        amount = min(c, 5 - b)
        actions.append(((a, b + amount, c - amount), amount))

    return actions  
