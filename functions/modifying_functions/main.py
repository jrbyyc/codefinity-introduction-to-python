#  define function to apply discount
def apply_discount(price, discount=0.05):
    discounted_price = price * (1 - discount)
    return discounted_price

# define function to return price after adding tax. 
def apply_tax(discounted_price, tax=0.07):
    taxed_price = discounted_price * (1 + tax)
    return taxed_price

# define function to calculate final total
def calculate_total(price, discount=0.05, tax=0.07):
    discounted_price = apply_discount(price, discount)
    total_price = apply_tax(discounted_price, tax)
    return total_price

# Call the function without providing a `discount`, using the default value
total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")

# Call the function with a custom `discount` value
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")