import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import matplotlib as mpl

#################################################################

# Box Plot은 이상치를 나타내기 위하여 사용한다.

[f.name for f in fm.fontManager.ttflist if'Nanum'in f.name]

mpl.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.family'] = 'NanumGothic'

cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'boxPlotExam'
filename = '../data/tips.csv'

#################################################################

myframe = pd.read_csv(filename, encoding='utf-8', index_col=0)

print(myframe['time'].unique())

DINNER, LUNCH = 'Dinner', 'Lunch'

# for Dinner
frame01 = myframe.loc[myframe['time'] == DINNER, 'total_bill']
frame01.index.name = DINNER
print(frame01.head())
print('='*50)

# for Lunch
frame02 = myframe.loc[myframe['time'] == LUNCH, 'total_bill']
frame01.index.name = LUNCH
print(frame02.head())
print('='*50)

chartcata = [np.array(frame01), np.array(frame02)]
print(chartcata)
print('='*50)

xtick_label = ['저녁', '점심']

# fig(figure는 그림 - 도화지)
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

bplot1 = ax1.boxplot(chartcata)

# vert = verical의 줄임말로 수직 정렬 방식을 Control
bplot1 = ax1.boxplot(chartcata, vert=True, patch_artist=True, labels=xtick_label)
ax1.set_title('상자 수염(noNotch)')

# print(type(bplot1))
# print(bplot1)

bplot2 = ax2.boxplot(chartcata, vert=True, patch_artist=True, labels=xtick_label, notch=True)
ax2.set_title('상자 수염(Notch)')

colors = ['pink', 'lightblue']

for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('점심과 저녁 Tip')
    ax.set_ylabel('관찰 데이터')
        
plt.show()

cnt += 1

saveFile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG

plt.savefig(saveFile, dpi=400)

print(saveFile + '의 파일 저장이 완료 되었습니다!')

plt.show()