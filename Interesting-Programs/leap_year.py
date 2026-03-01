print("╔════════════════════════════════════════════════════════════╗")
print("║              LEAP YEAR CHECKER PROGRAM                    ║")
print("╚════════════════════════════════════════════════════════════╝\n")


year = 0
continue_program = 1


while continue_program == 1:
    
    
    while True:
        print("📅 Enter year details:")
        print("──────────────────────────────────")
        year_input = input("Enter the Year: ")
        
        is_valid = 1
        for char in year_input:
            if char < '0' or char > '9':
                is_valid = 0
                break
        
        if is_valid == 1:
            year = int(year_input)
            if year > 0:
                break
            else:
                print("❌ Please enter a positive year (after 1 AD)!\n")
        else:
            print("❌ Invalid input! Please enter only numbers.\n")
    
    print("\n════════════════════════════════════════════════════════════")
    print("ANALYSIS RESULTS:")
    print("════════════════════════════════════════════════════════════\n")
    
    print(f"📅 Year: {year}")
    print("──────────────────────────────────")
    
    
    if year <= 0:
        print("❌ RESULT: OUT OF DOMAIN")
        print("   Years must be positive numbers (1 AD onwards)")
        
    elif year % 400 == 0:
        print("✅ RESULT: LEAP YEAR")
        print("   Condition: Divisible by 400")
        print("   • February: 29 days")
        print("   • Total days: 366")
        print("   • Type: Century Leap Year")
        
    elif year % 100 == 0:
        print("❌ RESULT: NOT A LEAP YEAR")
        print("   Condition: Divisible by 100 but NOT by 400")
        print("   • February: 28 days")
        print("   • Total days: 365")
        print("   • Type: Century Year (Non-leap)")
        
    elif year % 4 == 0:
        print("✅ RESULT: LEAP YEAR")
        print("   Condition: Divisible by 4 (and not a century)")
        print("   • February: 29 days")
        print("   • Total days: 366")
        print("   • Type: Regular Leap Year")
        
    else:
        print("❌ RESULT: NOT A LEAP YEAR")
        print("   Condition: Not divisible by 4")
        print("   • February: 28 days")
        print("   • Total days: 365")
        print("   • Type: Regular Year")
    # END OF IF-ELSE LADDER
    
    print("\n════════════════════════════════════════════════════════════")
    print("YEAR INFORMATION:")
    print("════════════════════════════════════════════════════════════")
    if year > 0:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("📌 This is a century leap year (rare!)")
                else:
                    print("📌 This is a century year (non-leap)")
            else:
                print("📌 This is a regular leap year")
        else:
            if year % 100 == 0:
                print("📌 This is a century year (non-leap)")
            else:
                print("📌 This is a regular year")
        
        
        print("\n📊 HISTORICAL CONTEXT:")
        print("──────────────────────────────────")
        
        
        if year > 0:
            print(f"• Recent leap years before {year}:")
            count = 0
            check_year = year - 1
            while count < 3 and check_year > 0:
                if (check_year % 400 == 0) or (check_year % 4 == 0 and check_year % 100 != 0):
                    print(f"  - {check_year}")
                    count = count + 1
                check_year = check_year - 1
            
            if count == 0:
                print("  (No recent leap years found)")
            
            print(f"\n• Upcoming leap years after {year}:")
            count = 0
            check_year = year + 1
            while count < 3:
                if (check_year % 400 == 0) or (check_year % 4 == 0 and check_year % 100 != 0):
                    print(f"  - {check_year}")
                    count = count + 1
                check_year = check_year + 1
    
    print("\n════════════════════════════════════════════════════════════")
    
    
    while True:
choice = input("\nDo you want to check another year? (yes/no): ")
        
        
        choice_lower = ""
        for char in choice:
            if 'A' <= char <= 'Z':
                choice_lower = choice_lower + chr(ord(char) + 32)
            else:
                choice_lower = choice_lower + char
        
        if choice_lower == "yes" or choice_lower == "y":
            continue_program = 1
            print("\n" + "="*60 + "\n")
            break
        elif choice_lower == "no" or choice_lower == "n":
            continue_program = 0
            break
        else:
            print("❌ Please enter 'yes' or 'no' only.")


print("\n" + "╔════════════════════════════════════════════════════════════╗")
print("║         THANK YOU FOR USING THE LEAP YEAR CHECKER!        ║")
print("║                    Have a great day! 📅                   ║")
print("╚════════════════════════════════════════════════════════════╝")