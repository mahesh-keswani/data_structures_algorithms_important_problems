'''
    One transaction is defined as one buy and one sell. 
'''
def maxProfitKTransactions(prices, k):
    # intializing with 0 profits for all transactions from k=0...K
    profits = [ [0 for day in prices] for ntransction in range(0, k + 1)]
    '''
     Formula: profits[nTransaction][day] = max( profits[nTransaction][day - 1],
                                     prices[day] + max(-prices[x] + profits[nTransaction - 1][x]) for all x from 0...day
                                    )
     
    The first term means we do not sell the share, therefore the profit we had on previous day is same as profit on today.
    The second term is when we sell the share, we will get profit= price_on_current_ day +
    max_profit_on_previous_day_with_one_transaction_less.
    
    '''
    for transaction in range(1, k + 1):
        # This is for maintaining the maxProfit on previous day.
        maxThusFar = float("-inf")
        for day in range(1, len(prices)):
            # same as above formula
            maxThusFar = max( maxThusFar, -prices[day - 1]+ profits[transaction - 1][day - 1] )

            # Now updating the profit for current transaction on the current day.
            profits[transaction][day] = max( profits[transaction][day - 1], prices[day] + maxThusFar )
  	
	return profits[-1][-1]
