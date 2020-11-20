value1 = int(150)
detail1 = input("Enter your Country")
provinceCanada = ["Alberta","British Columbia","Maitoba","New Brunswick","Nova Scotia","Nunavut","Ontario","Yukon"]
if detail1 == "Canada":
    detail2 = input("Enter your province")
    if detail2 == "Alberta":
        print("Your total charge for the order is " + str(value1) + " + 0.5% General Sales Tax(GST), with a total of " +str(value1*0.005))
    elif detail2 == "Ontario" or detail2 == "New Brunswick" or detail2 == "Nova Scotia":
        print("Your total charge for the order is " + str(value1) + " + 0.13% Harmonised Sales Tax, with a total of " + str(value1)+str(value1*0.0013))
    else:
        print("Your total charge for the order is " + str(value1) + " + 0.6% Provincial Sales Tax" + "+0.5% General Sales Tax(GST), with a total of " + str(value1)+str(value1*0.006)+str(value1*0.005))
else:
    print("No additional Tax")
    print("Your total charge for the order is " + str(value1))

print("Thank You for shopping. Hope you have a nice day!")

