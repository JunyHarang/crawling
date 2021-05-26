from email.headerregistry import Address
from email.mime import base
import re # 정규 표현식 모듈 불러오기

from itertools import count
import branca

from numpy import save

from ChickenUtil import ChickenStore    # ChickenUtil 이라는 Class 안에 ChickenStore()를 불러온다.

##########################################################################################################
brandName = '굽네치킨'
base_url = 'https://www.goobne.co.kr/store/search_store.jsp'
##########################################################################################################
def getData():

    savedData = [] # 액셀로 저장될 List 선언

    chknStore = ChickenStore(brandName, base_url)

    for page_idx in count() :
        print('%s번째 페이지가 호출 되었습니다!' % str(page_idx + 1))
        bEndpage = False        # 마지막 페이지면 True

        cmdJavaScript = "javascript:store.getList('%s')" % str(page_idx + 1)

        soup = chknStore.getWebDriver(cmdJavaScript)

        store_list = soup.find('tbody', attrs = {'id':'store_list'})

        mytrlists = store_list.findAll('tr')

        # print(len(mytrlists))

        print(type(soup))

        for onestore in mytrlists:
            mytdlists = onestore.findAll('td')

            if len(mytdlists) > 1:
                store = onestore.select_one('td:nth-of-type(1)').get_text(strip=True) 

                phone = onestore.select_one('td:nth-of-type(2)').a.string

                address = onestore.select_one('td:nth-of-type(3)').a.string

                tmp = str(address).split(' ')
                
                sido = tmp[0]
                
                gungu = tmp[1]

                savedData.append([brandName, store, sido, gungu, address, phone])

            else : # 마지막 페이지라면
                bEndpage = True
                break
        
        # if page_idx == 2 :
        #     break

        if bEndpage == True:
            break

        # chknStore.save2Csv(savedData)
            
    # print(savedData)

    chnkStore.save2Csv(savedData)

            # break
##########################################################################################################
print(brandName + ' 크롤링을 시작 합니다!')
getData()
print(brandName + ' 크롤링이 종료 되었습니다!')
