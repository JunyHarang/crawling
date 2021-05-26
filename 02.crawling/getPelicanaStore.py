from itertools import count
from ChickenUtil import ChickenStore
####################################################
brandName = 'pelicana' # 브랜드 이름
base_url = 'https://www.pelicana.co.kr/store/stroe_search.html' # 접속  url
####################################################
def getData():
    savedData = [] # 엑셀로 저장할 리스트
    
    for page_idx in count() :
        url = base_url + '?page=' + str( page_idx + 1 )
        # print( url )
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()
        
        mytable = soup.find('table', attrs={'class':'table mt20'})
        mytbody = mytable.find('tbody')

        # print('패이지 번호 : %d' % page_idx)

        shopExists = False # 매장 목록이 없다고 가정
        for mytr in mytbody.findAll('tr') :
            shopExists = True
            mylist = list(mytr.strings)
            # print( mylist )
            # print('a' * 30)

            # phone은 전화 번호입니다.
            imsiphone = mytr.select_one('td:nth-of-type(3)').string
            if imsiphone != None :
                phone = imsiphone.strip()
            else:
                phone = ""
            # print(phone)
            # print('c' * 30)

            # # td4th_a는 4번째 <td> 아래의 <a> 태그를 의미합니다.
            # td4th_a = mytr.select_one('td:nth-of-type(4)').a
            #
            # if td4th_a != None :
            #     onclidk = td4th_a.attr['onclick']
            # else:
            #     onclidk = ""
            # print(td4th_a)
            # print('d' * 30)

            store = mylist[1]
            address = mylist[3]
            #print( '{' + address + '}' )
            #print('b' * 30)

            if len(address) >= 2 :
                imsi = address.split()
                sido = imsi[0]
                gungu = imsi[1]

                mydata = [brandName, store, sido, gungu, address, phone]
                savedData.append(mydata)
        
        #if page_idx == 0 :
        if shopExists == False :
            chknStore.save2Csv( savedData ) 
            break
####################################################
print( brandName + ' 매장 크롤링 시작')
getData()
print( brandName + ' 매장 크롤링 끝')