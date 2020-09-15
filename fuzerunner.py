import sys
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.MAGENTA)
print(Style.BRIGHT)
print """coded by sm1l3
:'######::'##::::'##::::'##:::'##::::::::'#######::
'##... ##: ###::'###::'####::: ##:::::::'##.... ##:
 ##:::..:: ####'####::.. ##::: ##:::::::..::::: ##:
. ######:: ## ### ##:::: ##::: ##::::::::'#######::
:..... ##: ##. #: ##:::: ##::: ##::::::::...... ##:
'##::: ##: ##:.:: ##:::: ##::: ##:::::::'##:::: ##:
. ######:: ##:::: ##::'######: ########:. #######::
:......:::..:::::..:::......::........:::.......:::



this is url fuzzer



results: http://example.com/test.php?file=a
b
c
d
e
vb.


--thread 10 = [10 saniye aralik ile test eder]
--proxy list.txt = [proxy listesi aktarir]
--out log.txt = [bulunanlari kayit eder]
--site http://example.com/test.php?file= = [hedef siteyi belirler]
--wordlist wlist.txt = [wordlist belirler]
"""
import getopt

import requests

print(Fore.RED)
print(Style.BRIGHT)


argv= sys.argv[1:] 
options, args = getopt.getopt(argv, "f:l:",["thread=","out=","proxy=","wordlist=","site="])

for name , value in options:
        if name in ['--wordlist']:
            wordlist = value
        
        if name in ['--site']:
            site=value
 
       
        if name in ['--thread']:
            thread = float(value)

            
        

        if name in ['--out']:
            out = value
            
        
        if name in ['--proxy']:
            proxy = value

dos  = open(out, "w+")
fo = open(wordlist,"r+")
url = site
for i in fo.readlines():
    
            
    pl = open(proxy,"r")
    for pf in pl.readlines():
        s = requests.Session()
        s.proxies = {"http": pf}
        print (Fore.GREEN)
        print (Style.BRIGHT)
           
    
    r = requests.get(url+i)
    
    time.sleep(thread)
    
    st = str(i)
    stv = str(r.status_code)
    stri = st+stv
     
    dos.writelines("%s\n" % stri)
    
    
    print (i,+r.status_code)
        
    
    
dos.close()
