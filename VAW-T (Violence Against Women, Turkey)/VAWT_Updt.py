# =============================================================================
 #import needed libraries
#import requests  #to send reques for  webpage retrieval
import pickle
#from bs4 import BeautifulSoup  #For webpage access and extract
# 
# #initializations
# lst=[]
# BaseURL=''
# Y=''
# Name=[]
# Date=[]
# MurderMotive=[]
# MurdererName=[]
# ProtectionRequest=[]
# MurderWeapon=[]
# NewsSource=[]
# DataSource=[]
# AgeofVictim=[]
# Province=[]
# PerpetratorStatus=[]
# 
# ### Create List of URLS needed to travers for data acquistion
# def LST(url):
#     BasePage = requests.get(Y)
#     BasePageSoup=BeautifulSoup(BasePage.content, 'html.parser')
#     BaseSoupFind=BasePageSoup.find_all('a')
#     for link in BaseSoupFind:
#         url=link.get('href')
#         fURL=BaseURL+url
#         #print(url)
#         lst.append(fURL)
#     del lst[0:2]
#     return lst
# #lst #Check length of created URLs list a.k.a 'lst'
# #len(lst) #check length of created URLs list a.k.a 'lst'
# 
# def TEXT(url):
#     BasePage = requests.get(url)
#     BasePageSoup=BeautifulSoup(BasePage.content, 'html.parser')
#     text = BasePageSoup.find_all(text=True)
#     return text
# 
# 
# ### Function to extract data if the number of elements at destination page are old dated
# def short(text):
#     Name.append(text[13])
#     Date.append(text[15])
#     MurderMotive.append(text[17])
#     MurdererName.append(text[19])
#     ProtectionRequest.append(text[21])
#     MurderWeapon.append(text[23])
#     NewsSource.append(text[25])
#     DataSource.append(url)
#     
# ### Function to extract data if the number of elements at destination page are updated
# def long(text):
#     Name.append(text[13])
#     AgeofVictim.append(text[15])
#     Province.append(text[17])
#     Date.append(text[19])
#     MurderMotive.append(text[21])
#     MurdererName.append(text[23])
#     ProtectionRequest.append(text[25])
#     MurderWeapon.append(text[27])
#     PerpetratorStatus.append(text[29])
#     NewsSource.append(text[32])
#     DataSource.append(url)
#     
# def long2(text):
#     Name.append(text[13])
#     AgeofVictim.append(text[15])
#     Province.append(text[17])
#     Date.append(text[19])
#     MurderMotive.append(text[21])
#     MurdererName.append(text[23])
#     ProtectionRequest.append(text[25])
#     MurderWeapon.append(text[27])
#     NewsSource.append(text[32])
#     DataSource.append(url)
#     
#     
# 
# lst=LST(Y)
# len(lst)
# 
# number=0
# for url in lst:
#     #translator = Translator()
#     text = TEXT(url)
# 
#     
#     if len(text)<=16:        
#         #Data=short(text)
#         short(text)
#         #col+=1
#         #short_write(Data)
#         #print("Data Written in Sheet 1 \n")
#     elif len(text)<34:
#         
#         
#     else:        
#         #Data=long(text)
#         long(text)
#         #COL+=1
#         #long_write(Data)
#         #print("Data Written in Sheet 2 \n ")
#     #time.sleep(5)
#     number+=1
#     nn=url.split('id=')
#     new=nn[-1]
#     print('Done', str(number) , ' of', str(len(lst)), "\t ID: " , new, 'done')

with open('file.pkl','rb') as file:
    Data=pickle.load(file)
    
Name15=[]        
Date15=[]
MurderMotive15=[]
MurdererName15=[]
ProtectionRequest15=[]
WayOfKilling15=[]        
NewsSource15=[]
NN='NA'

Name16=[]
Date16=[]
MurderMotive16=[]
MurdererName16=[]
ProtectionRequest16=[]
WayOfKilling16=[]
NewsSource16=[]

Name17=[]
Date17=[]
MurderMotive17=[]
MurdererName17=[]
ProtectionRequest17=[]
WayOfKilling17=[]
NewsSource17_1=[]
NewsSource17_2=[]

Name18=[]
Date18=[]
MurderMotive18=[]
MurdererName18=[]
ProtectionRequest18=[]
WayOfKilling18=[]
NewsSource18=[]
PerpetroatorStatus18=[]

Name19=[]
Date19=[]
MurderMotive19=[]
MurdererName19=[]
ProtectionRequest19=[]
WayOfKilling19=[]
NewsSource19_1=[]
NewsSource19_2=[]
        
Name20=[]
Date20=[]
MurderMotive20=[]
MurdererName20=[]
ProtectionRequest20=[]
WayOfKilling20=[]
NewsSource20=[]
Province20=[]
AgeofVictim20=[]
    
Name21=[]
Date21=[]
MurderMotive21=[]
MurdererName21=[]
ProtectionRequest21=[]
WayOfKilling21=[]
NewsSource21_1=[]
NewsSource21_2=[]
PerpetratorStatus21=[]
Province21=[]
AgeofVictim21=[]
    
Name22=[]
Date22=[]
MurderMotive22=[]
MurdererName22=[]
ProtectionRequest22=[]
WayOfKilling22=[]
NewsSource22=[]
PerpetratorStatus22=[]
Province22=[]
AgeofVictim22=[]
    
