import serverInfo
import telegramBot
import exteriorDatos
import saudos
import time
import requests
from datetime import datetime
# Import the configparser module
import configparser
config = configparser.ConfigParser()  
config.read('config.ini')


ip = serverInfo.getIpWan()
espazo = serverInfo.getDiskUsage("/")
saudo = saudos.boDia()

mensaxeIpWan = "A IP externa do servidor é : " + ip
mensaxe = "A temperatura en Mugardos é " + exteriorDatos.obtener(config.get('Configuracion', 'OwmKey'), config.get('Configuracion', 'Ubicacion')) + " ºC"

print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), saudo))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), mensaxe))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), espazo))