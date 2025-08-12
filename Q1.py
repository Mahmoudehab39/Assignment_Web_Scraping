import requests 
from bs4 import BeautifulSoup
import csv


page = requests.get("https://baraasalout.github.io/test.html")      # To Get Request From The Web Site            
soup = BeautifulSoup(page.content,"lxml")

li = []                                                             # The List That Will Contain Dictionaries 


# To put H1 values in the Dictionary then to the list
Heading_1 = soup.find('h1')
for i in Heading_1:
    li.append({'Type':'H1' ,'Content' :Heading_1.text})

# To put H2 values in the Dictionary then to the list    
Heading_2 = soup.find_all('h2')
for i in Heading_2:
    li.append({'Type':'H2', 'Content':i.text})

# To put li values in the Dictionary then to the list 
Lists = soup.find_all('li')
for i in Lists:
    for ii in i:
        li.append({'Type':'LI', 'Content': ii.text})

# To put P values in the Dictionary then to the list 
Parag = soup.find_all('p')
for i in Parag:
    for ii in i:
        li.append({'Type':'P', 'Content':ii.text})

print(li)

# To save the Output in the CSV File
Header = ['Type', 'Content']
with open('Q1.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=Header)
    writer.writeheader()
    writer.writerows(li)