print("Enter three numbers to begin the game.")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter the third number:"))

if(a + b + c > 1000):
   print("You win the game!")

elif(a + b + c == 1000):
   print("You make the game Foul!")

else:
  print("You lose the game!"