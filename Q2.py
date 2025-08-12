import requests 
from bs4 import BeautifulSoup
import csv


page = requests.get("https://baraasalout.github.io/test.html")                   # To Get Request From The Web Site 
soup = BeautifulSoup(page.content,"lxml")

li = []                                                                          # The List That Will Contain Dictionaries 
li_2  = []


table_t = soup.find_all('tr')

# To put th values in the Second List to use them as keys for the Dictionary 
th = table_t[0].find_all('th')      
for i in th:
    li_2.append(i.text)

# To put td values in the Dictionary then to the list
for num in range(1,len(table_t)):
    t = table_t[num].find_all('td')
    d = {}
    for i in range((len(t))):
        d[li_2[i]] = t[i].text
    li.append(d)

print(li)

# To save the Output in the CSV File
Header = ['Product', 'Price', 'In Stock']
with open('Q2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=Header)
    writer.writeheader()
    writer.writerows(li)