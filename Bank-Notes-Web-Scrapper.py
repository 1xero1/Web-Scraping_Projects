###Extract bank notes details from the website ''

import requests
from bs4 import BeautifulSoup
import time

#lists initializations
ImgList=[]
ImgNames=[]
ImURL=[]
ImageName=[]
CountryNames=[]
lst=[]

BaseURL=""
BasePage = requests.get('')
BaseStatus = BasePage.status_code #check if the website working
if BaseStatus==200:
    print("Success! The Main page is working")

BasePageSoup = BeautifulSoup(BasePage.content, 'html.parser')
#Since our landing page has href links leading to final extraction destination
#we extract all links tagged with href

BaseSoupFind=BasePageSoup.find_all('a')

for link in BaseSoupFind:
    url=link.get('href')
    lst.append(url)
#lst

LangSelect=lst[4:16] # List for language selection (Optional Implementation)
CountriesURLsList=lst[17:-25] #List of Countries (destination URLs)

# List of country names to save images in their respective folders

for nm in CountriesURLsList:
    nam=nm.split("/")
    Name=nam[-1]
    CountryName=Name[0:-5]
    CountryNames.append(CountryName)

for CountryURL in CountriesURLsList:
    CountryPageURL=BaseURL+CountryURL
    CountryPage = requests.get(CountryPageURL)
    CountryPageStatus = CountryPage.status_code
    if CountryPageStatus==200:
        print("Success! The destination page: %s" % CountryPageURL, " is working::")
    CountryPageSoup= BeautifulSoup(CountryPage.content, 'html.parser')
    images = CountryPageSoup.select('img') #get the images URL List
    for image in images:
        src = image.get('src')
        ImgList.append(src)
print("All Images URLs retrieved")
    
#Remove extra Logo Images
Logo=
Logo1=
while Logo in ImgList:
    ImgList.remove(Logo)
while Logo1 in ImgList:
    ImgList.remove(Logo1)

#Get the Full Image URLS    
for url in ImgList:
    ImgURL=url[3:]
    ImageURL=BaseURL+ImgURL
    ImURL.append(ImageURL)
print("Full Image URLs Retrieved ")

#Get the Image Names
for URL in ImURL:
    nm=URL.split("/")
    ImgName=nm[-1]
    ImageName.append(ImgName)
print("Image names retrieved from the Image URLs")

# Write Images to local storage
for x in range(0,len(ImURL)):
    img_data = requests.get(ImURL[x]).content
    with open(ImageName[x], 'wb') as handler:
        handler.write(img_data)
        print(ImageName[x], "at: %s" % ImURL[x], "is Saved")
print("All images have been saved")

#***********************x*x*x****************************#