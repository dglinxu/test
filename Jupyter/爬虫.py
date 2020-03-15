import requests

# url="http://www.baidu.com"
# reponse=requests.get(url=url)
# reponse.encoding='uft-8'
# reponse.text #显示文本数据，前面要enconding
# repolse.content #提取二进制数据，用于MP3.4数据的提取

'''get方法'''
# url='http://httpbin.org/get'
# reponse=requests.get(url=url,params={'name':'dglinxu','salary':20000})
# print(reponse.text)
# todo dkife fjie dfjie
'''post方法'''
# url = 'http://httpbin.org/post'
# response = requests.post(url=url, data={'姓名': 'Tom', 'address': 'humen', 'age': 18})
# response.encoding = 'utf-8'
# print(response.text)

def func(S):
    # your code here
    return S


S = eval(input())
print(func(S))



