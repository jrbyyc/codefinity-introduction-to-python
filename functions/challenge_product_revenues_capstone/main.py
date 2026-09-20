
# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold): 
    revenue = []
    
    for i in range(len(prices)):
        total = prices[i] * quantities_sold[i]
        revenue.append(total)
    
    return revenue

revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = list(zip(products, revenue))

def formatted_output(revenues):
    revenues.sort()

    for product_name, product_revenue in revenues:
        print(f"{product_name} has total revenue of ${product_revenue}")
    
# Example of expected output line (do not remove):
# print(f"{revenue[0]} has total revenue of ${revenue[1]}")

formatted_output(revenue_per_product)