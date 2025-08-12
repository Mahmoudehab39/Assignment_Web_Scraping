import requests 
from bs4 import BeautifulSoup
import json


page = requests.get("https://baraasalout.github.io/test.html")
soup = BeautifulSoup(page.content,"lxml")

features = soup.find_all('div',class_='product-card')
li = []
count =1
for i in features:

    li.append({f'Product_{count}':{'ID': i.get('data-id') , 'Product_Name':(i.find("p",class_='name')).text,'Price' : (i.find("p",class_='price')).text, 'Available colors' :(i.find("p",class_='colors')).text[18:]}})
    count += 1
print(li)


# to view the result of the json 
res = json.dumps(li, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2)
print(res)

# to save the output in json file
with open('Q6_1.json', 'w', encoding='utf-8') as f:
    json.dump(li, f, ensure_ascii=False, indent=4)




# # another solution

# page = requests.get("https://baraasalout.github.io/test.html")
# soup = BeautifulSoup(page.content,"lxml")

# features = soup.find_all('div',class_='product-card')
# li = []

# for i in features:

#     li.append({'ID': i.get('data-id') , 'Product_Name':(i.find("p",class_='name')).text,'Price' : (i.find("p",class_='price')).text, 'Available colors' :(i.find("p",class_='colors')).text[18:]})

# print(li)

# res = json.dumps(li, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2)
# print(res)

# with open('Q6_2.json', 'w', encoding='utf-8') as f:
#     json.dump(li, f, ensure_ascii=False, indent=4)