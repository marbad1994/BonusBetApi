from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
from bet import bet_one, bet_two, safe_bet_one, safe_bet_two

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)
URL = "http://" + requests.get("http://169.254.169.254/latest/meta-data/public-hostname").text
CORS(app, origins=URL, allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"], support_credentials=True)


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
        response = jsonify(ret_json)
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Credentials", "true")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Origin, Content-Type, Accept")


        return response


api.add_resource(Bet, "/bet")
api.add_resource(SafeBet, "/safebet")

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port="5000", debug=True)
