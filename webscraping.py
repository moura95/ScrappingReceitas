import requests
from bs4 import BeautifulSoup
from pprint import pprint

buscar = str(input("Digite algum ingrediente: "))

base_url = "https://www.tudogostoso.com.br"
url = f"https://www.tudogostoso.com.br/busca?q={buscar}"


html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")


def get_links(url):
    links = []

    links_rec = soup.findAll("a", {"class": "link row m-0"})
    for link in links_rec:
        link = f"{base_url}{link['href']}"
        links.append(link)
    return links


def get_ingredientes(urlreceita):
    html = requests.get(urlreceita).text
    soup = BeautifulSoup(html, "html.parser")
    list_ingrediente = "\n"
    title = soup.h1.text
    ingredientes = soup.findAll("span", {"class": "p-ingredient"})
    ingredientes = map(lambda i: i.text, ingredientes)
    ingredientes = list_ingrediente.join(ingredientes)
    link = urlreceita
    return link, title, ingredientes


def main():
    links = get_links(url)
    for link in links:
        link, title, ingredientes = get_ingredientes(link)
        print(f"{title}\n{ingredientes}\n {link}")
        print("------------------------------------")


main()
