# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# Subtract sales
for i in range(len(products)):
    products[i][1] -= units_sold[i][1]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

# Add new shipments
for i in range(len(products)):
    products[i][1] += shipment_received[i][1]
# Print updated stock levels
print("Final stock levels for all products:", products)