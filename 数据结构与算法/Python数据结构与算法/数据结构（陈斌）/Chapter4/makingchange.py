def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(1,change+1):   #这里要从1开始，书上从0开始
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents]=coinsUsed[cents-newCoin]+[newCoin]  #求最少找零时的币值分布，注意输入列表格式
      # coinsUsed[cents] = newCoin             #求出change最大硬币值，输入列表与上面不同
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,25]
    coinsUsed = [[] for i in range(amnt+1)]
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    # print("They are:")
    # printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed[-1])

main()
