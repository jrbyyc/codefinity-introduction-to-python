grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
# test price of eggs, reduce by $1 if over $5
if grocery_inventory["Eggs"][1] > 5:
    category, price, quantity = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (category, price - 1, quantity)
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable.")
# Add tomatoes and print list
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
# Test stock of milk, add 20 if under 10
milk_stock = grocery_inventory["Milk"][2] 
if milk_stock < 10:
    category, price, stock = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (category, price, stock + 20)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")
print(grocery_inventory)
# Remove apples if more than $2
if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
# Print updated inventory
print("Updated Inventory:", grocery_inventory)
    