def is_goal(s):
    x, y, z = s
    return x == 4 and y == 4

def successors(s):
    x, y, z = s
    successor_states = []

    # Define the pour operation from one bottle to another
    def pour(source, destination):
        nonlocal x, y, z
        state_list = list(s)  # Convert the tuple to a list for modification
        if state_list[source] > 0 and state_list[destination] < destination_capacity[destination]:
            amount_to_pour = min(state_list[source], destination_capacity[destination] - state_list[destination])
            state_list[source] -= amount_to_pour
            state_list[destination] += amount_to_pour
            successor_states.append(tuple(state_list))  # Convert the list back to a tuple

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
