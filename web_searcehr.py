# start the coding web searcher for find (admin page , login page and more ...) with python3.9
# imoprt library`s :
import requests
import subprocess
from colorama import Fore,init
# colorama 
init()
# step 2 ( define search address`s)
search = ['robots.txt',
'search/',
'admin/',
'login/',
'user/login/',
'profiles/',
'scripts/',
'install.php',
'log.txt',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'user/password/',
'xmlrpc.php'
]
# step 3 (input for conenction to web)
url = input(Fore.LIGHTMAGENTA_EX+" [*] "+Fore.WHITE+" Enter URL for Search : ")
# step 4 ( define loop for testing ... )
for page in search:
    req = requests.get("https://"+url+"/"+page)
    if req.status_code == 200:
	    print(Fore.GREEN+" [+]"+Fore.WHITE+" Found Page "+url+"/"+page)
    else:
	    print(Fore.RED+" [-] "+Fore.WHITE+"Not Found "+url+"/"+page)
