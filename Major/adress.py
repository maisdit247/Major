import socket
import urllib.request
from bs4 import BeautifulSoup as bs

# pour observer toute connection sur notre local MAX 255
for ping in range(1, 255):
    address = "192.168.1." + str(ping)
    socket.setdefaulttimeout(1)

    try:
        hostname, alias, addresslist = socket.gethostbyaddr(address)
    except socket.herror:
        hostname = None
        alias = None
        addresslist = address

    if hostname != None:
        print(addresslist, "=>", hostname)

# trouver son Ip localhost
ip = socket.gethostbyname(socket.gethostname())
print("LocalHost ", ip)

# trouver ip FAI
page = urllib.request.urlopen("https://ipinfo.io/")
soup = bs(page, "html.parser")
print(soup)

# trouver ip client sur net
use = input("=>")
print(socket.gethostbyaddr(use), use, sep="\t")
