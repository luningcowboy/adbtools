import os
import subprocess

def runCMD(cmd):
    return os.system(cmd)

def runCMDWithResult(cmd):
    sub = subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE)
    sub.wait()
    return sub.stdout.read()
