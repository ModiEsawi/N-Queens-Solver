from printBoard import printBoard
from hill_climbing import hill_climbing
from random_restart import random_restart
from simulated_annealing import simulated_annealing
from NQueens import NQueensSearch
from genetic_algorithm import start_genetic_algorithm
from genetic_algorithm import  get_genetic_algorithm_result
from time import time


def run_hill_climbing(n):
    queen_problem = NQueensSearch(n)
    #print("Hill Climbing: ")
    start = time()
    result = hill_climbing(queen_problem)
    if queen_problem.goal_test(result):
        #print("Run time: " + str(time() - start))
        return result
        pass
    else:
        #print("Run time: " + str(time() - start))
        return []
        pass


def run_random_restart(n, limit, r):
    queen_problem = NQueensSearch(n)
    print("Random Restart Hill Climbing: ")
    start = time()
    result = random_restart(queen_problem, limit, r)
    if queen_problem.goal_test(result):
        print("Run time: " + str(time() - start))
        return result
    else:
        print("Run time: " + str(time() - start))
        return []


def run_simulated_annealing(n, t):
    queen_problem = NQueensSearch(n)
    print("simulated annealing: ")
    start = time()
    result = simulated_annealing(queen_problem, t)
    if queen_problem.goal_test(result):
        print("Run time: " + str(time() - start))
        return result
    else:
        print("Run time: " + str(time() - start))
        return []


def run_genetic_algorithm(n, populationNum, mutation_probability):
    print("genetic algorithm")
    start = time()
    start_genetic_algorithm(n, populationNum, mutation_probability)
    print("Run time: " + str(time() - start))


if __name__ == "__main__":
    # n = 30
    # hill_climbing_result = run_hill_climbing(n)
    # printBoard(hill_climbing_result)
    #random_restart_limit = 100000
    #for n in [40] :
    #    for i in range(3):
    #        print ("-------- n "+ str(n) + "-----------")
    #        print("START iteration " + str(i+1))

    #        print("Random Plus")
    #        random_restart_result = run_random_restart(n, random_restart_limit, False)
    #        printBoard(random_restart_result)

    #        print("Random")
    #        random_restart_result = run_random_restart(n, random_restart_limit, True)
    #        printBoard(random_restart_result)

    #random_restart_limit = 100000
    #simulated_annealing_t = 9000000
    #for n in [5, 8, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70]:
    #    print("-------- n " + str(n) + "-----------")
    #    for i in range(3):
            #print("START iteration " + str(i+1))
            #simulated_annealing_result = run_simulated_annealing(n, simulated_annealing_t)
            #printBoard(simulated_annealing_result)

    #        print("Random Plus")
    #        random_restart_result = run_random_restart(n, random_restart_limit, False)
    #        printBoard(random_restart_result)

    #simulated_annealing_t = 9000000
    #simulated_annealing = run_simulated_annealing(5, simulated_annealing_t)
    #printBoard(simulated_annealing)




    popula= 100
    for prop in [0.1,0.2,0.4,0.5,0.7,0.9]:
        for n in [5,6,7,8,9]:
            for iteration in range(1):
                print(" n : "+str(n) +" -----" + "mutatuin : " + str(prop))
                get_genetic_algorithm_result(n, popula, prop)

    #for n in [30]:
    #    cc = 0
    #    times = []
    #    for i in range(1000):
    #        start = time()
    #        rr = run_hill_climbing(n)
    #        if rr != []:
    #            cc += 1
    #            times.append(time() - start)
    #    if(len(times) == 0):
    #        avgtimes = 9999
    #    else:
    #        avgtimes = sum(times)/len(times)
    #    print("n :"+str(n) + " counter = "+str(cc) + "  prop:" +str(cc/1000)+" average times" + str(avgtimes))