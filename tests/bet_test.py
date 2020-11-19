import requests

BORDER = "\n======================================\n"


def bet_one_test(url):
    data = {"1": 1.5, "X": 3.5, "2": 8, "bonus": 500}
    response = requests.post(url, json=data).json()
    test_data = {'bonus': 500.0,
                 'crossBet': 500.0,
                 'oneBet': 1500, 
                 'twoBet': 500,
                 'winningsOnCross': 0.0,
                 'winningsOnOne': 250.0,
                 'winningsOnTwo': 500.0
                }
    if response != test_data:
        msg = "Running Bet One Test\n"
        msg += "Response:\n" + str(response) + "\nTest data:\n" + str(test_data)
        msg += BORDER
        return msg
    else:
        return ""

def bet_two_test(url):
    data = {"1": 8, "X": 3.5, "2": 1.5, "bonus": 500}
    response = requests.post(url, json=data).json()
    test_data = {'bonus': 500.0,
                 'crossBet': 500.0,
                 'oneBet': 500,
                 'twoBet': 2500,
                 'winningsOnCross': 0.0,
                 'winningsOnOne': 500.0,
                 'winningsOnTwo': 250.0
                }
    if response != test_data:
        msg = "Running Bet Two Test\n"
        msg += "Response:\n" + str(response) + "\nTest data:\n" + str(test_data)
        msg += BORDER
        return msg
    else:
        return ""

