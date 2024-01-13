import urllib3
import requests
import json

def enviarMensaje(bot_api_key, chat_id, mesg):
    http = urllib3.PoolManager()
    baseURL = 'https://api.telegram.org/bot' + bot_api_key + '/sendMessage?chat_id='+ chat_id +'>&text=' + mesg
    r = http.request('POST', baseURL)
    
    r.status

    r.data
    r.release_conn()
    print ("Mensaje enviado")
