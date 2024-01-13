import requests
import shutil

def getIpWan ():
    urlCheckWan = "https://eth0.me"
    r = requests.get(urlCheckWan)
    return  r.text

def getDiskUsage(disk_path):

    total, used, free = shutil.disk_usage(disk_path)
    
    to = "Total: %d GB" % (total // (2**30))
    us = "Uso: %d GB" % (used // (2**30))
    li = "Libre: %d GB" % (free // (2**30))

    cadena = "Espazo en disco para unidade " +  disk_path + " :  \n " + to + "\n" + us + "\n" + li 

    return cadena
