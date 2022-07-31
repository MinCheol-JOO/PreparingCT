prices = [2,1,2,1,0,1,2]
# Output =5
left = 0
right = 1 
max_profit = 0
while(right<len(prices)):
    current_profit = prices[right]-prices[left]
    if prices[left] < prices[right]:
        max_profit = max(max_profit, current_profit)
    else:
        left=right
    right+=1

        


            
# print(sell_prices-buy_prices)
return max_profit
            

            



    