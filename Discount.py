"""
Name Aksa Vinod
Date 15-10-2024
Version 1.1
"""
purchase_amount=int(input("Enter your Purchase amount:"))
if purchase_amount>500:
    discount=purchase_amount*20/100
    final_amount=purchase_amount-discount
    print ("The final amount after discount:",final_amount)
elif purchase_amount>=200 and purchase_amount<=500:
    discount=purchase_amount*10/100
    final_amount=purchase_amount-discount
    print("The final amount after discount:",final_amount)
if purchase_amount<200:
    final_amount=purchase_amount
    print("The final amount",final_amount)


