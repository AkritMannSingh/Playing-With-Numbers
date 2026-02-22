print("╔════════════════════════════════════════════════════════════╗")
print("║                 DAYS LEFT IN MONTH FINDER                 ║")
print("║              (Using If-Else Ladder)                       ║")
print("╚════════════════════════════════════════════════════════════╝\n")

# Get month input
month = input("Enter the current month: ").strip()
print()

# Get date input
date = int(input("Enter today's date: "))
print()

print("════════════════════════════════════════════════════════════")
print("CALCULATION RESULTS:")
print("════════════════════════════════════════════════════════════\n")

# IF-ELSE LADDER STARTS HERE
if month == "January" or month == "january" or month == "JANUARY":
    if 1 <= date <= 31:
        print(f"📅 Month: January")
        print(f"📆 Today's Date: {date}")
        print(f"✅ Days left in January: {31 - date}")
        if date == 31:
            print("   (Last day of the month!)")
    else:
        print("❌ Invalid date for January! (Valid: 1-31)")

elif month == "February" or month == "february" or month == "FEBRUARY":
    if 1 <= date <= 29:
        print(f"📅 Month: February")
        print(f"📆 Today's Date: {date}")
        
        # Check for leap year (using if-else inside)
        if date <= 28:
            print(f"✅ Days left in February: {28 - date}")
        else:
            print("⚠️  Note: February 29 only exists in leap years!")
            print(f"✅ Days left in February: {29 - date}")
        
        if date == 28:
            print("   (Last day of February in non-leap years)")
        elif date == 29:
            print("   (Last day of February in leap years)")
    else:
        print("❌ Invalid date for February! (Valid: 1-28 or 1-29 in leap years)")

elif month == "March" or month == "march" or month == "MARCH":
    if 1 <= date <= 31:
        print(f"📅 Month: March")
        print(f"📆 Today's Date: {date}")
        print(f"✅ Days left in March: {31 - date}")
        if date == 31:
            print("   (Last day of the month!)")
    else:
        print("❌ Invalid date for March! (Valid: 1-31)")

elif month == "April" or month == "april" or month == "APRIL":
    if 1 <= date <= 30:
        print(f"📅 Month: April")
        print(f"📆 Today's Date: {date}")
        print(f"✅ Days left in April: {30 - date}")
        if date == 30:
            print("   (Last day of the month!)")
    else:
        print("❌ Invalid date for April! (Valid: 1-30)")

elif month == "May" or month == "may" or month == "MAY":
    if 1 <= date <= 31:
        print(f"📅 Month: May")
        print(f"📆 Today's Date: {date}")
        print(f"✅ Days left in May: {31 - date}")
        if date == 31:
            print("   (Last day of the month!)")
    else:
        print("❌ Invalid date for May! (Valid: 1-31)")

elif month == "June" or month == "june" or month == "JUNE":
    if 1 <= date <= 30:
        print(f"📅 Month: June")
        print(f"📆 Today's Date: {date}")
        print(f"✅ Days left in June: {30 - date}")
        if date == 30:
            print("   (Last day of the month!)")
    else:
        print("❌ Invalid date for June! (Valid: 1-30)")

elif month == "July" or month == "july" or month == "JULY":
    if 1 <= date <= 31:
        print(f"📅 Month: July")
        print(f"📆 Today's Date: {date}")
        print(f"✅ Days left in July: {31 - date}")
        if date == 31:
            print("   (Last day of the month!)")
    else:
        print("❌ Invalid date for July! (Valid: 1-31)")

elif month == "August" or month == "august" or month == "AUGUST":
    if 1 <= date <= 31:
        print(f"📅 Month: August")
        print(f"📆 Today's Date: {date}")
        print(f"✅ Days left in August: {31 - date}")
        if date == 31:
            print("   (Last day of the month!)")
    else:
        print("❌ Invalid date for August! (Valid: 1-31)")

elif month == "September" or month == "september" or month == "SEPTEMBER":
    if 1 <= date <= 30:
        print(f"📅 Month: September")
        print(f"📆 Today's Date: {date}")
        print(f"✅ Days left in September: {30 - date}")
        if date == 30:
            print("   (Last day of the month!)")
    else:
        print("❌ Invalid date for September! (Valid: 1-30)")

elif month == "October" or month == "october" or month == "OCTOBER":
    if 1 <= date <= 31:
        print(f"📅 Month: October")
        print(f"📆 Today's Date: {date}")
        print(f"✅ Days left in October: {31 - date}")
        if date == 31:
            print("   (Last day of the month!)")
    else:
        print("❌ Invalid date for October! (Valid: 1-31)")

elif month == "November" or month == "november" or month == "NOVEMBER":
    if 1 <= date <= 30:
        print(f"📅 Month: November")
        print(f"📆 Today's Date: {date}")
        print(f"✅ Days left in November: {30 - date}")
        if date == 30:
            print("   (Last day of the month!)")
    else:
        print("❌ Invalid date for November! (Valid: 1-30)")

elif month == "December" or month == "december" or month == "DECEMBER":
    if 1 <= date <= 31:
        print(f"📅 Month: December")
        print(f"📆 Today's Date: {date}")
        print(f"✅ Days left in December: {31 - date}")
        if date == 31:
            print("   (Last day of the month!)")
    else:
        print("❌ Invalid date for December! (Valid: 1-31)")

else:
    print("❌ ERROR: Invalid month name!")
    print("   Please enter a valid month (e.g., January, February, etc.)")
# END OF IF-ELSE LADDER

print("\n════════════════════════════════════════════════════════════")
print("📝 NOTE: February is shown with 28 days by default")
print("        For leap years, February 29 is valid")
print("════════════════════════════════════════════════════════════")
print("\nThank you for using the Days Finder! 📅")