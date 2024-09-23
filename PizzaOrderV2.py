# Pizza Order
# Version 2.0
# 9/22/2024
# Programming Fundamentals

print("Each pizza costs $7.99.")
print("If you order more than 5 pizzas, you will get a 10% discount.")

cost_per_pizza = 7.99
discount_percentage = 0.1

pizzas_ordered = int(input("How many pizzas do you want to order? >> "))

if pizzas_ordered <= 5:
    total_cost = pizzas_ordered * cost_per_pizza
else:
    total_cost = pizzas_ordered * cost_per_pizza * (1 - discount_percentage)

print("The total cost is $" + str(total_cost))
