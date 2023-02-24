# -*- coding: utf-8 -*-
#pip install webbrowser
#pip install PyAutoGUI
import webbrowser as web
import pyautogui as pt
import pandas as pd
import time
import pyperclip
import re
import os
import math

web.open("https://www.google.com")
coord=[]

os.chdir(r'C:\Users\giani\OneDrive\Escritorio\Universidad\PYTHON EXPERMIENTOS')
data = pd.read_excel("direcciones_buscar.xlsx")
data["Buscar"]=data["Departamento"]+" "+data["Provincia"]+" "+data["Distrito"]+" "+data["Dirección"]
buscar = data["Buscar"].values

def isnan(value):
    try: 
        return math.isnan(float(value))
    except:
        return False

p1=380,50 # click al buscador
p2=300,210 # click a maps
p3=722,41 # click al url
pobs3=200,300 # click a una parte de direcciones opcionales (por si nos lleva a otro país)


for i in range(0,len(buscar)):
    if isnan(buscar[i])==False:
        pt.click(p1)
        time.sleep(2)
        pt.typewrite(buscar[i])
        pt.hotkey("ENTER")
        time.sleep(5)
        pt.click(p2)
        time.sleep(5)
        
        # pt.typewrite("maps")
        # time.sleep(2)
        # pt.hotkey("Ctrl","Enter")
        # time.sleep(10)
        # pt.click(p3)
        # time.sleep(3)
        # pt.hotkey("Ctrl","c")
        a = re.findall("@-\d+.\d+,-\d+.\d+", pyperclip.paste())
        # try:
        #     coord.append(a)
        #     a = re.sub("@","",a[0])
        # except:
        #     print("1 falla")
        #     pt.click(pobs3)
        #     time.sleep(9)
        #     pt.click(p3)
        #     time.sleep(3)
        #     pt.hotkey("Ctrl","c")
        #     a = re.findall("@+\d+.\d+,+\d+.\d+", pyperclip.paste())
        #     a = re.sub("@","",a[0])
        #     coord.append(a)                         
    else:
        coord.append("")
        
        
data["coord"]=coord
data.to_excel("direcciones_encontradas.xlsx",index=False)

# por se aca: https://stackoverflow.com/questions/49101270/move-to-searched-text-on-active-screen-with-pyautogui