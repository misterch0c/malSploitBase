#### Rovnix


Type: Hash Collision

Author: [Xylitol](https://twitter.com/Xylit0l)

```
<?php
        /**
         * Defeat the weak hash function of Rovnix
         * to get password from a hash.
         */

        $HASH   = 'fbff791ef0770855e599ea6f87d41653';

        $value  = getNumber($HASH);
        $search = search($value, $HASH);

        echo('Hash:   ' . $HASH  . '<br />');
        echo('Value:  ' . $value . '<br />');
        echo('Search: ' . $search);

        // Search an working (number) password
        function search($value, $hash) {
                $i = 0;

                while (true) {
                        if (getHash($i) == $value)
                                return $i;

                        $i++;
                }
        }

        // Get the hashed number
        function getNumber($hash) {
                $i = 0;

                while (true) {
                        if (md5($i) == $hash)
                                return $i;

                        $i++;
                }
        }

        // Hash function without final MD5 (return only numbers)
        function getHash($hash) {
                $salt = 'LKJFDJLJkkljKJKJKJkjkj$i%&@(%jkjJn@@j$r@!cdh*!@#$djl1J$r!j@o*$@duJxlJLEKJkJFKJEJ2$jkeJFJLEJFE';

                return $hash + $salt + md5($salt) + md5($hash) + $salt[3];
        }
?>
```
