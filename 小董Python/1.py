<<<<<<< HEAD
print(int('11111',2))
=======
# from random import randint
# a=["flower","flow","flight"]
# print(min(len(i) for i in a))
# li=[randint(1,10) for i in range(25)]
# s=set(li)
# for i in s:
#     print('%d鏁板瓧鐨勬�℃暟鏄�锛�%d'%(i,li.count(i)),end='\n')
import time
li = ["\\", "|", "/", "鈥�"]  #绗�涓€涓�涓や釜鏂滄潬鏄�涓轰簡杞�涔�
s="鏋濅笂鏌崇坏鍚瑰張灏戯紝澶╂动浣曞�勬棤鑺宠崏"
l=len(s)
for i in range(10+1):
    # \r 琛ㄧず灏嗗厜鏍囩殑浣嶇疆鍥為€€鍒版湰琛岀殑寮€澶翠綅缃�
    # \b琛ㄧず灏嗗厜鏍囩殑浣嶇疆鍥為€€涓€浣�
    # print('\r%d'%i,end='') #鍏夋爣鍦ㄥ瓧绗﹀悗闈�
    # print(i,end='\r') #鍏夋爣鍦ㄥ瓧绗﹀墠闈�pip
    # print('\r'+'*'*i,end=' ')
    # j = i % 4
    # print('\r'+li[j], end='')
    
    print('\r'+'绂荤▼搴忛€€鍑鸿繕鏈�%d绉掞紒'%(10-i),end=' ')  #杩涘害鏉�
    time.sleep(1)
>>>>>>> e4408744db7d96541bc78192259229d59acf8bbb
