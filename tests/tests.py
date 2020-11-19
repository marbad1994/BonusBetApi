import requests
import datetime
import sys

def bet_one_test():
    url = "http://ec2-18-225-6-54.us-east-2.compute.amazonaws.com:5000/bet"
    url = "http://172.31.16.204:5000/bet"
    data = {"1": 1.5, "X": 3.5, "2": 8, "bonus": 500}
    response = requests.post(url, json=data).json()
    test_data = {'bonus': 500.0,
                 'crossBet': 500.0, 
                 'oneBet': 2500, 
                 'twoBet': 500, 
                 'winningsOnCross': 0.0, 
                 'winningsOnOne': 250.0, 
                 'winningsOnTwo': 500.0
                }
    if response == test_data:
        sys.exit(0)
    else:
        print("Response:")
        print(response)
        print("Test data:")
        print(test_data)
        with open("/opt/TEST/tests/log/log_" + str(datetime.datetime.now()), "w") as f:
            f.write("Response:\n" + str(response) + "\nTest data:\n" + str(test_data))
        sys.exit(1)

if __name__ == '__main__':
    bet_one_test()
