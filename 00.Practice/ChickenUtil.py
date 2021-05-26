from multiprocessing.connection import wait
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import ssl
import datetime
from selenium import webdriver
import time

class ChickenStore():

   

    def save2Csv(self, result) :
        mycolumn = ['brand', 'storeName', 'sido', 'gungu', 'storeAddress', 'phone']
        data = pd.DataFrame(result, columns=mycolumn)
        data.to_csv(self.brandName + '.csv', encoding='utf-8', index=True)
        print(self.brandName + '파일이 생성되었습니다!')

    def getSoup(self):

        if self.soup == None:
            return None

        else :
            return BeautifulSoup(self.soup, 'html.parser')

    def get_request_url(self):
        
        request = urllib.request.Request(self.url)
        
        try:
            context = ssl._create_unverified_context()
        
            response = urllib.request.urlopen(request, context=context)

            # Servercode 가 200 (OK)라면?
            if response.getcode() == 200:
                # print('[%s] url request success' % datetime.datetime.now())

                if self.brandName != 'pelicana':
                    return response.read().decode('utf-8')
        
                else:
                    return response

        except Exception as err:
        
            print(err)
        
            now = datetime.datetime.now()
        
            msg = '[%s] error for url %s' % (now, self.url)
        
            print(msg)
        
            return None

    def __init__(self, brandName, url):
        
        self.brandName = brandName
        
        self.url = url

        if self.brandName != 'goobne' :
            self.soup = self.get_request_url()
            self.driver = None

        else : # 굽네 매장이라면
            self.soup = None

            #filepath = '/usr/local/bin/geckodriver'
            self.driver = webdriver.Firefox()
            self.driver.get(self.url)

        print(brandName)
        print(url)

    def getWebDriver(self, cmdJavaScript):
        print(cmdJavaScript)
        self.driver.execute_script(cmdJavaScript)
        wait = 5
        time.sleep(wait)
        mypage = self.driver.page_source
        return BeautifulSoup(mypage, 'html.parser')

    # pass    # pass 는 작업이 실패해도 넘어가라는 뜻