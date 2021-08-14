import random
import math
import sys


def exp_schedule(k=4, alpha=0.001, limit=100000):
    return lambda t: (k * math.exp(-alpha * t) if t < limit else 0)


def simulated_annealing(problem, t):
    schedule = exp_schedule(limit=t)
    current = problem.initial()
    current_h = problem.heuristic(current)
    for t in range(sys.maxsize):
        T = schedule(t)
        if T == 0 or problem.goal_test(current):
            return current
        neighbour = problem.randomNearState(current)
        if not neighbour:
            return current
        new_h = problem.heuristic(neighbour)
        delta_e = new_h - current_h
        if delta_e > 0 or math.exp(delta_e / T) > random.uniform(0.0, 1.0):
            current = neighbour
            current_h = new_h
