import sys
import requests
from bet_test import bet_one_test, bet_two_test
from log_module import write_log_file, print_log, append_to_log

url = "http://" + requests.get("http://169.254.169.254/latest/meta-data/public-hostname").text + ":5000/bet"

TESTS = [bet_one_test, bet_two_test]
log = "" 

if __name__ == '__main__':
    for test in TESTS:
        result = test(url)
        print_log(result)
        log = append_to_log(log, result)
    if log == "":
        sys.exit(0)
    else:
        write_log_file(log)
        sys.exit(1)

