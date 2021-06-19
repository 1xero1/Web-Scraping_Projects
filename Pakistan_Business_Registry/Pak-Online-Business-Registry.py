#%% Import needed Libraries
import requests
import re
import random
from bs4 import BeautifulSoup
import pickle
import csv


#%% Randomizing the user agent to prevent Web/IP blocking from the webmaster

def GET_UA():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36", 
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25", 
                 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0", 
                 "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",  
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",  
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",  
                 "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",   
                 "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",   
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36" 
                 ]
 
    return random.choice(uastrings)
##Call
#headers = {'User-Agent': GET_UA()}


#%% Load/Dump intermediary Data for further processing later

#with open('All_Info_Final.pickle', 'wb') as f:
#    pickle.dump(InfoData, f)

#with open('All_Info_Final.pickle', 'rb') as f:
#    Info = pickle.load(f)


#%% get the soup of the web address
def soups(address):
    url=address
    BasePage = requests.get(url, headers = {'User-Agent': GET_UA()})
    #BasePageStatus=BasePage.status_code
    BasePageSoup=BeautifulSoup(BasePage.content, 'html.parser')
    #BasePageStatus
    return BasePageSoup


#%% Extract all Categories from the home page
def cat():
    Cats=[]
    CatPageSoup=soups(address)
    Cat = CatPageSoup.find_all("h5")
    for cat_el in Cat:
        a_cat=cat_el.find("a")
        try:
            h_cat=a_cat.attrs['href']
        except AttributeError:
            print('usual')        
        Cats.append(h_cat)
    Cats=Cats[0:10] #removing irrelevant persistent categories
    return Cats

#%% Extract all Sub-Categories from the home page
def Sub_Cat():
    SubCat=[]
    SubCat_PageSoup=soups(address)
    SC = SubCat_PageSoup.find_all("h5")
    for subcat_el in SC:
        a_subcat=subcat_el.find("a")
        try:
            h_subcat=a_subcat.attrs['href']
        except AttributeError:
            print('usual')        
        SubCat.append(h_subcat)
    SubCat=SubCat[0:-7] #removing irrelevant persistent sub-categories
    return SubCat

#%% Each Sub-Category may have multiple pages of data, Extract all URLS of pages of Sub-Categories
def PageURL():
    uls=[]
    PageURLs=[]
    PageURLSoup=soups(address)
    for h in PageURLSoup.findAll('li', text=" >>"):
        a = h.find('a')
        if 'href' in a.attrs:
            uu = a.get('href')
            uls.append(uu)
            if len(uls[0])>6:
                lin=uls[0]
                baku=lin.split('page=')
                BaseSubCatURL=baku[0]
                MPg=baku[1]
                MPg=int(MPg)
                for i in range(1,MPg+1):
                    i=str(i)
                    uurl=BaseSubCatURL+'page='+i
                    PageURLs.append(uurl)
                    #print(url)
    if len(PageURLs)<1:
        for h in PageURLSoup.find_all('li',{'class': 'hidden-xs active'},'a'):            a = h.find('a')
        if 'href' in a.attrs:
            uu = a.get('href')
            PageURLs.append(uu)
        else:
            pass
        #    print(a)
    return PageURLs


#%% extract business cards on page(s) of sub-category page in 'biz_list'
def BusinessCard():
    biz_list=[]
    BizAddress=address
    BizSoup=soups(BizAddress)
    biz = BizSoup.find_all("h4")
    for biz_el in biz:
        a_biz=biz_el.find("a")
        try:
            h_biz=a_biz.attrs['href']
        except AttributeError:
            print('usual')        
        biz_list.append(h_biz)
    biz_list=set(biz_list) #take out the empty lists from the final compilation
    return biz_list



