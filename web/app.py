from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from bet import bet_one, bet_two, safe_bet_one, safe_bet_two

app = Flask(__name__)
api = Api(app)

class Bet(Resource):
    def post(self):
        json_res = request.get_json()
        one = json_res["1"]
        cross = json_res["X"]
        two = json_res["2"]
        bonus = json_res["bonus"]

        one = float(one)
        cross = float(cross)
        two = float(two)
        bonus = int(bonus)
        if one < two:
            ret_json = bet_one(one, cross, two, bonus)
        else:
            ret_json = bet_two(one, cross, two, bonus)

        return jsonify(ret_json)

class SafeBet(Resource):
    def post(self):
        json_res = request.get_json()
        one = json_res["1"]
        cross = json_res["X"]
        two = json_res["2"]
        bonus = json_res["bonus"]

        one = float(one)
        cross = float(cross)
        two = float(two)
        bonus = int(bonus)
        if one < two:
            ret_json = safe_bet_one(one, cross, two, bonus)
        else:
            ret_json = safe_bet_two(one, cross, two, bonus)

        return jsonify(ret_json)

api.add_resource(Bet, "/bet")
api.add_resource(SafeBet, "/safebet")

if __name__ == "__main__":
    app.run(host="0.0.0.0")