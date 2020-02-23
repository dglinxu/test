'''动态规划法找零'''
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    #从1分开始到change逐个计算最小硬币数
    for cents in range(1,change+1):
        #初始化一个最大值
        coinCount=cents
        newCoin=1
        # 减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
                newCoin=j
        # 得到当前最少硬币数，记录到表中
        minCoins[cents]=coinCount
        coinsUsed[cents]=newCoin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin=change
    while coin>0:
        thisCoin=coinsUsed[coin]
        print(thisCoin)
        coin=coin-thisCoin

amnt=63
clist=[1,5,10,25]
coinsUsed=[0]*(amnt+1)
coinCount=[0]*(amnt+1)
print('%d最小找零数是：%d'%(amnt,dpMakeChange(clist,amnt,coinCount,coinsUsed)))
print('找零分别是：')
printCoins(coinsUsed,amnt)
print(coinsUsed)


# '''改进迭代法找零'''
# def recMC(coinValuelist, change,knownResults):
#     minCoins = change
#     if change in coinValuelist:
#         knownResults[change]=1       #增设数组检查change是否已经尝试过，没有就给1
#         return 1
#     elif knownResults[change]>0:
#         return knownResults[change] #检查change是否已经尝试过，已检查返回最小coins
#     else:
#         for i in [c for c in coinValuelist if c <= change]:      #大于change的硬币不用检查
#             numCoins = 1 + recMC(coinValuelist, change - i,knownResults)
#             if numCoins < minCoins:
#                 minCoins = numCoins
#                 knownResults[change]=minCoins   #把数组的change格，赋值最小coins数量
#     return minCoins


# print(recMC([1, 5, 10, 25], 63,[0]*64))   #生成change+1个空列表
