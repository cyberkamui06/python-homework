amount = float(input("Enter your total purchase amount: "))

if amount > 50000:
    discount = amount * 0.20
elif amount > 20000:
    discount = amount * 0.10
elif amount > 10000:
    discount = amount * 0.05
else:
    discount = 0

final_price = amount - discount

print("Final price:", final_price)