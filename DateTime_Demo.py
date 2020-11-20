import datetime
deadline = input("Enter deadline for your project...(mm/dd/yyyy)")
currentDate = datetime.date.today()
dueDays = datetime.datetime.strptime(deadline,'%m/%d/%Y').date()
difference = dueDays - currentDate
print("You have " + str(difference.days) + " days left to complete your project.")
