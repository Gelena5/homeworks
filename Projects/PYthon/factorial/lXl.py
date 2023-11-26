def y(x):
   if x == 1:
       return x
   else:
       return x * y(x - 1)

num = int(input("number: "))

if num < 0:
   print("factorial doesn't exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", y(num))