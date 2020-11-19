import subprocess

p1 = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "5000"], stdin=p1.stdout,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

p1.stdout.close()
out, err = p2.communicate()
output = str(out, "utf-8").split("\n")

for o in output:
    if "docker" in o:
        pid = list(filter(("").__ne__, o.split(" ")))[1]


        subprocess.run(["kill", "-9", pid])
