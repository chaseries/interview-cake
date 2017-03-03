#!/usr/local/bin/python3

def best_purchase(prices):
  if len(prices) < 2:
    raise Exception
  min_price = prices[0]
  max_profit = prices[1] - prices[0]
  for i, x in enumerate(prices):
    if i == 0: continue 
    current_price = prices[i]
    potential_profit = current_price - min_price
    max_profit = max(max_profit, potential_profit)
    min_price = min(min_price, current_price)
  return max_profit

if __name__ == '__main__':
  #print(best_purchase([10, 7, 5, 8, 11, 9]))
	print(max_profit([10, 7, 5, 8, 11, 9]))


