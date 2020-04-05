from bs4 import BeautifulSoup
import requests

search = input("Enter search terms:")
params = {"q" : search}

r = requests.get("https://www.google.com/search", params=params)

soup = BeautifulSoup(r.text, features="html.parser")
print(soup.prettify())