import requests 
from bs4 import BeautifulSoup
import json



page = requests.get("https://baraasalout.github.io/test.html")

soup = BeautifulSoup(page.content,"lxml")

li_tup_1 =[]
d ={}
label = soup.find_all('label')
for i in label:
    text =i.text.replace('\n','')
    li_tup_1.append(text.strip())
li_tup_1 = tuple(li_tup_1)


Default_Values = soup.find_all('option') 
li_tup_2 =[] 
for i in Default_Values:
    li_tup_2.append(i.text)
li_tup_2 = tuple(li_tup_2)



inp = soup.find_all('input')
li_tup_3 =[] 
for i in inp:
    li_tup_3.append(i.get('type'))
li_tup_3 = tuple(li_tup_3)
    
  
d = {'Label':li_tup_1,'Default_Values':li_tup_2,'input_type':li_tup_3}

# to view the result of the json 
res = json.dumps(d, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2)
print(res)

# to save the output in json file
with open('Q4_1.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)










# page = requests.get("https://baraasalout.github.io/test.html")

# soup = BeautifulSoup(page.content,"lxml")

# li =[]
# li_tup =[]
# label = soup.find_all('label')
# for i in label:
#     text =i.text.replace('\n','')
#     li_tup.append(text.strip())
# li_tup = tuple(li_tup)
# li.append({'Label':li_tup}) 

# Default_Values = soup.find_all('option') 
# li_tup =[] 
# for i in Default_Values:
#     li_tup.append(i.text)
# li_tup = tuple(li_tup)
# li.append({'Default_Values':li_tup}) 


# inp = soup.find_all('input')
# li_tup =[] 
# for i in inp:
#     li_tup.append(i.get('type'))
# li_tup = tuple(li_tup)
# li.append({'input_type':li_tup})  
    
# print(li)  

# res = json.dumps(li, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2)
# print(res)

# with open('Q4_2.json', 'w', encoding='utf-8') as f:
#     json.dump(li, f, ensure_ascii=False, indent=4)







