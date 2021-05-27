import matplotlib.pyplot as plt
import pandas as pd

csv_file = './../02.crawling/allStoreModified.csv'

# read_csv는 csv Data를 읽어오기 위해 사용

myframe = pd.read_csv(csv_file, index_col=0, encoding='utf-8')

print (myframe.info())

print('='*50)

#  DB에서 distict와 같은 역할이 'unique()이다. 자료 중 필요한 것만 빼 올 때 사용한다.

# 반환 결과 List

print(myframe['brand'].unique())

print('='*50)

mygrouping = myframe.groupby(['brand'])['brand']

print(type(mygrouping))

print('='*50)

chartdata = mygrouping.count()

print(type(chartdata))

print(chartdata)

print('='*50)

plt.figure()

mycolor = ['r', 'g', 'b', 'm']

print(chartdata.index)

print('='*50)

brand_dict = {'cheogajip':'처가집', 'goobne':'굽네', 'pelicana':'페리카나','nene':'네네'}

# List comprehension(newindex = [brand_dict[idx] for idx in chartdata.index])
# chartdata.index(4개)라는 복수개를 idx에 하나씩 넣고, 그 idx를 brand_dict key로 찾으면 value가 나오는 형식

newindex = [brand_dict[idx] for idx in chartdata.index]
chartdata.index = newindex

import matplotlib.pyplot as plt

plt.rcParams['font.family']='NanumGothic'

plt.figure()

chartdata.plot(kind='pie', legend=False, autopct = '%1.2f%%', colors=mycolor)

filename = 'makeChickenGraph01.png'

plt.savefig(filename, dpi=400)

print(filename + '파일이 정상적으로 저장 되었습니다!')


plt.figure()

chartdata.plot(kind='barh', legend=False, title='브랜드별 총 매장 개수', rot=30, color=mycolor)

filename = 'makeChickenGraph02.png'

plt.savefig(filename, dpi=400)

print(filename + '파일이 정상적으로 저장 되었습니다!')

# plt.show()


# py:201: RuntimeWarning: Glyph 45208 missing from current font. font.set_text(s, 0, flags=flags) 한글 깨짐 처리를 해줘야 하는 오류
# plt.rcParams['font.family']='Malgun Gothic'로 해결함.