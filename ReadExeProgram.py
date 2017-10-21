import subprocess
import os
from subprocess import Popen, PIPE

#if x == True:
#    command = "ConFire"
#    subprocess.Popen(command)
#    subprocess.check_call(command , shell=True)


p = Popen('ConFire', stdin=PIPE) #NOTE: no shell=True here
p.communicate(os.linesep.join(["input 1", "input 2"]))