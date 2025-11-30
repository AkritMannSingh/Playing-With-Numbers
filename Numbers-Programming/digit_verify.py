num = int(input("Enter a number:"))

if(9<num<=99):
  print("Two digit number.")

elif(99<number<=999):
  print("Three digit number.")

elif(999<number<=9999):
  print("Four digit number.")

else:
  print("The range of given number is greater than 4 digit.")