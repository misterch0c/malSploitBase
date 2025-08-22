


Type: SQL injection

Vuln: http://localhost/download.php?file=global.php

Author:  [Bilal KARDADOU](https://www.linkedin.com/in/kardadou/)

```
################################################
#Title: AZORult Stealer v2 Botnet - SQL injection
#Credit: Bilal KARDADOU
#URL: https://www.rekings.com/shop/azorult-stealer/
#Product: 'AZORult Stealer v2 Botnet'
#Type: Paid
#Google Dork: N/A
################################################
#
#  Description:
#   Stealer of stored passwords, cookies, autocomplete from browsers:
#   Google Chrome, Mozilla Firefox, Internet Explorer, Microsoft Edge,
YandexBrowser, Opera, InternetMailRu, ComodoDragon, Amigo, Bromium,
Chromium, 360Browser, Nichrome, RockMelt, #  Vivaldi,GoBrowser, Sputnik,
Kometa, Uran, QIPSurf, Epic, Brave, CocCoc, CentBrowser, 7Star,
ElementsBrowser, TorBro, Suhba, SaferBrowser, Mustangm Superbird, Chedot,
Torch, Waterfox, Cyberfox, Comodo IceDragon, PaleMoon
#   (Cookies in Netscape format, in the admin panel they are converted into
JSON)
#
#   Stealer of stored passwords:
#   Outlook, Thunderbird, Filezilla, WinSCP
#   Pidgin, PSI, PSI Plus, Skype, Telegram
#   Steam ( ssfn + vdf)
#   Anoncoin, Armory, BBQcoin, Bitcoin Core, Bytecoin, Craftcoin, DashCoin,
Devcoin, Digitalcoin, Electrum, Fastcoin, Feathercoin, Florincoin, Franko,
Freicoin, GoldCoin, IoCoin, Litecoin, Mincoin, Monero, MultiBit, namecoin,
NovaCoin, Phoenixcoin, PPCoin, primecoin, ProtoShares, Quarkcoin, Tagcoin,
Terracoin, Worldcoin, Yacoin, Zetacoin
#
# --Method=GET -p [search]
#
#  -u "
http://127.0.0.1/index.php?status=0&datefrom=&dateup=&search=a[SQLI]&cookiesearch=&page=reports
"
#
#  PoC:
#  https://prnt.sc/kp4otu
#
# Bilal KARDADOU - https://www.linkedin.com/in/kardadou/)
################################################
```

