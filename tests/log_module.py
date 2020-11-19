from datetime import datetime

def print_log(msg):
    print(msg)

def append_to_log(log, msg):
    log += msg
    return log
    

def write_log_file(log):
    log_path = "/opt/log/"
    log_date = str(datetime.now()).replace(" ", "-")
    log_filename = log_path + "log-" + log_date
    with open(log_filename, "w") as log_file:
        log_file.write(log)

