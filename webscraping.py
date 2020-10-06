from os import replace
import re
import requests
from bs4 import BeautifulSoup
import pprint
pagAtual = 1
ingrediente = str(input("Digite os ingredientes separados por espaço: "))
url = "https://www.tudogostoso.com.br/busca?page="+str(pagAtual)+"&q="+str(ingrediente.replace(" ", "+"))
recipe_urls = []

def main(url,ingrediente, pagAtual):
    htmlResponse = requests.get(url)
    soup = BeautifulSoup(htmlResponse.text, 'html.parser')
    container = soup.findAll("div", {"class": "mb-3 recipe-card recipe-card-with-hover"})
    #recipe_urls = []
    for r in container:
        link = "https://www.tudogostoso.com.br"+r.a['href']
        recipe_urls.append(link)
        print(link)

main(url,ingrediente,pagAtual)