# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
num1 = float(input("Enter the number1 : "))
num2 = float(input("Enter the number2 : "))
X = num1 * num2
S = num1 + num2
if X <= 1000:
    print(str(X))
else:
    print(str(S))
