from urllib import request
#from selenium import webdriver
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import time
import webbrowser


url = requests.get("https://www.masxmenos.cr/torta-kimby-congelado-pollo-unidades-640gr/p")
url2 = requests.get("https://www.peridomicilio.com/frescos/congelados/tortas-congeladas/tortas-pollo-kimby-8und.html")
url3 = requests.get("https://www.walmart.co.cr/torta-kimby-congelado-pollo-unidades-640gr/p")
#url4 = requests.get("http://www.automercado.cr/p/torta-pollo-kimby-caja-640-g/id/cec900ee-a42d-4ce4-88fb-25417aeb3d2a")


soup = BeautifulSoup(url.content, "html.parser")
soup2 = BeautifulSoup(url2.content, "html.parser")
soup3 = BeautifulSoup(url3.content, "html.parser")
#soup4 = BeautifulSoup(url4.content, "html.parser")

resultado = float(soup.find("span", {"class":"vtex-store-components-3-x-currencyContainer vtex-store-components-3-x-currencyContainer--summary"}).text.replace("₡","").replace(".",""))
resultado2 = float(soup2.find("span", {"id":"sec_discounted_price_7231"}).text.replace(",",""))
resultado3 = float(soup3.find("span", {"class":"vtex-store-components-3-x-currencyContainer vtex-store-components-3-x-currencyContainer--summary"}).text.replace("₡","").replace(".",""))
#resultado4 = soup4.find("div", {"class":"med-small-text"})



print("Mas x Menos: " + str(resultado))
print("Peri: " + str(resultado2))
print("Walmart: " + str(resultado3))


url = "http://www.automercado.cr/p/torta-pollo-kimby-caja-640-g/id/cec900ee-a42d-4ce4-88fb-25417aeb3d2a"
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = BeautifulSoup(webpage, "html.parser")
containers = page_soup.find_all("div", {"class":"med-small-text"})

auto = containers[1].text.replace("₡","").replace(",","")
cortado = float(auto[0:auto.find("/")] )
print("Automercado: " + str(cortado))


# print("Auto Mercado: " + auto.find("/"))


# for container in containers:
    # print(containers[1])


#print("AutoMercado: " + str(resultado4))



