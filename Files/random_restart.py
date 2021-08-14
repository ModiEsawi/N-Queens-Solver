from hill_climbing import hill_climbing


def random_restart(problem, limit, random_initial,initial =50):
    if random_initial :
        state = problem.initial()
    else:
        state = problem.initial_plus(initial)
    count = 0
    while not problem.goal_test(state) and count < limit:
        state = hill_climbing(problem, random_initial)
        count += 1
    return state
