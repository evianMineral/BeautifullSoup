from bs4 import BeautifulSoup
import requests

search = input("Enter search terms:")
params = {"q" : search}

gr = requests.get("https://www.google.com/search", params=params)

soup = BeautifulSoup(gr.text, "html.parser")

resultDiv = soup.find_all('div', attrs = {'class' : 'ZINbbc'})

links = []
titles = []
descriptions = []

for r in resultDiv:
    # Checks if each element is present, else, raise exception
    try:
        link = r.find('a', href = True)
        link2 = r.find("a").attrs["href"]
        title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
        description = r.find('div', attrs={'class':'s3v9rd'}).get_text()
        
        # Check to make sure everything is present before appending
        if link != '' and title != '' and description != '': 
            links.append(link['href'])
            titles.append(title)
            descriptions.append(description)
    # Next loop if one element is not present
    except:
        continue