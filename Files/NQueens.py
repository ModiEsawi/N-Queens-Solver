from random import choice, randrange
from collections import Counter


class NQueensSearch:
    def __init__(self, N):
        self.N = N

    '''
        return random list of n items , each item indicate queen's index
        in it's column
    '''

    def initial(self):
        return list(randrange(self.N) for i in range(self.N))

    def initial_plus(self, initial=50):
        states = [list(randrange(self.N) for i in range(self.N)) for i in range(initial)]
        best =  max(states, key=lambda state: self.heuristic(state))
        h = self.heuristic(best)
        return best


    '''
        given state , returns true if the state is goal state, else false
    '''
    def goal_test(self, state):
        a = set()
        b = set()
        c = set()
        for row, col in enumerate(state):
            if col in a or row - col in b or row + col in c:
                return False
            a.add(col)
            b.add(row - col)
            c.add(row + col)
        return True

    def heuristic(self, state):
        a, b, c = [Counter() for i in range(3)]
        for row, col in enumerate(state):
            a[col] += 1
            b[row - col] += 1
            c[row + col] += 1
        h = 0
        for count in [a, b, c]:
            for key in count:
                h += count[key] * (count[key] - 1) / 2
        return -h


    def nearStates(self, state):
        near_states = []
        for row in range(self.N):
            for col in range(self.N):
                if col != state[row]:  # not in same column
                    temp = list(state)
                    temp[row] = col
                    near_states.append(list(temp))
        return near_states

    def randomNearState(self, state):
        randomRow = randrange(self.N)
        randomCol = randrange(self.N)
        counter = 0
        while counter < 4000:
            if randomCol != state[randomRow]:  # not in same column
                temp = list(state)
                temp[randomRow] = randomCol
                return list(temp)
            counter += 1
        return choice(self.nearStates(state))
