from bill_counter import bill_counter

try: 
    value = int(input("Enter the amount: ")) 
except ValueError: 
    print("Error: Please enter a valid numeric value.") 

if value <= 0: 
    print("Error: The amount must be positive.")
elif value % 2 != 0: 
    print("Error: The amount must be a multiple of 2.")
else: 
    print("Bills delivered:")
    bill_counter(value)