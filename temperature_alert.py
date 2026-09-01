temperature = float(input("What is the current temperature in Celsius? "))

is_hot = temperature > 30
is_cold = temperature < 10

if is_hot:
    print("Warning: High temperature detected. Stay hydrated.")

if is_cold:
    print("Alert: Low temperature detected. Dress warmly.")