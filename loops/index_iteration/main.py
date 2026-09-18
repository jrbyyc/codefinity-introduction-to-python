# set up price list and discount list
prices = [29.99, 45.50, 12.75, 38.20] 
discounts = [0.10, 0.20, 0.15, 0.05]
# create range loop based on the index of prices, set original price and discount variables
for i in range(len(prices)):
    original_price = prices [i]
    discount = discounts[i]
# apply discount and update price(index)
    new_price = original_price * (1 - discount)
    prices[i] = new_price
# print new price to 2 decimal places
    print(f"Updated price for item {i}: ${new_price:.2f}")