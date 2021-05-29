import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm
import matplotlib as mpl

#################################################################

# Box Plot은 이상치를 나타내기 위하여 사용한다.

[f.name for f in fm.fontManager.ttflist if'Nanum'in f.name]

mpl.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.family'] = 'NanumGothic'

cnt, PNG, UNDERBAR=0, '.png', '_'

CHART_NAME = 'brokenLineExam'
fileName = '../data/abc.csv'

#################################################################

data = pd.read_csv(fileName, index_col='국가')
print(data.columns)
print('='*50)

chartdata = data['4월06일']
print(chartdata)
print('='*50)
print(type(chartdata))

plt.plot(chartdata, color='blue', linestyle='solid', marker='o')

YTICKS_INTERVAL = 50000

'''
4월 6일 발생건수가 가장 높은 미국(335,524)를 VTICKS_INTERVAL(50000)으로 나눈 뒤 숫자 1을 더하고, 다시 YTICS_INTERVAL을 곱하여 maxlim(350,000)에 넣었다.
그래프에 발생건수는 350,000까지 5000씩 커지는데, 미국의 상한선보다 조금 더 높게 그래프를 보이게 하기 위해 이렇게 코딩.
'''
maxlim = (int(chartdata.max()/YTICKS_INTERVAL) + 1) * YTICKS_INTERVAL

print(maxlim)

# 0~100까지 (1100은 제외) 100씩 증가
# values = np.arange(0, 1100, 100)

values = np.arange(0, maxlim + 1, YTICKS_INTERVAL)
print(values)

# 100 단위에 콤마를 넣어주기 위해 사용
plt.yticks(values, ['%s' % format(val, ',') for val in values])

plt.grid(True)
plt.xlabel('국가명')
plt.ylabel('발생 건수')
plt.title('04월06일 코로나 발생 건수')

cnt += 1

saveFile=CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG

plt.savefig(saveFile, dpi=400)

print(saveFile + ' 의 파일 저장이 완료 되었습니다!')

#################################################################

COUNTRY = ['한국', '스위스', '이란', '영국', '프랑스', '독일', '이탈리아', '스페인', '미국', '중국']
WHEN = ['4월06일', '4월07일', '4월08일', '4월09일', '4월10일']

chartdata = data.loc[COUNTRY, WHEN]
chartdata = chartdata.T

print(chartdata)
print('='*50)


chartdata.plot(title='Some Title', marker='o', rot=0, legend=True, figsize=(10, 6))

plt.grid(True)
plt.xlabel('일자')
plt.ylabel('국가명')
plt.title('일자별 국가명 꺽은 선')

cnt += 1

saveFile=CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG

plt.savefig(saveFile, dpi=400)

print(saveFile + ' 의 파일 저장이 완료 되었습니다!')

#################################################################

tipsFile = '../data/tips.csv'
myFrame = pd.read_csv(tipsFile)
print(type(myFrame))
print(myFrame.columns)

# 슬라이싱 (어디서부터 어디까지) / total_bill = 250개 이다.
dataBill = myFrame.loc[:, ['total_bill']]
dataTip = myFrame.loc[:, ['tip']]

fig, ax1 = plt.subplots()
ax1.set_title('결재 금액과 tip(이중축)')

xrange = range(len(myFrame))
color = 'tab:red'
ax1.set_ylabel('결재금액', color=color)

# plot(x축, y축)
ax1.plot(xrange, dataBill, color=color)
ax1.tick_params(axis='y', labelcolor=color)


ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Tip(팁)', color=color)

# plot(x축, y축)
ax2.plot(xrange, dataTip, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()

cnt += 1

saveFile=CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG

plt.savefig(saveFile, dpi=400)

print(saveFile + ' 의 파일 저장이 완료 되었습니다!')

#################################################################

print('brokenLineExam 프로그램이 정상적으로 종료 되었습니다!')