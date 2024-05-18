import serverInfo
import telegramBot
import exteriorDatos
import saudos
import time
import requests
import os
from datetime import datetime

# Import the configparser module
import configparser
config = configparser.ConfigParser()  
config.read('config.ini')


ip = serverInfo.getIpWan()
espazoStorage = serverInfo.getDiskUsage(str("/storage"))
espazoRaiz = serverInfo.getDiskUsage(str("/"))
espazoRaid = serverInfo.getDiskUsage(str("/mnt/array"))
espazoExterno = serverInfo.getDiskUsage(str("/mnt/externo"))
espazoExterno4tb = serverInfo.getDiskUsage(str("/mnt/externo4tb"))
#saudo = saudos.boDia()
saudo = "Información diaria para servidor drugo - Codery"
uptime = os.popen('uptime|cut -d , -f1|cut -d u -f 2|cut -d p -f 2').read()

mensaxeIpWan = "A IP externa do servidor é : " + ip
mensaxeTemp = "A temperatura en AMES é " + exteriorDatos.obtener(config.get('Configuracion', 'OwmKey'), config.get('Configuracion', 'Ubicacion')) + " ºC"

print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), "🌟🌟🌟🌟🌟🌟🌟🌟🌟"))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), "Información diaria drugo"))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), ""))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), ".."))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), "Uptime: " + str(uptime)))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), mensaxeTemp))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), ".."))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), mensaxeIpWan))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), ".."))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), espazoStorage))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), espazoRaiz))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), espazoRaid))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), espazoExterno))
print ("Mensaxe enviado..", telegramBot.enviarMensaje(config.get('Configuracion', 'BotToken'), str(config.get('Configuracion', 'ChatId')), espazoExterno4tb))

