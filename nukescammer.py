import requests
import random
import string
import linecache

n=0
authurl = 'https://betxmax.com/auth.php'

while True:
    n = n+1
   
    username=linecache.getline('./fakeinfo/username.txt', int(random.randint(1, 10000)))
    password=linecache.getline('./fakeinfo/password.txt', int(random.randint(1, 10000)))
    name=linecache.getline('./fakeinfo/name.txt', int(random.randint(1, 10000)))
    ccnum=linecache.getline('./fakeinfo/ccnum.txt', int(random.randint(1, 10000)))
    expiration=linecache.getline('./fakeinfo/expiration.txt', int(random.randint(1, 10000)))
    address=linecache.getline('./fakeinfo/address.txt', int(random.randint(1, 10000)))

    requests.post(authurl, allow_redirects=False, data={
        'login': username, 
        'password': password
        
    })

    print(f"Sent: {n}")
