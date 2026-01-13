def maxProfit(prices):
    MP = 0
    bestBuy = prices[0]
    for i in range(1,len(prices)):
        if prices[i] > bestBuy:
            MP = max(MP,prices[i]-bestBuy)
        bestBuy = min(bestBuy, prices[i])
    return MP

prices = [7,1,5,3,6,4]

print(maxProfit(prices))