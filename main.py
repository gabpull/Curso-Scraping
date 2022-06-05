from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from connecction import *
from products import Products

def get_soup(url):
    driver = webdriver.Chrome('driver/chromedriver.exe')
    driver.get(url)
    sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()
    return soup

def get_amazon_object(soup):
    products = soup.find_all('div', {'class':"s-featured-result-item"})
    for i, product in enumerate(products):
        name = product.find('span', {'class':"a-size-medium a-color-base a-text-normal"}).text
        price = product.find('span', {'class':"a-offscreen"}).text
        print(f'{i+1}. {name}. Precio: {price}')

    selected = int(input("Escoja un producto de Amazon: "))
    amazon_url = products[selected-1].find('a', {'class':"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}).attrs['href']
    amazon_price = products[selected-1].find('span', {'class':"a-offscreen"}).text
    return amazon_url, amazon_price



def get_ebay_object(soup):
    products = soup.find_all('li', {'class':"s-item s-item__pl-on-bottom"})
    for i, product in enumerate(products):
        name = product.find('h3', {'class':"s-item__title"}).text
        price = product.find('span', {'class':"s-item__price"}).text
        print(f'{i+1}. {name}. Precio: {price}')

    selected = int(input("Escoja un producto de eBay: "))
    ebay_url = products[selected-1].find('a', {'class':"s-item__link"}).attrs['href']
    ebay_price = products[selected-1].find('span', {'class':"s-item__price"}).text
    return amazon_url, amazon_price


def init():
    name = input("Ingrese el producto a Buscar:  ").replace(" ", "+")
    amazon_result_url = f"https://www.amazon.com/s?k={name}&crid=16U03R5OU1GWZ&sprefix=logitech+c922%2Caps%2C159&ref=nb_sb_noss_1"
    ebay_result_url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={name}&_sacat=0"
    #amazon_soup = get_soup(amazon_result_url)
    #ebay_soup = get_soup(ebay_result_url)
    #amazon_url, amazon_price = get_amazon_object(amazon_soup)
    #ebay_url, ebay_price = get_amazon_object(ebay_soup)
    #print(amazon_url, amazon_price)
    #print(ebay_url, ebay_price)

if __name__ == "__main__":
    init()    
