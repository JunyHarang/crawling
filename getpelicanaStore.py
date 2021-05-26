# ChickenUtil 이라는 Class 안에 ChickenStore()를 불러온다.

from itertools import count

from ChickenUtil import ChickenStore

##########################################################################################################
brandName = '페리카나'
base_url = 'https://pelicana.co.kr/store/stroe_search.html'
##########################################################################################################
def getData():

    savedData = [] # 액셀로 저장될 List 선언

    for page_idx in count():
        
        url = base_url + '?page=' + str(page_idx + 1)
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()
        # print(type(soup))

        if soup != None:
            mytable = soup.find('table', attrs={'class':'table mt20'})
        
        mytbody = mytable.find('tbody')

        shopExists = False  # 목록이 없다고 가정하기 위하여 선언

        # count = 0

        for mytr in mytbody.findAll('tr'):
            shopExists = True

            imsiphone = mytr.select_one('td:nth-of-type(3)').string

            if imsiphone != None :
                phone = imsiphone.strip() 
            else :
                phone = ''

            # print(phone)

            mylist = list(mytr.strings)
            # print(mylist)
            # print('-'*30)

            storeName = mylist[1]
            # print(storeName)

            storeAddress = mylist[3]
            # print(storeAddress)

            # 주소에 길이가 2자리 이상일 때 if문 실행
            if len(storeAddress) >= 2 :
                tmp = storeAddress.split()
                sido = tmp[0]
                gungu = tmp[1]

                # print('==================')
                # print(sido)
                # print('------------------')
                # print(gungu)

                mydata = [brandName, storeName, sido, gungu, storeAddress, phone]

                savedData.append(mydata)

        print(savedData)

        if shopExists == False:
            chknStore.save2Csv(savedData)

            break
##########################################################################################################
print(brandName + ' 크롤링을 시작 합니다!')
getData()
print(brandName + ' 크롤링이 종료 되었습니다!')
