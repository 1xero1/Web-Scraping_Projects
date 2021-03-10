#Extract bank notes details from the website 'http://www.atsnotes.com/catalog/cedulas-mundo-catalogo.html'

import requests
from bs4 import BeautifulSoup
BaseURL="http://www.atsnotes.com/catalog/"
res = requests.get('http://www.atsnotes.com/catalog/cedulas-mundo-catalogo.html')
status = res.status_code #check if the website working status
print(status)
page = requests.get("http://www.atsnotes.com/catalog/cedulas-mundo-catalogo.html") #get the main page
soup = BeautifulSoup(page.content, 'html.parser')#get the page content via 'html.parser'

#check page title, head, body
page_title = soup.title.text
page_body = soup.body
page_head = soup.head
#print(page_body)

#Since our landing page has href links leading to final extraction destination
#we extract all links tagged with href
lst=[]
SoupFind=soup.find_all('a')

for link in SoupFind:
    url=link.get('href')
    lst.append(url)

#since the 'href' links also contain the catalogue language (website language) selection, 
#we create a speate l;ist for language selection
#(optional use)
LangSelect=lst[4:16]

BankNotesURLsList=lst[17:-25]

#for x in range(len(BankNotesURLsList)):
url=BankNotesURLsList[x]
URL=BaseURL+url
page = requests.get(UURL)
status = page.status_code #check if the website working status
print(status)