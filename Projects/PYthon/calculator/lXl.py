def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("1.მიმატება")
print("2.გამოკლება")
print("3.გამრავლება")
print("4.გაყოფა")
choice = input("ჩაწერე არჩევანი (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
        num1 = float(input("ჩაწერე პირველი რიცხვი: "))
        num2 = float(input("ცაწერე მეორე რიცხვი: ")) 

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))