import requests 
from bs4 import BeautifulSoup
import json


page = requests.get("https://baraasalout.github.io/test.html")                                                                          # To Get Request From The Web Site 
soup = BeautifulSoup(page.content,"lxml")

li = []                                                                                                                                 # The List That Will Contain Dictionaries 
li_2 = []

Header = ['title', 'price', 'stock']
book_2 = soup.find_all('div',style="text-align: center; width: 200px; border: 1px solid #ddd; padding: 10px; border-radius: 5px;")

# for books
for num in range(len(book_2)):
    z = book_2[num].find_all('p')
    zz = book_2[num].find_all('button')
    di ={}
    for i in range(len(z)):
        di[Header[i]]= z[i].text
    li.append(di)

    #for buttons
    for i in zz:
        li_2.append(i.text)

d = {'Books':li,"Buttons":li_2}
print(d)


# to save the output in json file
with open('Q3.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)