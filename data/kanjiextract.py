import requests
from bs4 import BeautifulSoup
import json

f=open("kanji.html")
soup = BeautifulSoup(f.read(), 'html.parser')
a=soup.find_all('a')
all_data=[]

def json_dump(x):
    global all_data
    str_json=json.dumps(all_data,ensure_ascii=False)
    filename="kanji{}.json".format(x)
    f1=open("kanji{}.json".format(x),"w")
    f1.write(str_json)
    f1.close()
    all_data=[]
    print("dumped-{}".format(filename))

for x in range(0,len(a)):
    href=a[x].get("href")
    kanji=a[x].get_text()
    try:
        r = requests.get('https://kanjicards.org'+href)
    except:
        print("Failed at {}: {}".format(x,href))
    if(r.status_code != requests.codes.ok):
        print("Failed at {}: {}".format(x,href))
    # import pdb;pdb.set_trace()
    soup1 = BeautifulSoup(r.text, 'html.parser')
    table=soup1.find('table')
    rows = table.find_all('tr')
    words=[]
    meta={"kun":"","on":"","meaning":""}
    for y in range(1,len(rows)):
        cols=rows[y].find_all("td")
        word_atomic=[]
        for z in range(0,len(cols)):
            word_atomic.append(cols[z].get_text())
        words.append(word_atomic)
    li=soup1.find_all("li")
    for az in range(4,7):
        temp=li[az].get_text().split(":")
        meta[temp[0]]=temp[1]
    data={"kanji":kanji,"words":words,"meta":meta,"url":href}
    # print("{}: {}".format(x,href))
    all_data.append(data)
    if(x%500==0):
        json_dump(int(x/500)+1)
# str_json=json.dumps(all_data)
# f1=open("kanji.json","w")
# f1.write(str_json)
# f1.close()