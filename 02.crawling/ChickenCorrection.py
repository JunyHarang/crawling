import pandas as pd 

pd.options.display.max_columns = 1000
pd.options.display.max_rows = 100

class ChickenCorrection():
    myencoding = 'utf-8'

    def __init__(self, workfile):
        self.workfile = workfile
        self.myframe = pd.read_csv(self.workfile, encoding = self.myencoding, \
                                   index_col = 0 )
        # print( self.myframe.info() )
        self.correctionSido()
        self.correctionGungu()
        self.showMergeResult()
        self.correctionAddress()

        self.myframe.to_csv('allStoreModified.csv', encoding='utf-8')

    def correctionAddress(self):  # 주소지 보정하기
        try:
            for idx in range(len(self.myframe)):
                # print(self.myframe.iloc[idx])
                imsiseries = self.myframe.iloc[idx]
                addrSplit = imsiseries['address'].split(' ')[2:]
                imsiAddress = [imsiseries['sido'], imsiseries['gungu']]
                imsiAddress = imsiAddress + addrSplit
                self.myframe.iloc[idx]['address'] = ' '.join(imsiAddress)
        except TypeError as err:
            pass

    def showMergeResult(self):
        # 표준화된 행정 구역 데이터와 비교
        district = pd.read_csv('district.csv', encoding='utf-8')
        
        mergedData = pd.merge(self.myframe, district, on=['sido', 'gungu'], \
                              how='outer', suffixes=['', '_'], indicator = True )
        result = mergedData.query('_merge == "left_only"')
        # print('좌측에만 있는 데이터')
        # print( result[['sido', 'gungu', 'address']])
#         print( '[' + result[['gungu']] + ']')
        
        
    def correctionSido(self): # 시도 보정하기
        # 제거할 데이터
        self.myframe = self.myframe[ self.myframe['store'] != 'CNTTEST'] # pelicana 매장
        self.myframe = self.myframe[self.myframe['sido'] != '테스트'] # pelicana 매장
    
        # print('before sido')
        # print( np.sort(self.myframe['sido'].unique()) )
        # print('-' * 40)

        sidofile = open('sido_correction.txt', 'r', encoding='utf-8')
        linelists = sidofile.readlines()
        
#         print(linelists)
        
        sido_dict = {} # 시도 보정을 위한 사전
        for oneline in linelists :
            mydata = oneline.replace('\n', '').split(':')
#             print(mydata[1])
            sido_dict[ mydata[0] ] = mydata[1]
 
        self.myframe.sido = \
            self.myframe.sido.apply( lambda data : sido_dict.get(data, data)) 

        # print('after sido')
        # print( np.sort(self.myframe['sido'].unique()) )
        # print('-' * 40)
        
    def correctionGungu(self):
        # print('before gungu')
        # print( self.myframe['gungu'].unique() )
        # print('-' * 40)
        
        gungufile = open('gungu_correction.txt', 'r', encoding='utf-8')
        linelists = gungufile.readlines()
        
#         print(linelists)
        
        gungu_dict = {}
        for oneline in linelists :
            mydata = oneline.replace('\n', '').split(':')
#             print(mydata[1])
            gungu_dict[ mydata[0] ] = mydata[1]
 
        self.myframe.gungu = \
            self.myframe.gungu.apply( lambda data : gungu_dict.get(data, data)) 

        # print('after gungu')
        # print( self.myframe['gungu'].unique() )
        # print('-' * 40)
# end class

filename = 'allstore.csv'

chknStore = ChickenCorrection(filename)