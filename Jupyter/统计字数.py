'''统计i have a dream 单词使用词频'''
def data_clean(line):
    for c in ["\\n",',','.',':','"','!',"'"]:
        line=line.replace(c,' ')
    return line
    
words=[]
with open('I:\python\Jupyter\i have a dream.txt','r') as fp:
    lines=fp.readlines()
for line in lines:
    word=[word.lower() for word in data_clean(line).split() if word]
    words.extend(word)
#     for word in data_clean(line).split():
#         if word:
#             word=word.lower()
#             words.append(word)
print(words)
