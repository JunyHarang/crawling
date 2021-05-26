import numpy as np
import pandas as pd

pd.options.display.max_columns = 1000
pd.options.display.max_rows = 1000

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

        self.myfram.to_csv('allstoreModified.csv', encoding=self.myencoding)
        print('파일 저장이 완료 되었습니다!')

    def correctionSido(self):
        self.myframe = self.myframe[self.myframe['store'] != 'CNTTEST']
        self.myframe = self.myframe[self.myframe['sido'] != '테스트']

        # print('Befor sido')

        # print(self.myframe['sido'].unique())

        # print('='*100)

        sidofile = open('sido_correction.txt', 'r', encoding=self.myencoding)

        linelists = sidofile.readlines()

        # print(type(linelists())

        # print(linelists)

        # dict() 이렇게 해도 된다.

        sido_dict = {}

        for oneline in linelists:
            mydata = oneline.replace('\n', '').split(':')
            # print(mydata)

            # 사전에 Key값은 mydata의 0번째 원소를 Value는 mydata의 1번째 원소를 사용
            sido_dict[mydata[0]] = mydata[1]

        # print(sido_dict)

        self.myframe.sido = \
            self.myframe.sido.apply(lambda data: sido_dict.get(data, data))

        # print('After sido')

        # print(np.sort(self.myframe['sido'].unique()))

    # end def correctionSido(self)

    def correctionGungu(self):
        # print('Befor gungu')
        # print(self.myframe['gungu'].unique())
        # print('='*100)

        gungufile = open('gungu_correction.txt', 'r', encoding=self.myencoding)
        linelists = gungufile.readlines()

        gungu_dict = {}

        for oneline in linelists:
            mydata = oneline.replace('\n', '').split(':')
            gungu_dict[mydata[0]] = mydata[1]

        self.myframe.gungu = \
            self.myframe.gungu.apply( lambda data : gungu_dict.get(data, data))

        # print('After gungu')
        # print(self.myframe['gungu'].unique())
        # print('='*100)

    # end def correctionGungu(self)

    def showMergeResult(self):
        district = pd.read_csv('district.csv', encoding=self.myencoding)

        # print(district.info())

        '''merge()는 DB에서의 Join과 비슷하다. 두 개의 DataFrame 중 열 개수가 늘어나게 한다. (DB의 union과 비슷), on은 DB에서 join할 때 비슷한 
           컬럼들을 써주게 되는데, 그 개념과 비슷하다.
            how에 outer join을 위해 outer라고 명시, 
        '''
        mergedata = pd.merge(self.myframe, district, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator = True )

        # print(mergedata.head(10))

        result = mergedata.query('_merge == "left_only"')

        print("왼쪽에만 있는 데이터")

        print(result[['sido', 'gungu', 'address']])

    def correctionAddress(self):
        try :
            # len()는 0부터 매개변수 개수 -1개를 반환한다.
            for idx in range(len(self.myframe)):
                # series는 자바에선 bean이고, DB에선 Row와 같은 개념
                imsiseries = self.myframe.iloc[idx]
                # print(idx)

                addrSplit = imsiseries['address'].split(' ')[2:]
                # print(addrSplit)
                imsiAddress = [imsiseries['sido'], imsiseries['gungu']]
                imsiAddress = imsiAddress + addrSplit

                # print(imsiAddress)
                # print('='*100)

                # idx번째 address에 imsiaddress를 Write하는데, 띄어쓰기 구분자를 넣는다.
                self.myframe.iloc[idx]['address'] = ' '.join(imsiAddress)

        except TypeError as err:
            pass

filename = 'allstore.csv'
chknStore = chickenCorrection(filename)

print('chickenCorrection의 작업이 모두 완료 되었습니다!')