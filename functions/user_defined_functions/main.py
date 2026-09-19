#  define function with parameters price and quantity, and return price * quantity
def calculate_total_cost(price, quantity):
    total = price * quantity
    return total

# Call the function and print the result
apples_total_cost = calculate_total_cost(1.50, 10)

# Print the total cost 
print(f"The total cost for apples is ${apples_total_cost}")