Name23=[]
Date23=[]
MurderMotive23=[]
MurdererName23=[]
ProtectionRequest23=[]
WayOfKilling23=[]
NewsSource23_1=[]
NewsSource23_2=[]
PerpetratorStatus23=[]
Province23=[]
AgeofVictim23=[]
    
Name24=[]
Date24=[]
MurderMotive24=[]
MurdererName24=[]
ProtectionRequest24=[]
WayOfKilling24=[]
NewsSource24=[]
PerpetratorStatus24=[]
Province24=[]
AgeofVictim24=[]
Notes=[]

Name25=[]
Date25=[]
MurderMotive25=[]
MurdererName25=[]
ProtectionRequest25=[]
WayOfKilling25=[]
PerpetratorStatus25=[]
Province25=[]
AgeofVictim25=[]
NewsSource25_1=[]
NewsSource25_2=[]
Notes25=[]


for L in Data:
    
    if len(L)==15:
        Name15.append(L[1])
        Date15.append(L[3])
        MurderMotive15.append(L[5])
        MurdererName15.append(L[7])
        ProtectionRequest15.append(L[9])
        WayOfKilling15.append(L[11])
        NewsSource15.append(NN)
    
    elif len(L)==16:
        Name16.append(L[1])
        Date16.append(L[3])
        MurderMotive16.append(L[5])
        MurdererName16.append(L[7])
        ProtectionRequest16.append(L[9])
        WayOfKilling16.append(L[11])
        NewsSource16.append(L[14])

    elif len(L)==17:
        Name17.append(L[1])         
        Date17.append(L[3]) 
        MurderMotive17.append(L[5]) 
        MurdererName17.append(L[7]) 
        ProtectionRequest17.append(L[9]) 
        WayOfKilling17.append(L[11]) 
        NewsSource17_1.append(L[14]) 
        NewsSource17_2.append(L[15])
    
    elif len(L)==18:
        Name18.append(L[1])
        Date18.append(L[3])
        MurderMotive18.append(L[5])
        MurdererName18.append(L[7])
        ProtectionRequest18.append(L[9])
        WayOfKilling18.append(L[11])
        NewsSource18.append(L[16])
        PerpetroatorStatus18.append(L[13])
    
    elif len(L)==19:
        Name19.append(L[1])
        Date19.append(L[3])
        MurderMotive19.append(L[5])
        MurdererName19.append(L[7])
        ProtectionRequest19.append(L[9])
        WayOfKilling19.append(L[11])
        NewsSource19_1.append(L[15]) 
        NewsSource19_2.append(L[16])
        
    elif len(L)==20:
        Name20.append(L[1])
        Date20.append(L[7])
        MurderMotive20.append(L[9])
        MurdererName20.append(L[11])
        ProtectionRequest20.append(L[13])
        WayOfKilling20.append(L[15])
        NewsSource20.append(L[19])
        Province20.append(L[5])
        AgeofVictim20.append(L[3])
    
    elif len(L)==21:
        Name21.append(L[1])        
        Date21.append(L[5])
        MurderMotive21.append(L[7])
        MurdererName21.append(L[9])
        ProtectionRequest21.append(L[11])
        WayOfKilling21.append(L[13])
        NewsSource21_1.append(L[18])
        NewsSource21_2.append(L[19])
        PerpetratorStatus21.append(L[15])
        Province21.append(L[3])
    
    elif len(L)==22:
        Name22.append(L[1])        
        Date22.append(L[7])
        MurderMotive22.append(L[9])
        MurdererName22.append(L[11])
        ProtectionRequest22.append(L[13])
        WayOfKilling22.append(L[15])
        NewsSource22.append(L[20])
        PerpetratorStatus22.append(L[17])
        Province22.append(L[5])
        AgeofVictim22.append(L[3])
    
    elif len(L)==23:
        Name23.append(L[1])
        Date23.append(L[7])
        MurderMotive23.append(L[9])
        MurdererName23.append(L[11])
        ProtectionRequest23.append(L[13])
        WayOfKilling23.append(L[15])
        NewsSource23_1.append(L[20])
        NewsSource23_2.append(L[21])
        PerpetratorStatus23.append(L[17])
        Province23.append(L[5])
        AgeofVictim23.append(L[3])
    
    elif len(L)==24:
        Name24.append(L[1])        
        Date24.append(L[7])
        MurderMotive24.append(L[9])
        MurdererName24.append(L[11])
        ProtectionRequest24.append(L[13])
        WayOfKilling24.append(L[15])
        NewsSource24.append(L[23])
        PerpetratorStatus24.append(L[17])
        Province24.append(L[5])
        AgeofVictim24.append(L[3])
        Notes.append(L[20])

    elif len(L)==25:
        Name25.append(L[1])
        Date25.append(L[7])
        MurderMotive25.append(L[9])
        MurdererName25.append(L[11])
        ProtectionRequest25.append(L[13])
        WayOfKilling25.append(L[15])
        NewsSource25_1.append(L[22]) 
        NewsSource25_2.append(L[23])
        PerpetratorStatus25.append(L[17])
        Province25.append(L[5])
        AgeofVictim25.append(L[3])
        Notes25.append(L[19])

        
    else:
 #       return
        print('non of those')
    
    

Name16
#Date16
#MurderMotive16
#MurdererName16
#ProtectionRequest16
#WayOfKilling16
#NewsSource16

