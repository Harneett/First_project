amount = input("Enter the amount for your total purchase")
value = amount+10
if int(amount) < 50:
    print("Your total purchase amount is" + value)
    print("Shipment Charges applied")
else:
    print("Free Shipping!")
    print("Your total purchase amount is " + "$" + amount)
print("Have a nice day!")