#NOTA: SABER QUE LOS SCHEDULE SE BORRAN SOLO CUANDO PYTHON SE CIERRA O CANCELAS POR COMANDO!
#pip install pywhatkit
#pip install schedule
import json
import requests
import pywhatkit
import datetime
import schedule
import time
from urllib.parse import quote
import pyautogui as pt
import webbrowser as web

#creador: https://github.com/Ankit404butfound/PyWhatKit/blob/master/pywhatkit/main.py


#inspirado del vídeo: https://www.youtube.com/watch?v=p9dPoIsxMsM

def MsgWsp():
    now = datetime.datetime.now()
    pywhatkit.sendwhatmsg_instantly("+541153383316", "Puto",wait_time=15)
MsgWsp()
schedule.every().hour.do(MsgWsp)

def job():
    now = datetime.datetime.now()
    print(now.hour)
    
    
    print(now.minute+1)
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    a = json.loads(r.text)
    btc_string = "1 Bitcoin te costará " + str(a["bitcoin"]["usd"]) + " USD"
    pywhatkit.sendwhatmsg_to_group("DALPuGJPg3eGDkXK9T5TNB", "Hola amigos, les informo que hoy " + btc_string + ". Toy programando desde python asheee", now.hour, now.minute+1,wait_time=15)
# job()
schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
