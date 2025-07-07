import requests
from bs4 import BeautifulSoup


url = 'https://aimicrodegree.org/login'
response = requests.get(url)

#check if request was succesful
if response.status_code == 200:
    print("Successfully fetch the web page")
else:
    print(F"failed . status code: {response.status_code}")


soup = BeautifulSoup(response.text, 'lxml')
    #we can also use 'html' parser
title =  soup.title.string
print(F"page title: {title}")

    # Extract all Hyperlinks
links = soup.find_all('a')
for link in links:
        href = link.get('href')
        text = link.get_text()
        print(F"link text: {text}, URL: {href}")


paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.get_text())