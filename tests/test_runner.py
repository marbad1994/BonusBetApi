import sys
from bet_test import bet_one_test, bet_two_test
from log_module import write_log_file, print_log, append_to_log

URL = "http://localhost:5000/bet"
TESTS = [bet_one_test, bet_two_test]
log = "" 

if __name__ == '__main__':
    for test in TESTS:
        result = test(URL)
        print_log(result)
        log = append_to_log(log, result)
    if log == "":
        sys.exit(0)
    else:
        write_log_file(log)
        sys.exit(1)

