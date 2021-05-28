import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl

[f.name for f in fm.fontManager.ttflist if'Nanum'in f.name]

mpl.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.family'] = 'NanumGothic'

filename = 'pusanHospitalExcel.csv'

myframe = pd.read_csv(filename, encoding='utf-8')

# csv의 컬럼 정보, None정보, Data Type을 출력(pandas에서는 문자열을 object로 인식)
print(myframe.info())

print('='*50)


# csv의 컬럼의 수치형 Data 중 통계 정보를 출력한다. (평균 = mean, std = 표준편차, 등등) option을 넣으면 더 많은 정보를 볼 수 있다.
print(myframe.describe())

print('='*50)


# CSV의 컬럼 정보, Data Type만을 간략하게 출력
print(myframe.columns)

print('='*50)

# CSV의 'instit_kind'의 범주형 값 출력
# 범주형은 막대기, pi로 Graph를 그리는 것이 좋다.
print(myframe['instit_kind'].unique())

print('='*50)

''' 
groupby의 앞의 소괄호는 그룹 하고자 하는 컬럼을 넣고, 뒤의 대괄호에는 연산을 하고자 하는 컬럼을 넣는다.
현재 instit_kind는 ['약국' '의원' '치과의원' '한의원' '병원' '한방병원' '요양병원' '치과병원' '보건지소' '보건진료소' '종합병원' '보건소'] 값이 있고, 이것들을 약국은 
약국끼리 병원은 병원끼리 그룹핑을 하여 대괄호에 넣어준 연산을 할 수 있다.(총합, 평균, 표준편차 등등) 
'''
mygrouping = myframe.groupby(['instit_kind'])['instit_kind']

# 범주형은 막대기, pi로 Graph를 그리는 것이 좋다.
print(type(mygrouping))

print('='*50)

# 각각의 컬럼들을 그룹핑한 값에 개수를 count하여 chartdata 변수에 넣는다.
chartdata = mygrouping.count()

# chartdata의 DataType을 출력하고, 안에 어떤 값이 있는지 출력
print(type(chartdata))
print(chartdata)
print('='*50)

# chartdata 중 1000보다 큰 값만 추려서 newdata에 넣는다.
newdata = chartdata[chartdata > 1000]
print(newdata)
print('='*50)

mycolor = ['r','g','b','m']

plt.figure()

newdata.plot(kind='pie', legend=True, autopct='%6.3f%%')
saveFileName = 'getHostpitalInfo01.png'
plt.savefig(saveFileName, dpi=400)

print(saveFileName + '의 저장이 완료 되었습니다!')


plt.figure()

# rot은 글자의 기울임을 각도로 나타내는 것
newdata.plot(kind='bar', legend=False, title='부산 지역 병/의원 현황 Top 4', color=mycolor, rot=0)
saveFileName = 'getHostpitalInfo02.png'
plt.savefig(saveFileName, dpi=400)

print(saveFileName + '의 저장이 완료 되었습니다!')