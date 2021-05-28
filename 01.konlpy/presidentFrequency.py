from PyKomoran import Komoran
import matplotlib.pyplot as plt
import nltk
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.font_manager as fm
import matplotlib as mpl

[f.name for f in fm.fontManager.ttflist if'Nanum'in f.name]

mpl.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.family'] = 'NanumGothic'

class Visualization:
    def __init__(self, wordList):
        self.wordList = wordList
        self.wordDict = dict(wordList)
    # def __init__(self, wordList) 끝
    
    def makeWordCloud(self):
        aliceColorFile = '../04.wordcloud/alice_color.png'
        aliceColoring = np.array(Image.open(aliceColorFile))
        
        fontPath = 'NanumGothic.ttf'
        wordcloud = WordCloud(font_path=fontPath, mask=aliceColoring, relative_scaling=0.2, background_color='black')
        # generate는 무조건 생성이라고 생각하고, frequencies는 발생 빈도를 나타낸다. 즉, 사전에 있는 내용들에 빈도를 가져오라는 의미이다.
        wordcloud = wordcloud.generate_from_frequencies(self.wordDict)
        
        image_colors = ImageColorGenerator(aliceColoring)
        
        wordcloud = wordcloud.recolor(color_func=image_colors, random_state=42)
        
        plt.imshow(wordcloud)
        
        plt.axis('off')
        
        fileName = 'myWorldClound.png'
        plt.savefig(fileName, dpi=400)
        print(fileName + '의 파일이 저장 되었습니다!')
    # def makeWordCloud(self) 끝
    
    def makeBarChart(self):
        plt.figure(figsize=(12, 8))
        
        barCount = 10
        
        # 0:10 이면 0부터 10까지인데, 앞에 생략을 하면 0부터 이다.
        result = self.wordList[:barCount]
        
        #차트 수치
        chartData = [] 
        
        # 글씨
        fontData = []
        
        for idx in range(len(result)):
            chartData.append(result[idx][1])
            fontData.append(result[idx][0])
            
            # 60건 출력을 하도록 한다.
            value = str(chartData[idx]) + '건'
            
            plt.text(x=idx, y=chartData[idx] -5, s=value, fontsize=8, horizontalalignment='center')
            
        mycolor = ['r', 'g', 'b', 'y', 'b', 'c', '#FFCC00', '#CCFFBB', '#05CCFF', '#11CCFF']
            
        plt.bar(range(barCount), chartData, align='center', color=mycolor)
            
        plt.title('상위 ' + str(barCount) + '빈도 수')
            
        xlow, xhigh = - 0.5, barCount - 0.5
            
        plt.xlim([xlow, xhigh])
        plt.ylim([0, 50])
        plt.xlabel('주요 키워드')
        plt.ylabel('빈도수')
            
        fileName = 'MyBarChart.png'
            
        plt.savefig(fileName, dpi=400)
            
        print(fileName + '의 파일이 저장 되었습니다!')
    # def makeBarChart(self) 끝
    
# Class Visualization 끝

fileName = 'moon.txt'

koConText = open(fileName, encoding='utf-8').read()

print(type(koConText))
print('='*50)

# komoran의 기능을 사용하기 위하여 불러오기
komo = Komoran('STABLE')

# Text 파일 안에 명사만을 꺼내기 위한 작업
tokenCorea = komo.nouns(koConText)

print(tokenCorea)
print('='*50)

stopWordFile = 'stopword.txt'
stopFile = open(stopWordFile, 'rt', encoding='utf-8')
stopWords = [ word.strip() for word in stopFile.readlines()]

print(stopWords)
print('='*50)

# moon.txt에서 뽑아온 단어들에서 stopword에 들어 있는 단어들은 빼고, tokenCorea에 넣는다.
print(len(tokenCorea))
tokenCorea = [eachWord for eachWord in tokenCorea if eachWord not in stopWords]
print(len(tokenCorea))

# text안에 단어 조각들을 모아서 vocab()안에 most_common으로 빈도가 제일 많은 것들을 정렬하여 1000개만 가져와서 corea에 넣는다.
corea = nltk.Text(tokens=tokenCorea)
data = corea.vocab().most_common(1000)

print(data)
print(len(data))
print('='*50)

wordList = list()

# data변수에 텍스트 중, 글자가 word로 들어가고, count에 숫자가 들어간다. 
for word, count in data:
    if count >= 1 and len(word) >= 2: # count가 1 이상이고, word가 2글자 이상이라면?
        wordList.append((word, count))    # wordList에 글자와 숫자를 추가한다. 여기서 매개변수는 두 개가 아니고, 하나로 보아야 한다.

print(wordList)
print('='*50)

visual = Visualization(wordList)
visual.makeWordCloud()
visual.makeBarChart()

print('프로그램이 모두 완료 되었습니다!')