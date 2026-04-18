from calculate_tips import calculate_tips

try:
    order_amount = float(input("Enter the order amount: "))
    tip_per = float(input("Enter the tip percentage: "))
except ValueError:
    print("Please enter a valid numeric value.")
    exit(1)

tip_amount, total_amount = calculate_tips(order_amount, tip_per)
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount to pay: ${total_amount:.2f}")