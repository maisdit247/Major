import os
import socket

# WIFI
# voir toutes les connections avec ce mon PC
ip_con = os.popen("nmcli device show").read()
print("Toute les ports de connection connue avec ce pc : \n", ip_con, "\n")

# voir ip box
ip_root = os.popen("\n curl ifconfig.me").read()
print("Ip de la box ", ip_root, "\n")


# pour voir le port wifi connecté + nom
sig_id = os.popen("\n iwgetid").read()
print("connection sous ", sig_id)


# pour voir les wifi ext
sig = os.popen("\n nmcli device wifi list").read()
print(sig)

# trouver l'adresse avec adresse MAC BSSID
