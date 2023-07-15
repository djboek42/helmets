# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

driver = webdriver.Chrome(r"C:\Users\danie\chromedriver\chromedriver.exe")
driver.get("https://www.helmet.beam.vt.edu/bicycle-helmet-ratings.html#!")

# get all content from the website
content = driver.page_source
soup = BeautifulSoup(content, features='lxml')

helmets = soup.findAll(attrs={'class':'helmet-name'})       #find the names of the helmets
details = soup.findAll('div', attrs={'class':'gallery-header gallery-header-bottom'})   #contains price, score and rating

index = 0
df = pd.DataFrame(columns = ['helmet', 'price', 'score', 'rating'])

# loop through the helmet and details, combining the data together in a dataset
for helmet in helmets:
    detaillines = details[index].text.splitlines()
    data = pd.DataFrame({'helmet': [helmet.text],
            'price': [int(detaillines[1].split('$')[1])],
            'score': [float(detaillines[2].split(' ')[1])],
            'rating': [int(5-detaillines[3].count('star_border'))]})    
    df = pd.concat([df, data], ignore_index=True)
    index += 1

# scatterplot, showing price and score of all helmets
plt.scatter(df['price'], df['score'])
plt.title('Concussion risk vs helmet price')
plt.ylabel('Concussion Risk')
plt.xlabel('Price ($)')

# boxplot showing the price ranges of helmets, grouped by rating
ax = df.boxplot(column='price', by='rating')
ax.get_figure().suptitle('')
ax.set_title('Boxplot of helmet prices')
plt.ylabel('Price ($)')
plt.xlabel('Rating (out of 5)')