#%% extract all info from the business cards page(s) URL'
def BusinessInfo():
    LIST=[]
    lst=[]
    lst1=[]
    
    BusinessInfoAddress=address
    BusinessInfoSoup=soups(BusinessInfoAddress)
    itemprops=["streetAddress","addressLocality","addressRegion","telephone","faxNumber","description"]
    
    U = BusinessInfoSoup.find_all("a",itemprop="url")
    if len(U)<5:
        Wesite='NA'
    else:
        for h in U:
            Wesite=h.get('href')
            #print(Wesite)
            try:
                Wesite
            except NameError:
                Wesite='NA'
            
    try:
        BusinessName = BusinessInfoSoup.find(class_ = 'page-header').find('span', itemprop = 'name').get_text()
    except NameError:
        BusinessName='NA'

    cat = BusinessInfoSoup.find_all('div',{'class': 'breadcrumb breadcrumb-hybrid'},'a')
    for c in cat:
        ss=c.get_text()
        lst.append(ss)
    lis=ss.split('\n')
    Category=lis[7]
    SubCategory=lis[9]

    el = BusinessInfoSoup.find_all('div',{'class': 'panel-body'},'p')
    for e in el:
        sh=e.get_text()
        lst1.append(sh)
        more=lst1[0]
        contact=re.split('\n |: |\*|\n', more)

    try:
        ContactPerson=contact[2]
    except NameError:    
        ContactPerson='NA'
    try:
        BusinessType=contact[4]
    except:
        BusinessType='NA'

    data = BusinessInfoSoup.find_all('div', itemprop='aggregateRating')
    for d in data:
        star=d.get_text()
    rat=re.split(' | \n \*|\n', star)
    StarRating=rat[1]
    Votes=rat[4]

    LIST.append(BusinessName)
    LIST.append(Category)
    LIST.append(SubCategory)
    LIST.append(BusinessType)
    LIST.append(StarRating)
    LIST.append(Votes)
    LIST.append(Wesite)
    LIST.append(ContactPerson)

    for it in itemprops:
        dat=BusinessInfoSoup.find_all("span",itemprop=it)
        for span in dat:
            data=span.get_text()
            try:
                data
            except NameError:
                data='NA'
            LIST.append(data)
    return LIST



#%% run cat() function to Extract Categories
address='MainPageURL'
Cats=cat()
#print(Cats)

#%% run Sub_Cat() function to Extract Sub-Catehories
S_Cat=[]
for cat_links in Cats:
    print('\n Getting Sub-Categoriess \n')
    address=cat_links
    SubCats=Sub_Cat()
    S_Cat.append(SubCats)
    #print(SubCats)


#%% run PageURL() function to Extract All Page URLS for Each Sub-Category in S_Cat list
PageURLS=[]
for lilink in S_Cat:
    for lilinks in lilink:
        print(lilinks)
        print('\n')
        address=lilinks
        PageURLs=PageURL()
        PageURLS.append(PageURLs)
    #print(PageURLs)


#%% run BusinessCard() function to Extract All Businesses URLs from all Page URLS for Each Sub-Category
BizCard=[]
for biz_link in PageURLS:
    for biz_links in biz_link:
        print('Getting Business Cards \n')
        address=biz_links
        BizCards=BusinessCard()
        BizCard.append(BizCards)
        print(BizCards)
        print('\n')       
#print(BizCards)


#%% run BusinessInfo() function to Extract all info from the business page
InfoData=[]
#max=100
max=len(BizCard)
for ii in range(0,max):
    BizURLs= BizCard[ii]
    #print(BizURL)
    for BizURL in BizURLs:
        address=BizURL
        print(address)
        InfoList=BusinessInfo()
        InfoData.append(InfoList)
        print('Set', ii, 'of', max, ' is Done')


#%% write data to csv file
header=['Business Name', 'Category', 'Sub-Category', 'Business Type', 'Rating', 
        'by People', 'Website', 'Contact Person', 'Full Address',
        'City', 'Province', 'Phone', 'Fax', 'Business Description']

with open('PYP.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    writer.writerows(InfoData)

