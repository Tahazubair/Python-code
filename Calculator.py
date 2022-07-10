num1 = float(input("Enter first number : "))
Op = input("Enter the Operator : ")
num2 = float(input("Enter first number : "))

if Op == "+":
    print(num1 + num2)
elif Op == "-":
    print(num1 - num2)
elif Op == "/":
    print(num1 / num2)
elif Op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")