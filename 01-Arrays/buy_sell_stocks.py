
# Earn Max profi on buying and selling of stocks

prices =[7,1,5,3,6,4]
max_profit=0
minimum_price= prices[0]

for price in range(len(prices)):
    if price < minimum_price:
        minimum_price=price

    profit= price - minimum_price

    if profit > max_profit:
        max_profit=profit

print("Maximum profit should be of:", max_profit)
