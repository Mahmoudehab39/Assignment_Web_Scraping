import requests 
from bs4 import BeautifulSoup
import json

page = requests.get("https://baraasalout.github.io/test.html")

soup = BeautifulSoup(page.content,"lxml")


v = soup.find('iframe')
li = [{'Youtube_link': v.get('src')}]

print(li)

# to view the result of the json 
res = json.dumps(li, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2)
print(res)

# to save the output in json file
with open('Q5.json', 'w', encoding='utf-8') as f:
    json.dump(li, f, ensure_ascii=False, indent=4)