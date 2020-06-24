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

example : url --> http://example.com/test.php?file=

results: http://example.com/test.php?file=a
b
c
d
e
vb.

"""
import requests
url = raw_input("url --> ")
file = raw_input("data list ---> ")
code = input("status code ----> ")
fo = open(file,"r+")
for i in fo.readlines():
    r = requests.get(url+i)
    if r.status_code == code:
       print ("found "+i)
    else:
       print ("not found "+i)
