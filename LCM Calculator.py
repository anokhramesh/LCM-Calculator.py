# A program to Find the LCM of Two Given Numbers


num1 = int(input("Enter First Number\n"))
num2 = int(input("Enter the Second Number\n"))

maxNum = max(num1,num2)
while True:
    if (maxNum%num1==0 and maxNum%num2==0):
        break
    maxNum =maxNum +1
print( f"The LCM of {num1} and {num2} is {maxNum}")
