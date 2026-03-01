print("🎯 Welcome to Multiple Finder! 🎯\n")

num = int(input("Enter a number: "))


print(f"\nFirst 10 multiples of {num} are:")
print("-" * 25)


print(f"{num} ×  1 = {num * 1}")
print(f"{num} ×  2 = {num * 2}")
print(f"{num} ×  3 = {num * 3}")
print(f"{num} ×  4 = {num * 4}")
print(f"{num} ×  5 = {num * 5}")
print(f"{num} ×  6 = {num * 6}")
print(f"{num} ×  7 = {num * 7}")
print(f"{num} ×  8 = {num * 8}")
print(f"{num} ×  9 = {num * 9}")
print(f"{num} × 10 = {num * 10}")

print("-" * 25)


feedback = input("\nHow was your experience with Multiple Finder? (good/okay/bad): ")

if feedback.lower() == "good":
    print("Thanks! Glad you liked it! 😊")
elif feedback.lower() == "okay":
    print("Thanks! We'll try to make it better! 🙂")
elif feedback.lower() == "bad":
    print("Sorry to hear that! We'll improve! 🛠️")
else:
    print("Thanks for your feedback! 📝")