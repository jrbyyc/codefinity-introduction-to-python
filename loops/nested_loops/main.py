produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
# combine lists into a single list
groceries = [produce, dairy]
#  iterate through both loops to print full grocery list
for section in groceries:
    for item in section:
        print(f"Item Name: {item}")