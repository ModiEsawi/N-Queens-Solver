from flask import Flask
from flask_restful import Resource, Api, reqparse
from container import run_hill_climbing
from container import run_random_restart
from container import run_simulated_annealing
from container import run_simpleBackTracking
from container import run_branchAndBound
from container import run_genticAlgorithm
from flask_cors import CORS

import ast


app = Flask(__name__)
api = Api(app)
CORS(app)


class hill_climbing_endpoint(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('n', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        n = args['n']
        result = run_hill_climbing(int(n))
        return {'data' : result}


class random_restart_endpoint(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('n', required=True)  # add args
        parser.add_argument('limit', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        n = args['n']
        limit = args['limit']
        result = run_random_restart(int(n),int(limit),True)
        return {'data': result}

class random_restart_plus_endpoint(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('n', required=True)  # add args
        parser.add_argument('limit', required=True)  # add args
        parser.add_argument('initial', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        n = args['n']
        limit = args['limit']
        initial = args['initial']
        result = run_random_restart(int(n),int(limit),False,int(initial))
        return {'data': result}


class simulated_annealing_endpoint(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('n', required=True)  # add args
        parser.add_argument('limit', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        n = args['n']
        limit = args['limit']
        result = run_simulated_annealing(int(n),int(limit))
        return {'data': result}


class simpleBackTracking_endpoint(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('n', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        n = args['n']
        result = run_simpleBackTracking(int(n))
        return {'data' : result}

class branchAndBound_endpoint(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('n', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        n = args['n']
        result = run_branchAndBound(int(n))
        return {'data' : result}

class genetic_algorithm_endpoint(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('n', required=True)  # add args
        parser.add_argument('populationSize', required=True)  # add args
        parser.add_argument('mutationProb', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        n = args['n']
        pop = int(args['populationSize'])
        mut = float(args['mutationProb'])
        result = run_genticAlgorithm(int(n),pop,mut)
        return {'data': result}



api.add_resource(hill_climbing_endpoint, '/hillclimbing')
api.add_resource(random_restart_endpoint, '/randomrestart')
api.add_resource(random_restart_plus_endpoint, '/randomrestartplus')
api.add_resource(simulated_annealing_endpoint, '/simulatedannealing')
api.add_resource(simpleBackTracking_endpoint, '/simplebacktracking')
api.add_resource(branchAndBound_endpoint, '/branchandbound')
api.add_resource(genetic_algorithm_endpoint, '/genetic')

if __name__ == '__main__':
    app.run(port= 5000)