import requests
from bs4 import BeautifulSoup

url='https://www.lmonkey.com/t'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

response=requests.get(url,headers=headers)

if response.status_code==200:
    print('连接成功！')
    soup=BeautifulSoup(response.text,'lxml')
    #获取所有文章
    # divs=soup.find_all('div',class ='list-group-item list-group-item-action p-06')
    divs=soup.find_all('div',class_='list-group-item list-group-item-action p-06')
    varlist=[]
    for i in divs:
        try:
            r=i.find('div',class_='topic_title mb-0 lh-180').text
            vardict={'title':r.split()[0],
                     'url':i.a['href'],
                     'author':i.strong.a.text,
                     'date':i.span['title']}
            varlist.append(vardict)
        except:
            pass

print(varlist)

