import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator

image_file = 'alice.png'

img_file = Image.open(image_file)

print(type(img_file))
print('='*50)

alice_mask = np.array(img_file) # image를 numpy의 2차원 배열로 넣기 위해 사용

print(type(alice_mask))
print('='*50)

plt.figure(figsize=(8, 8)) # 그림의 크기를 설정

plt.imshow(alice_mask, interpolation='bilinear') # imshow는 image show의 약어이고, interpolation(보강법)은 그라데이션을 설정하는 부분이고, bilinear는 binary linear로 서서히 그라데이션이 먹는 효과로 볼 수 있다.

plt.axis('off')
filename = 'graph01.png'
plt.savefig(filename, dpi = 400)
print(filename + '이 정상적으로 저장 되었습니다!')

mystopwords = set(STOPWORDS)

# 크롤링하는 txt 파일에 제외할 문자열을 등록한다.
mystopwords.add('said')
mystopwords.update(['hohoho', 'hahaha'])

print(len(mystopwords))
print(mystopwords) # 미리 불용어로 등록된 단어들이 출력된다.

wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask, stopwords=mystopwords)

stevefile = 'steve.txt'
text = open(stevefile, 'rt', encoding='utf-8')
text = text.read()

wc = wc.generate(text)

print(wc.words_)


plt.figure(figsize=(12, 12)) # 그림의 크기를 설정

plt.imshow(wc, interpolation='bilinear') # imshow는 image show의 약어이고, interpolation(보강법)은 그라데이션을 설정하는 부분이고, bilinear는 binary linear로 서서히 그라데이션이 먹는 효과로 볼 수 있다.

plt.axis('off')
filename = 'graph02.png'
plt.savefig(filename, dpi = 400)
print(filename + '이 정상적으로 저장 되었습니다!')


alice_color_file = 'alice_color.png'
alice_color_mask = np.array(Image.open(alice_color_file))

wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask, stopwords=mystopwords, max_font_size=40, random_state=42)

wc = wc.generate(text)


plt.figure(figsize=(12, 12)) # 그림의 크기를 설정

plt.imshow(wc, interpolation='bilinear') # imshow는 image show의 약어이고, interpolation(보강법)은 그라데이션을 설정하는 부분이고, bilinear는 binary linear로 서서히 그라데이션이 먹는 효과로 볼 수 있다.

plt.axis('off')
filename = 'graph03.png'
plt.savefig(filename, dpi = 400)
print(filename + '이 정상적으로 저장 되었습니다!')



plt.figure(figsize=(12, 12)) # 그림의 크기를 설정

plt.imshow(alice_color_mask, interpolation='bilinear') # imshow는 image show의 약어이고, interpolation(보강법)은 그라데이션을 설정하는 부분이고, bilinear는 binary linear로 서서히 그라데이션이 먹는 효과로 볼 수 있다.

plt.axis('off')
filename = 'graph04.png'
plt.savefig(filename, dpi = 400)
print(filename + '이 정상적으로 저장 되었습니다!')


image_color = ImageColorGenerator(alice_color_mask)
plt.figure(figsize=(12, 12))
newwc = wc.recolor(color_func=image_color, random_state=42)

plt.imshow(newwc, interpolation='bilinear')
plt.axix('off')

filename = 'graph05.png'
plt.savefig(filename, dpi = 400)
print(filename + '이 정상적으로 저장 되었습니다!')