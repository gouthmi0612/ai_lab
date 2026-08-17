from heapq import heappush, heappop

# State representation: (jug1, jug2)
class State:
 def __init__(self, x, y, g, h, parent=None):
 self.x = x # water in jug1
 self.y = y # water in jug2
 self.g = g # cost so far
 self.h = h # heuristic
 self.f = g + h
 self.parent = parent

 def __lt__(self, other):
 return self.f < other.f


# Heuristic: difference from target
def heuristic(x, y, target):
 return min(abs(x - target), abs(y - target))
def get_successors(state, max_x, max_y):
 x, y = state.x, state.y
 successors = []
 # Possible operations
 operations = [
 (max_x, y), # Fill Jug1
 (x, max_y), # Fill Jug2
 (0, y), # Empty Jug1
 (x, 0), # Empty Jug2
 # Pour Jug1 -> Jug2
 (x - min(x, max_y - y), y + min(x, max_y - y)),
 # Pour Jug2 -> Jug1
 (x + min(y, max_x - x), y - min(y, max_x - x))
 ]
 for new_x, new_y in operations:
 successors.append((new_x, new_y))

 return successors


def a_star(max_x, max_y, target):
 open_list = []
 closed_set = set()

 start = State(0, 0, 0, heuristic(0, 0, target))
 heappush(open_list, start)

 while open_list:
 current = heappop(open_list)
 if (current.x, current.y) in closed_set:
 continue
 closed_set.add((current.x, current.y))
 # Goal check
 if current.x == target or current.y == target:
 return current

 for (nx, ny) in get_successors(current, max_x, max_y):
 if (nx, ny) not in closed_set:
 new_state = State(
 nx, ny,
 current.g + 1,
 heuristic(nx, ny, target),
 current
 )
 heappush(open_list, new_state)
 return None
def print_path(state):
 path = []
 while state:
 path.append((state.x, state.y))
 state = state.parent
 path.reverse()

 print("\nSolution Path:")
 for step in path:
 print(step)
# Example
if __name__ == "__main__":
 jug1 = 4
 jug2 = 3
 target = 2
 result = a_star(jug1, jug2, target)
 if result:
 print_path(result)
 else:
 print("No solution found")