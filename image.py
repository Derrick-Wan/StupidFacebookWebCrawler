from wordcloud import WordCloud, ImageColorGenerator
import pymysql
import re
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

total = ""

db = pymysql.connect("120.78.148.41", "root", "Wanzy19981222", "FacebookData", use_unicode=True, charset="utf8")
cursor = db.cursor()
cursor.execute("select publish from facebookInfo")
a = cursor.fetchall()
for i in range(len(a)):
    total += str(a[i]) + " "

left = ""
left += re.sub('[^a-zA-Z]', ' ', total)
print(left)
text = left.lower()
listOfWord = text.split()
word = {'and', 'the', 'with', 'in', 'by', 'its', 'for', 'of', 'an', 'to', 'a', 'com', 'see', 'on', 'is', 'more', 'that',
        'your', 's', 'from', 'are', 'you', 'it', 'this',
        'have', 'at', 'be', 'www', 'how', 'us', 'we', 'was', 'https', 'or', 'as', 'has', 'been',
        'can', 'says', 'after', 'all', 'new', 'i', 'will', 'out', 'not', 'they', 'what', 'using', 'details', 'were',
        'our', 'over', 'u', 'about', 'but', 'my', 'which'}
for i in word:
    while i in listOfWord:
        listOfWord.remove(i)
final = ''

for i in range(len(listOfWord)):
    final = final + listOfWord[i]
    final += " "
print(final)
WEB_MASK = np.array(Image.open(r"web.png"))
genclr = ImageColorGenerator(WEB_MASK)
MyWordCloud = WordCloud(background_color="white",
                        max_words=500,
                        max_font_size=50,
                        random_state=42,
                        mask=WEB_MASK,
                        color_func=genclr,
                        width=1600, height=1200, margin=2)
MyWordCloud.generate(final)

# create coloring from image
# image_colors = ImageColorGenerator(WEB_coloring)
MyWordCloud.to_file("picture.png")
