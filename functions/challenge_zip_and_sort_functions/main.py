# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

# Zip the 3 lists into a list of tuples
combined_list = list(zip(products, prices, quantities_sold))

# Sort combined list by product Name and print list
sorted_products = sorted(combined_list)

# Loop through the sorted product list and print name, price, quantity
for item in sorted_products:
    
    # assign variables to each product's name, price, and quantity
    product_name = item[0]
    product_price = item[1]
    quantity_sold = item[2]
    
    # Print the product details for each product
    print(f"Product: {product_name}, Price: {product_price}, Quantity sold: {quantity_sold}")