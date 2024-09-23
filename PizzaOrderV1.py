# Pizza Order
# Version 1.0
# 9/22/2024
# Programming Fundamentals

print("Each pizza costs $7.99.")
print("If you order more than 5 pizzas, you will get a 10% discount.")

# set up variables to make the code easier to read
cost_per_pizza = 7.99
discount_percentage = 0.1

# get the number of pizzas and calculate the total cost
pizzas_ordered = int(input("How many pizzas do you want to order? >> "))
total_cost = pizzas_ordered * cost_per_pizza

# calculate and apply the discount if applicable
if pizzas_ordered > 5:
    discount = total_cost * discount_percentage
    total_cost = total_cost - discount

print("The total cost is $" + str(total_cost))