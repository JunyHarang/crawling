from email.headerregistry import Address
from email.mime import base
import re # 정규 표현식 모듈 불러오기

from itertools import count
import branca

from numpy import save

from ChickenUtil import ChickenStore    # ChickenUtil 이라는 Class 안에 ChickenStore()를 불러온다.

##########################################################################################################
brandName = '처가집'
base_url = 'http://www.cheogajip.co.kr/bbs/board.php'
##########################################################################################################
def getData():

    savedData = [] # 액셀로 저장될 List 선언

    for page_idx in count() :
        url = base_url
        url += '?bo_table=store'
        url += '&page%s' % str(page_idx)

        chknStore = ChickenStore(brandName, url)

        soup = chknStore.getSoup()

       # print(type(soup))
        
        mytbody = soup.find('tbody')
        
        shopExists = False        # 매장이 없다고 가정
        
        for mytr in mytbody.findAll('tr') :
            shopExists = True
            
            try:
                store = mytr.select_one('td:nth-of-type(2)').string
                
                address = mytr.select_one('td:nth-of-type(3)').string
                
                imsi = address.split()
        
                sido = imsi[0]
                
                gungu = imsi[1]
        
                phone = mytr.select_one('td:nth-of-type(4)').string
                
                savedData.append([brandName, store, sido, gungu, address, phone])

            except AttributeError as err :
                print(err)
               
                shopExists = False
                
                break
    
        if shopExists == False :

            chknStore.save2Csv(savedData)
            break
            
    # print(savedData)

    # chnkStore.save2Csv(savedData)

            # break
##########################################################################################################
print(brandName + ' 크롤링을 시작 합니다!')
getData()
print(brandName + ' 크롤링이 종료 되었습니다!')
