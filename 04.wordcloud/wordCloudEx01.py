from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
import matplotlib as mpl

[f.name for f in fm.fontManager.ttflist if'Nanum'in f.name]

mpl.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.family'] = 'NanumGothic'

filename = 'steve.txt'
myfile = open(filename, 'rt', encoding='utf-8')

# read()의 return type은 string이고, readlines()는 List이다.

text = myfile.read()

print(type(text))
print('='*50)

wordcloud = WordCloud()

wordcloud = wordcloud.generate(text)

print(type(wordcloud))
print('='*50)

# text 파일에 단어들을 사전으로 만들고, 빈도수를 계산한 값을 bindo 변수에 넣는다.
# 파이썬의 사전은 기본적으로 순서를 따지지 않고 만들지만, List는 순서를 따지면서 만든다.

bindo = wordcloud.words_

print(type(bindo))
print(bindo)
print('='*50)

# lambda 옆에 x는 매개변수라고 보면 된다. reverse는 결과를 뒤집어서 정렬하게 된다.

sortedData = sorted(bindo.items(), key=lambda x : x[1], reverse=True)
print(len(sortedData))
print(sortedData)
print('='*50)

chartData = sortedData[0:10]
print(chartData)
print('='*50)

xtick = []
chart = []

for item in chartData:
    xtick.append(item[0])
    chart.append(item[1])
    
mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#FFCC00', '#CCFFBB', '#05CEFF', '#1122CC']

plt.figure()

plt.bar(xtick, chart, color=mycolor)

plt.title('상위 빈도 top 10')

filename = 'wordcloudEx01_01.png'
plt.savefig(filename, dpi=400)

print(filename + '그래프 파일이 정상적으로 저장 되었습니다!')

# 그래프가 나오는 도화지를 설정

plt.figure(figsize=(12, 12))

plt.imshow(wordcloud)

plt.axis('off')