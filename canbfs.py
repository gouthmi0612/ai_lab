from collections import deque

class State:
    def __init__(self, m_left, c_left, boat, m_right, c_right, parent=None):
        self.m_left = m_left
        self.c_left = c_left
        self.boat = boat
        self.m_right = m_right
        self.c_right = c_right
        self.parent = parent

    def is_goal(self):
        return (self.m_left == 0 and self.c_left == 0 and
                self.m_right == 3 and self.c_right == 3)

    def is_valid(self):
        if (self.m_left < 0 or self.c_left < 0 or
            self.m_right < 0 or self.c_right < 0):
            return False

        if (self.m_left > 3 or self.c_left > 3 or
            self.m_right > 3 or self.c_right > 3):
            return False

        if self.m_left > 0 and self.c_left > self.m_left:
            return False

        if self.m_right > 0 and self.c_right > self.m_right:
            return False

        return True

    def successors(self):
        moves = [
            (2, 0),
            (0, 2),
            (1, 1),
            (1, 0),
            (0, 1)
        ]

        children = []

        for m, c in moves:
            if self.boat == 'L':
                new_state = State(
                    self.m_left - m,
                    self.c_left - c,
                    'R',
                    self.m_right + m,
                    self.c_right + c,
                    self
                )
            else:
                new_state = State(
                    self.m_left + m,
                    self.c_left + c,
                    'L',
                    self.m_right - m,
                    self.c_right - c,
                    self
                )

            if new_state.is_valid():
                children.append(new_state)

        return children

    def __eq__(self, other):
        return (self.m_left == other.m_left and
                self.c_left == other.c_left and
                self.boat == other.boat and
                self.m_right == other.m_right and
                self.c_right == other.c_right)

    def __hash__(self):
        return hash((self.m_left, self.c_left,
                     self.boat, self.m_right, self.c_right))

    def __str__(self):
        return (f"Left(M={self.m_left}, C={self.c_left}) "
                f"Boat={self.boat} "
                f"Right(M={self.m_right}, C={self.c_right})")


def bfs():
    start = State(3, 3, 'L', 0, 0)
    queue = deque([start])
    visited = set()

    while queue:
        current = queue.popleft()

        if current.is_goal():
            return current

        visited.add(current)

        for child in current.successors():
            if child not in visited and child not in queue:
                queue.append(child)

    return None


def print_solution(goal):
    path = []

    while goal:
        path.append(goal)
        goal = goal.parent

    path.reverse()

    print("\nSolution Steps:\n")

    for i, state in enumerate(path):
        print(f"Step {i}: {state}")


goal = bfs()

if goal:
    print_solution(goal)
else:
    print("No solution found.")