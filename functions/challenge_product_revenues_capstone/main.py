
# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
# define calculate_revenue function returning revenue
def calculate_revenue(prices, quantities_sold): 
    revenue = [] # Create empty revenue list
    # loop through all prices and calculate total per item and append to revenue list
    for i in range(len(prices)):
        total = prices[i] * quantities_sold[i]
        revenue.append(total)
    return revenue
# set revenue variable as output of the calculate_revenue function
revenue = calculate_revenue(prices, quantities_sold)
# set revenue_per_product variable as a zipped list combining products and revenue lists
revenue_per_product = list(zip(products, revenue))
# define the formatted_output function to sort the revenue list
def formatted_output(revenues):
    revenues.sort()
# loop through each item
    for product_name, product_revenue in revenues:
        print(f"{product_name} has total revenue of ${product_revenue}")
    
# Example of expected output line (do not remove):
# print(f"{revenue[0]} has total revenue of ${revenue[1]}")

formatted_output(revenue_per_product)