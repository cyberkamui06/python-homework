source_amount = float(input("Enter the amount: "))

exchange_rate = float(input("Enter the current exchange rate: "))

target_amount = source_amount / exchange_rate

print(f"Your money is equivalent to {target_amount:.2f}.")