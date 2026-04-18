def calculate_tips(order_amount, tip_percentage):
    tip_amount = order_amount * (tip_percentage / 100)
    total_amount = order_amount + tip_amount
    return tip_amount, total_amount

