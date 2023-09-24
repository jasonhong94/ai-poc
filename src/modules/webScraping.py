import requests
from bs4 import BeautifulSoup
from langchain.document_loaders import BSHTMLLoader


def loadHtml(self):
    url = 'https://ipoconference2023.v-capital.co/'
    data = requests.get(url)

    html = BeautifulSoup(data.text, 'html.parser')

    return html

def bs4LoadHtml():
    loader = BSHTMLLoader("https://ipoconference2023.v-capital.co/")
    data = loader.load()

    return data


bs4LoadHtml()
