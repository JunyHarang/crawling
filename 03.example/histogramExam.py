# 정규분포곡선 : 평균을 중심으로 왼쪽은 작은 값, 오른쪽은 큰 값을 나타낼 때 사용

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm
import matplotlib as mpl

#################################################################

# Box Plot은 이상치를 나타내기 위하여 사용한다.

programName = 'histogramExam'

[f.name for f in fm.fontManager.ttflist if'Nanum'in f.name]

mpl.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.family'] = 'NanumGothic'

cnt, PNG, UNDERBAR=0, '.png', '_'

CHART_NAME = 'histogramExam'
fileName = '../data/tips.csv'

#################################################################

tips = pd.read_csv(fileName, encoding='utf-8')

print(tips.columns)
print('='*100)

# Series
x = tips['total_bill']
print(type(x))


# 그래프를 그릴 도화지 만들기
numBins = 50

# fig는 그래프를 그릴 도화지이고, ax는 그래프라고 이해.
fig, ax = plt.subplots()

# numBins는 그래프의 솟은 그래프의 개수(눈금의 넓이 / 솟은 그래프의 넓이)
''' density(밀도) True = 전체적인 밀도를 보여줌(솟은 그래프의 값을 모두 더하면 1이 되게 보여줌), 
    False = 도수의 개수대로 보여줌(솟은 그래프의 값을 모두 더하면 열의 총 개수가 나온다.)
'''
n, bins, patches = ax.hist(x, numBins, density=True)

# 그래프 제목, 행, 열축 이름 설정
ax.set_title('히스토그램')
ax.set_xlabel('Frequency')
ax.set_ylabel('total bill')

mu = x.mean()  # 평균
print('mu :', mu)

sigma = x.std() # 표준 편차
print('sigma :', sigma)

# 표준 정규 분포 공식
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()

# 파일 저장(.png)
cnt += 1

saveFile=CHART_NAME + str(cnt).zfill(2) + PNG

plt.savefig(saveFile, dpi=400)

print(saveFile + ' 의 파일 저장이 완료 되었습니다!')

humanFile = '../data/human_height.csv'

human = pd.read_csv(humanFile, encoding = 'utf-8')

fig, axes = plt.subplots(nrows=1, ncols=2)

giant = human['giant']
dwarf = human['dwarf']

''' 
    hist() = histogram을 말하고, range() = 범위이다. 여기선 키 이기 때문에 최소값과 최대값으로 사용, 
    alpah = 그래프의 투명도이다.
'''
axes[0].hist(giant, range=(210, 290), bins=20, alpha=0.6)
axes[1].hist(dwarf, range=(100, 180), bins=20, alpha=0.6)

axes[0].set_title('큰 사람 나라의 키')
axes[1].set_title('작은 사람 나라의 키')

# 파일 저장(.png)
cnt += 1

saveFile=CHART_NAME + str(cnt).zfill(2) + PNG

plt.savefig(saveFile, dpi=400)

print(saveFile + ' 의 파일 저장이 완료 되었습니다!')

#################################################################

#2개의 histogram 같이 그리기
fig, axes = plt.subplots()

axes.hist(giant, bins=20, alpha=0.6)
axes.hist(dwarf, bins=20, alpha=0.6)

cnt += 1

saveFile=CHART_NAME + str(cnt).zfill(2) + PNG

plt.savefig(saveFile, dpi=400)

print(saveFile + ' 의 파일 저장이 완료 되었습니다!')

#################################################################

fig, axes = plt.subplots()

#stack histogram 그리기
man = human['man']
woman = human['woman']
x = np.array([man, woman]).T

print(x)

# shape은 형상을 나타낸다.
print(x.shape)

# stacked가 True이면 누적을 하겠다는 것이다.
axes.hist(x, bins=numBins, density=False, histtype='bar', stacked=True)

axes.set_title('누적 히스토그램')

cnt += 1

saveFile=CHART_NAME + str(cnt).zfill(2) + PNG

plt.savefig(saveFile, dpi=400)

print(saveFile + ' 의 파일 저장이 완료 되었습니다!')
#################################################################

print(programName + '의 프로그램이 정상적으로 종료 되었습니다!')