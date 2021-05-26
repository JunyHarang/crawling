from email.headerregistry import Address
import re # 정규 표현식 모듈 불러오기

from itertools import count

from numpy import save

from ChickenUtil import ChickenStore    # ChickenUtil 이라는 Class 안에 ChickenStore()를 불러온다.

##########################################################################################################
brandName = '네네치킨'
base_url = 'https://nenechicken.com/17_new/sub_shop01.asp'
##########################################################################################################
def getData():

    savedData = [] # 액셀로 저장될 List 선언

    for page_idx in range(1, 46 + 1) :
        url = base_url + '?page%d' % (page_idx)

        chnkStore = ChickenStore(brandName, url)

        soup = chnkStore.getSoup()

        # print (type(soup))

        tablelists = soup.findAll('table', attrs={'class':'shopTable'})
        # print(len(tablelists))

        for onetable in tablelists :
            store = onetable.select_one('.shopName').string

            tmp = onetable.select_one('.shopAdd').string

            if tmp == None :
                continue

            # print('tmp\n' + tmp)

            imsi = tmp.split()
            sido = imsi[0]
            gungu = imsi[1]

            # 주소 접미사
            im_address = onetable.select_one('.shopMap')
            im_address = im_address.a['href']

            # 정규 표현식으로 숫자가 처음으로 나오는 위치부터 문자열 추출
            regex = '\d\s*'         # 숫자로 시작하는 부분
            pattern = re.compile(regex)
            mymatch = pattern.search(im_address)

            addr_suffix = mymatch.group().replace("');",'')

            # print(addr_suffix)

            address = tmp + ' ' + addr_suffix

            phone = onetable.select_one('.tooltiptext').string

            # print(sido + '/' + gungu)

            mydata = [brandName, store, sido, gungu, address, phone]
            
            savedData.append(mydata)
            
    # print(savedData)

    chnkStore.save2Csv(savedData)

            # break
##########################################################################################################
print(brandName + ' 크롤링을 시작 합니다!')
getData()
print(brandName + ' 크롤링이 종료 되었습니다!')

