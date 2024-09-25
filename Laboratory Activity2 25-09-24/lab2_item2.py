def cal_discount(total_amount):
    if total_amount > 5000:
        discount_rate = 0.10 
    else:
        discount_rate = 0.05 
        
    discount_amount = total_amount * discount_rate
    final_amount = total_amount - discount_amount
    return final_amount, discount_amount

while True:
   
    totalpurchase_input = input("Enter the total purchase amount: ")

    if totalpurchase_input.replace('.', '', 1).isdigit() and float(totalpurchase_input) >= 0:
        total_purchase = float(totalpurchase_input)
        
        final_amount, discount_amount = cal_discount(total_purchase)
        
        print(f"Initial Purchase Amount: {total_purchase:.2f}")
        print(f"Discount: {discount_amount:.2f}")
        print(f"Final Price: {final_amount:.2f}")
        
    else:
        print("Please enter a valid positive number.")

    try_again = input("Do you want to try again? (yes/no): ").strip().lower()
    if try_again != 'yes':
        break

print("Thank you!")
