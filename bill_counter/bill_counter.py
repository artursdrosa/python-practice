def bill_counter(value):
    bills = [100, 50, 20, 10, 5, 2, 1] 
    for bill in bills: 
        quantity = value // bill
        if quantity > 0:
            if value != 1:
                print(f"{quantity} bills of $ {bill}")
                value = value % bill
            else:
                print(f"{quantity} coins of $ {bill}")
                value = value % bill