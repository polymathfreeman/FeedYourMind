# for performing your HTTP requests
import requests  

# for xml & html scrapping 
from bs4 import BeautifulSoup 

# for table analysis
import pandas as pd

# write to csv
import csv

# Time
import time

#Visuals
import matplotlib.pyplot as plt

# url of wikipedia page from which you want to scrap tabular data.
url1 = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
input(f"Check this website: {url1}\n")
# Session helps to object allows you to persist certain parameters across requests
# By default, Request will keep waiting for a response indefinitely. Therefore, it is advised to set the timeout parameter.
# If the request was successful, you should see the reponse output as '200'.
s = requests.Session()
response = s.get(url1, timeout=10)
#response2 = s.get(url2, timeout=5)
print(response)

# parse response content to html
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)

# to view the content in html format
pretty_soup = soup.prettify()
#print(pretty_soup)

# title of Wikipedia page
soup.title.string
print(soup.title.string)

# find all the tables in the html
all_tables=soup.find_all('table')

# get right table to scrap
right_table=soup.find('table', {"class":'wikitable sortable'})

# Number of columns in the table
for row in right_table.findAll("tr"):
    cells = row.findAll('td')

len(cells)

# number of rows in the table including header
rows = right_table.findAll("tr")
len(rows)

# header attributes of the table
header = [th.text.rstrip() for th in rows[0].find_all('th')][1:]
print(header)
print('------------')
print(len(header))

lst_data = []
for row in rows[2:]:
    data = [d.text.rstrip() for d in row.find_all('td')]
    lst_data.append(data)


# select also works as find_all
lst_data1 = []
for row in rows[2:]:
    data = [d.text.rstrip() for d in row.select('td')]
    lst_data1.append(data)

# length of each record
len(lst_data1[0])

lst_data1 = pd.DataFrame(lst_data1, columns=header)
df = lst_data1.copy()
print(df.head(3))