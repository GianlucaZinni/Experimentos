from selenium import webdriver
from selenium.webdriver.common.by import By
import re

years = [
    '1999', '2000', '2001'
    '2002', '2003', '2004', '2005'
    '2006', '2007', '2008', '2009', '2010', 
    '2011', '2012', '2013', '2014', '2015', '2016', 
    '2017', '2018', '2019', '2020', '2021', '2022', '2023'
    ]

onepiece = {}
path = 'C:\webdrivers\chromedriver.exe' #escribe tu ruta aqui
driver = webdriver.Chrome(path)

num = 0

for value in years:
    website = 'https://www.imdb.com/title/tt0388629/episodes?year=' + str(value)
    driver.get(website)

    imdb_info = driver.find_elements(By.CLASS_NAME, "info")
    imdb_rating = driver.find_elements(By.CLASS_NAME, "ipl-rating-star__rating")

    for info in imdb_info:
        imdb_episode = info.find_element(By.TAG_NAME, 'meta')
        imdb_rating = info.find_element(By.CLASS_NAME, "ipl-rating-star__rating")
        
        num += float(imdb_rating.get_attribute('innerHTML'))
        
        episode = imdb_episode.get_attribute('content')
        
        episode = episode.replace('.', "")
        if(episode == -1):
            continue
        onepiece[int(episode)] = imdb_rating.get_attribute('innerHTML')

# result = num / 1052

# print(result)

onepiece = dict(sorted(onepiece.items()))

        
file = open('onepiece_episode_ratings.txt', "w+")
for key, value in onepiece.items():
    file.write(str(key) + " ~ " + str(value) + "\n")

driver.quit()
