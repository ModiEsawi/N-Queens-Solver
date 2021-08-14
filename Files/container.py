from printBoard import printBoard
from hill_climbing import hill_climbing
from random_restart import random_restart
from simulated_annealing import simulated_annealing
from NQueens import NQueensSearch
from SimpleBackTracking import get_simpleBackTrackingSolver_result
from BranchAndBound import get_BranchAndBound_result
from genetic_algorithm import get_genetic_algorithm_result
from genetic_algorithm import start_genetic_algorithm


def run_hill_climbing(n):
    queen_problem = NQueensSearch(n)
    result = hill_climbing(queen_problem)
    if queen_problem.goal_test(result):
        return result
    else:
        return []


def run_random_restart(n, limit, r,initial=50):
    queen_problem = NQueensSearch(n)
    result = random_restart(queen_problem, limit, r,initial)
    if queen_problem.goal_test(result):
        return result
    else:
        return []


def run_simulated_annealing(n, t):
    queen_problem = NQueensSearch(n)
    result = simulated_annealing(queen_problem, t)
    if queen_problem.goal_test(result):
        return result
    else:
        return []


def run_simpleBackTracking(n):
    result = get_simpleBackTrackingSolver_result(n)
    return result


def run_branchAndBound(n):
    result = get_BranchAndBound_result(n)
    return result


def run_genticAlgorithm(n, populationNum, mutation_probability):
    result = get_genetic_algorithm_result(n, populationNum, mutation_probability)
    return result
