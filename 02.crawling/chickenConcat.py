import pandas as pd
from pandas import DataFrame

myencoding='utf-8'
# chickenList=['cheogajip', 'goobne', 'kyochon', 'nene', 'pelicana', 'bbq']
chickenList=['cheogajip', 'goobne', 'nene', 'pelicana']

newframe=DataFrame()
print( newframe )
print('-' * 40)

for onestore in chickenList :
    filename=onestore + '.csv'
    myframe=pd.read_csv(filename, index_col=0, encoding=myencoding)
    newframe=pd.concat([newframe, myframe], axis=0, ignore_index=True )
    
    print( myframe.head() )
    print('-' * 40)

print('a' * 40)
pd.options.display.max_columns = 10
print( newframe.head() )
print('-' * 40)    

totalfile='allstore.csv'    
newframe.to_csv(totalfile, encoding='utf-8')
newframe.info()
print( totalfile + ' 파일 저장 완료' )
print('-' * 40) 