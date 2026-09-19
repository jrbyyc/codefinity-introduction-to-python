# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
# Unpack inventory into variables
for item in inventory: 
    current_stock, regular_price, discounted_price = inventory[item]
 # Test if understock, print restock message and regular price message   
    if current_stock < 30:
        print(f"{item} need restocking.")
        print(f"{item} should be sold at the regular price of {regular_price}.")
 # Test if overstock, print discount price message       
    elif current_stock > 100:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")
  # Otherwise, just print regular price      
    else:
        print(f"{item} should be sold at the regular price of {regular_price}.")