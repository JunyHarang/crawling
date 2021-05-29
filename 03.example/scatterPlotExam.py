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

CHART_NAME = 'scatterPlotExam'
fileName = '../data/mpg.csv'

#################################################################

print('스타일 목록은 다음과 같습니다. \n' + str(plt.style.available))
print('='*50)

mpg = pd.read_csv(fileName, encoding='utf-8')
print(mpg.columns)
print('='*50)

# 엔진크기
xdata = mpg.loc[:, ['displ']]

# 주행 마일수
ydata = mpg.loc[:, ['hwy']]

# marker=o는 circle을 의미(참고 사이트: https://matplotlib.org/stable/api/markers_api.html?highlight=markers#module-matplotlib.markers)
plt.figure()
plt.plot(xdata, ydata, linestyle='None', marker='o')
plt.xlabel('엔진 크기')
plt.ylabel('주행 마일수')
plt.title('산점도 그래프')
plt.grid(True)

# 파일 저장(.png)
cnt += 1

saveFile=CHART_NAME + str(cnt).zfill(2) + PNG

plt.savefig(saveFile, dpi=400)

print(saveFile + ' 의 파일 저장이 완료 되었습니다!')

#################################################################

labels = mpg['drv'].unique()
print(labels)

mycolor = ['r', 'g', 'b']
plt.figure()
idx = 0
label_dict = {'f':'전륜 구동', '4':'4륜 구동', 'r':'후륜 구동'}

for finditem in labels : # ['f', '4', 'r']
    xdata = mpg.loc[mpg['drv'] == finditem, 'displ']
    ydata = mpg.loc[mpg['drv'] == finditem, 'hwy']
    
    plt.plot(xdata, ydata, linestyle='None', marker='o', label=label_dict[finditem], color=mycolor[idx])
    
    idx += 1
    
plt.legend()
plt.xlabel('엔진 크기')
plt.ylabel('주행 마일수')
plt.title('산점도 그래프')
plt.grid(True)

# 파일 저장(.png)
cnt += 1

saveFile=CHART_NAME + str(cnt).zfill(2) + PNG

plt.savefig(saveFile, dpi=400)

print(saveFile + ' 의 파일 저장이 완료 되었습니다!')

#################################################################

# Create Fig and gridspec
fig = plt.figure(figsize=(16, 10), dpi= 80)
grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.2)

# 축을 정의합니다.
ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])

# 메인 그래프에 산점도를 그립니다.
ax_main.scatter('displ', 'hwy', s=mpg.cty*4, c=mpg.manufacturer.astype('category').cat.codes, alpha=.9, data=mpg, cmap="tab10", edgecolors='gray', linewidths=.5)

# 하단의 histogram
ax_bottom.hist(mpg.displ, 40, histtype='stepfilled', orientation='vertical', color='lightpink')
ax_bottom.invert_yaxis()

# 오른쪽 histogram
ax_right.hist(mpg.hwy, 40, histtype='stepfilled', orientation='horizontal', color='lightblue')

# Decorations
ax_main.set(title='산점도(엔진의 크기 vs 주행 마일수)', xlabel='엔진의 크기', ylabel='주행 마일수')
ax_main.title.set_fontsize(20)
for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
    item.set_fontsize(14)

xlabels = ax_main.get_xticks().tolist()

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + ' 파일이 저장되었습니다.')

####################### 다이아몬드형 산점도 그래프 ##############################

# 파일 내 컬럼: carat(무게), cut(품질), color(색상), clarity, depth, table(상단 넓이), price(가격)
# price와 depth를 이용한 산점도 그래프, table을 이용하여 원의 크기를 다르게 만들기
# 샘플링
diamondFile = '../data/diamonds.csv'

diamonds = pd.read_csv(diamondFile)

print(diamonds)
print('='*100)

fraction = 0.005

diamonds = diamonds.sample(frac=fraction)

xdata = diamonds['price']
ydata = diamonds['depth']
table = diamonds['table']

cutList = diamonds['cut'].unique()

print(cutList)

mycolor = ['r', 'g', 'b', 'y', 'm']

cutList = diamonds['cut'].unique()

print(cutList)

cutDict = {cutList[idx] : mycolor[idx] for idx in range(len(cutList))}

print(cutDict)
print('='*100)

def record_cut(cut):
    return cutDict[cut]

# newcut이라는 새로운 컬럼 만들기. apply()는 새로운 함수를 적용한다는 뜻.
diamonds['newcut'] = diamonds['cut'].apply(record_cut)
newcut = diamonds['newcut']

def record_table(table):
    if table >= 60:
        return 100
    
    elif table >= 58:
        return 30
    
    elif table >= 54:
        return 5
    
    else :
        return 1

diamonds ['newtable'] = diamonds['table'].apply(record_table)
newtable = diamonds['newtable']

scatterPlot = plt.figure()

ax1 = scatterPlot.add_subplot(1, 1, 1)
ax1.scatter(x=xdata, y=ydata, s=newtable, c=newcut, alpha=0.8)

#################################################################

print(programName + '의 프로그램이 정상적으로 종료 되었습니다!')