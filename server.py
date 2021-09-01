from flask import Flask, request
from flask_restful import Resource, Api

from tsp import solve_tsp

app = Flask(__name__)
api = Api(app)

class SolveTSP(Resource):
    def get(self):
        result = solve_tsp(request.get_json()["points"])
        return {"shortest_path": result}

api.add_resource(SolveTSP, '/')

if __name__ == '__main__':
    app.run(debug=True)