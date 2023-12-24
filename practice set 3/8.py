withdraw_amt = int(input("enter withdrawal amount: "))
avl_amt = 200

if (withdraw_amt+100) > avl_amt:
    print("Transaction is failed.")
elif ((withdraw_amt+100) <= avl_amt) and (withdraw_amt % 5) == 0:
    print("Transaction is successfull")
    avl_amt = avl_amt - (withdraw_amt+100)
else:
    print("balance is low")

print(f"amt left is {avl_amt}")