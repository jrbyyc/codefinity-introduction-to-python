# Define the function that takes list of product prices and copies it
def apply_discount(prices):
    prices_copy = prices.copy()
    # loop through each price in the list and if over $2 apply 10% discount
    for i in (range(len(prices_copy))): 
        if prices_copy [i] > 2.00:
            prices_copy[i] = prices_copy[i] * 0.9 # write the discounted value back into the list:
    # After the loop. prints the discounted price before returning 
    print(f"Updated product prices: {prices_copy}")
    return prices_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)