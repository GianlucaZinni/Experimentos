from selenium import webdriver
import pandas as pd


website = 'https://www.coinbase.com/es/price/ethereum'
website2 = 'https://dolarhoy.com/'
path = 'C:\webdrivers\chromedriver.exe'

    # definer variable 'driver'
driver = webdriver.Chrome(path)
driver2 = webdriver.Chrome(path)


    # abrir Google Chrome mediante chromedriver
driver.get(website)
driver2.get(website2)
        
    # copiar valor del ETH
Etherium = driver.find_element_by_xpath('//div[@data-testid="asset-overview-price"]')
Dolar = driver2.find_element_by_xpath('//div[@class="val"]')

a = Etherium.text
b = Dolar.text


aa = a.replace(a[-1],"")
aaa = aa.replace(aa[-1],"")
aaaa = aaa.replace(aaa[-1],"")
aaaaa = aaaa.replace(aaaa[-1],"")
bb = b.replace(b[0],"")

int(aaaaa)
int(bb)

    # almacenar en lista
Celda = [aaaaa , bb]
print(Celda)



    # crea Dataframe en Pandas y exporta data en CSV (Excel)
    
Data = {'Etherium': [aaaaa],'   ': ["  "], 'Dolar': [bb]}
df = pd.DataFrame(Data)


print(df)
df.to_csv('Etherium.csv', index=False)