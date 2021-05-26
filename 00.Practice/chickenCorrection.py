import numpy as np
import pandas as pd

class chickenCorrection():
    myencoding = 'utf-8'

    def __init__(self, workfile):
        self.workfile = workfile
        self.myframe = pd.read_csv(self.workfile, encoding=self.myencoding, index_col=0)

        # print(self.myfram.head())

        # print(self.myfram.info())

        self.correctionSido()

        self.correctionGungu()

        self.showMergeResult()

        self.correctionAddress()

        # self.myfram.to_csv('allstoreModified.csv', encoding=self.myencoding)

    def correctionSido(self):
        self.myframe = self.myframe[self.myframe['store'] != 'CNTTEST']
        self.myframe = self.myframe[self.myframe['sido'] != '테스트']

        print('Befor sido')

        print(self.myframe['sido'].unique())

        print('='*100)
        
        
        
        sidofile = open('sido_correction.txt', 'r', encoding=self.myencoding)
        
        linelists = sidofile.readlines()
        
        # print(type(linelists())
        
        # print(linelists)
        
        sido_dict = {} # dict() 이렇게 해도 된다.
        
        for oneline in linelists:
            mydata = oneline.replace('\n', '').split(':')
            # print(mydata)
            sido_dict[mydata[0]] = mydata[1]    # 사전에 Key값은 mydata의 0번째 원소를 Value는 mydata의 1번째 원소를 사용
            
        # print(sido_dict)
        
        self.myframe.sido = \
            self.myframe.sido.apply(lambda data : sido_dict.get(data, data))
            
        print('After sido')
        
        print(np.sort(self.myframe['sido'].unique()))
        
    # end def correctionSido(self)

    def correctionGungu(self):
        pass

    def chowMergeResult(self):
        pass

    def correctionAddress(self):
        pass

filename = 'allstore.csv'
chknStore = chickenCorrection(filename)
        
print('chickenCorrection의 작업이 모두 완료 되었습니다!')