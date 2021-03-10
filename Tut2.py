
import requests
from bs4 import BeautifulSoup

result=requests.get("https://www.daraz.pk/")

#verify that the URL was accessible
if result.status_code == 200:
    print("Page is Accessible")

##Extra Information from Website 
#print other information from the header
print(result.headers)

#store the page content into the 'src' variable
src=result.content
#print(src)

soup=BeautifulSoup(src,'lxml')

#get all the links
links=soup.find_all("a")
print(links)
print("\n")



#Extract the links with specific text in it
for link in links:
    if "garnier" in link.text:
        print(link)
        print(link.attrs['href'])
        
####---------Store the links from the website------######
import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.daraz.pk/")
src=result.content
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'card-categories-li hp-mod-card-hover align-left'})
records=[]
for result in results:
        name = result.find('div', attrs={'class':'name'}).text # result not results
        
        price = result.find('div', attrs={'class':'price'}).text
        records.append((name, price,))
    
# =============================================================================
# print(urls)
# =============================================================================
    






















