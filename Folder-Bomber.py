import subprocess
import time

#subprocess.getoutput("cd desktop")
i = 1
while True:
    i = +1
    subprocess.getoutput(f"mkdir {i}")
    time.sleep(5)