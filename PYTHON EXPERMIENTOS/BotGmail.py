### Directorio
import os
os.chdir(r"C:\Users\giani\OneDrive\Escritorio\Universidad\PYTHON EXPERMIENTOS")

### Scraping
from sys import exit
import selenium
import re
import calendar
import time
import platform
import sys
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from datetime import datetime

# Iniciamos el Selenium
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
options.add_argument("--start-maximized")
#options.add_argument("headless") este es en caso no deseamos abrir el web driver

# Obtenemos info de la web

driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe", options=options)
driver.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
a = driver.find_element(By.XPATH,"/html/body/pre")
a = a.text

# Cerramos Selenium
driver.quit()

# Un poco de limpieza
a = re.sub('{"bitcoin":{"usd":',"",a)
a = re.sub('}}','',a)
a = int(a)

# Creación del mensaje
hoy = datetime.now()
hora=hoy.hour
min=hoy.minute
hoy = str(datetime.now())
hoy=hoy[:10]
mensaje = "Saludos, soy el BOT VidaBit, y te informo que el Bitcoin el " + hoy + " a las "+str(hora)+":"+str(min)+" tiene el valor de " + str(a) + " USD. Te adjunto un Luxray para que sonrías."

### Enviando correo
# permitir mandar por gmail: https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4M2DM7kvnClCJpPbPMFWq1-wguEnDPfyTr0RAFMnkDnVxitkun-r2GquqVmn5q-NLRtzKW7YYASu4yutswKjOM5Xtwlvw
import smtplib # pip install secure-smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Iniciamos los parámetros del script
remitente = 'gianisanlorenzo@gmail.com'
contra = 'Zinnigj1234'
ruta_adjunto = 'Vs_scorpion.gif'
destinatarios = ['zinnigianluca@hotmail.com', 'gianitigre@gmail.com']
asunto = '[RPA] Correo de prueba'
cuerpo = mensaje

# Creamos el objeto mensaje
mensaje = MIMEMultipart()

# Establecemos los atributos del mensaje
mensaje['From'] = remitente
mensaje['To'] = ", ".join(destinatarios)
mensaje['Subject'] = asunto

# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Adjuntamos archivo
archivo_adjunto = open(ruta_adjunto, 'rb')
adjunto_MIME = MIMEBase('application', 'octet-stream')
adjunto_MIME.set_payload((archivo_adjunto).read())
encoders.encode_base64(adjunto_MIME)
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % ruta_adjunto)
mensaje.attach(adjunto_MIME)

# Creamos la conexión con el servidor y enviamos correo
sesion_smtp = smtplib.SMTP('smtp.gmail.com',587)
sesion_smtp.starttls()
sesion_smtp.login(remitente,contra)
texto = mensaje.as_string()
sesion_smtp.sendmail(remitente, destinatarios, texto)

# Cerramos conexión
sesion_smtp.quit()