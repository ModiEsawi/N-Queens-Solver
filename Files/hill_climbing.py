def hill_climbing(problem, random_initial=True):
    if random_initial:
        current = problem.initial()
    else:
        current = problem.initial_plus()
    while True:
        neighbours = problem.nearStates(current)
        if not neighbours:
            break
        neighbour = max(neighbours, key=lambda state: problem.heuristic(state))
        if problem.heuristic(neighbour) <= problem.heuristic(current):
            break
        current = neighbour
    return current
