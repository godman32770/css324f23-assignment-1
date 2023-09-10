def initial_state():
    return (8, 0, 0)

def is_goal(s):
    a, b, c = s
    return a == 4 and b == 4

def successors(s):
    a, b, c = s
    successor_states = []
    def pour(source, destination):
        nonlocal a, b, c
        if s[source] > 0 and s[destination] < destination_capacity[destination]:
            amount_to_pour = min(s[source], destination_capacity[destination] - s[destination])
            s[source] -= amount_to_pour
            s[destination] += amount_to_pour
            successor_states.append(tuple(s))

    # Define the capacities of the bottles
    destination_capacity = [8, 5, 3]

    # Generate all possible pour operations
    pour(0, 1)  # Pour from the 8-liter bottle to the 5-liter bottle
    pour(0, 2)  # Pour from the 8-liter bottle to the 3-liter bottle
    pour(1, 0)  # Pour from the 5-liter bottle to the 8-liter bottle
    pour(1, 2)  # Pour from the 5-liter bottle to the 3-liter bottle
    pour(2, 0)  # Pour from the 3-liter bottle to the 8-liter bottle
    pour(2, 1)  # Pour from the 3-liter bottle to the 5-liter bottle

    return successor_states

# Test the functions
initial = initial_state()
print("Initial state:", initial)
print("Is goal state:", is_goal(initial))
print("Successor states:", successors(initial))





