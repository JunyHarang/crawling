import pandas as pd
from pandas import DataFrame

myencoding = 'utf-8'

chickenList = ['페리카나', '네네치킨', '처가집', '굽네치킨']

# chickenList = ['페리카나']

#비어 있는 DataFram(2차원 표) 선언
newframe = DataFrame()

for onestore in chickenList:
    filename = onestore + '.csv'
    myframe = pd.read_csv(filename, index_col=0, encoding=myencoding)

    # print(myframe.head())
    # print('-'*100)

    # concat은 UNION과 유사하고, 행을 합치는 것이다.
    newframe = pd.concat([newframe, myframe], axis=0, ignore_index=False)

print(newframe.info())

totalfile = 'allstore.csv'

newframe.to_csv(totalfile, encoding=myencoding)

print(totalfile + ' 파일이 저장 되었습니다! ')