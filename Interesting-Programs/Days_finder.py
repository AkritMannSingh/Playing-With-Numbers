print("Welcome to Days' Finder\n")
print("In this game, we find how many days are left in the current month\n")

date = int(input("Enter the today's date:"))
month = str(input("Enter the current Month:"))

if month in ["April", "June", "September", "November"]:
    print("Days left in this month are:", 30 - date)

elif month == "February":
    print("Days left in this month are:", 28 - date)

else:
    print("Days left in this month are:", 31 - date