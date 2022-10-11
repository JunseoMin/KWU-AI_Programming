import selenium
import wordcloud
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
wordcloud.wordcloud(font_path='C:\Windows\Fonts\HYHeadLine-Medium.ttf')
driver = webdriver.Chrome("C:\chromedriver\chromedriver")
url = "https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8"
Xpath='//*[@id="jWZtJ8Cjb"]/div[2]/div/div/div[1]'
driver.get(url)
#Xpths
KBO=driver.find_elements(By.XPATH,Xpath)

for value in KBO:
        kboText=value.text

delword=wordcloud.STOPWORDS.union({'을,를,있다,없다'})
image=wordcloud.WordCloud(width=1000,height=700,stopwords=delword).generate(kboText)

plt.figure(figsize=(40,30))
plt.imshow(image)
plt.show()