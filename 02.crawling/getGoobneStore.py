# https://sites.google.com/a/chromium.org/chromedriver/downloads
from itertools import count
from ChickenUtil import ChickenStore
####################################################
brandName = 'goobne'
base_url = 'http://www.goobne.co.kr/store/search_store.jsp'
####################################################
def getData():
    savedData = []
    chknStore = ChickenStore(brandName, base_url)
    
    bEndPage = True
    
    for page_idx in count():        
        print('%s번째 페이지가 호출됨' % str( page_idx + 1 ))
        bEndPage = False
        
        cmdJavaScript = "javascript:store.getList('%s')" % str( page_idx + 1 )
        soup = chknStore.getWebDriver( cmdJavaScript )
        #print( soup )
        
        store_list = soup.find('tbody', attrs = {'id':'store_list'})
        
        mytrlists = store_list.findAll('tr')
        
        for onestore in mytrlists :
            mytdlists = onestore.findAll('td')

            # print('a'*50)
            # print(mytdlists)

            if len( mytdlists ) > 1 :
                store = onestore.select_one('td:nth-of-type(1)').get_text(strip=True)
                phone = onestore.select_one('td:nth-of-type(2)').a.string
                address = onestore.select_one('td:nth-of-type(3)').a.string
                imsi = str(address).split(' ')
                sido = imsi[0]
                gungu = imsi[1]
                #print([brandName, store, sido, gungu, address])
                #print('a' * 40)

                savedData.append( [brandName, store, sido, gungu, address, phone] )

            else : # 마지막 페이지는 <td> 태그가 1개이더라
                bEndPage = True
                break
                
        if bEndPage == True :
            break 
        # end inner for     
    # end outer for

    chknStore.save2Csv( savedData )
####################################################
print( brandName + ' 매장 크롤링 시작')
getData()
print( brandName + ' 매장 크롤링 끝')