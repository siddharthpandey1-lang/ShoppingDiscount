print("Welcome ma'am/sir to the billing system!")
name = input("Please enter your name: ")
print(f"Hello, {name}! Let's get started with your billing.")
amount= float(input("Enter the total bill amount: "))
if amount >= 5000:
    discount = 50
elif amount >= 2000:
    discount = 30
elif amount >= 1000:
    discount = 10
else:
    discount = 0
final_amount = amount - (amount * discount / 100)
print(f"Your final bill amount after a discount of {discount}% is: {final_amount}")
print("Thank you for shopping with us!")