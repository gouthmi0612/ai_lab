import random

# Distance matrix
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = ['A', 'B', 'C', 'D']


# Calculate total distance
def calculate_distance(route):
    total = 0

    for i in range(len(route) - 1):
        total += distance[route[i]][route[i + 1]]

    # Return to starting city
    total += distance[route[-1]][route[0]]

    return total


# Generate neighboring route
def generate_neighbor(route):
    neighbor = route.copy()

    i, j = random.sample(range(len(route)), 2)

    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

    return neighbor


# Hill Climbing Algorithm
def hill_climbing():
    current_route = list(range(len(cities)))
    random.shuffle(current_route)

    current_distance = calculate_distance(current_route)

    while True:
        neighbor_route = generate_neighbor(current_route)
        neighbor_distance = calculate_distance(neighbor_route)

        # Move to better solution
        if neighbor_distance < current_distance:
            current_route = neighbor_route
            current_distance = neighbor_distance
        else:
            break

    return current_route, current_distance


# Execute the algorithm
best_route, best_distance = hill_climbing()

print("Best Route:")

for city in best_route:
    print(cities[city], end=" -> ")

print(cities[best_route[0]])

print("Minimum Distance:", best_distance)