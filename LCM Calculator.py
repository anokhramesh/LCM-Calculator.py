# A program to Find the LCM of Two Given Numbers
#LCM Stands for-Least Common Multiple .
'''Find the LCM of a set of numbers with this calculator.
Input the two numbers you want to find the LCM . 
For example, Enter first num=2500 ,second num=1000'''

num1 = int(input("Enter First Number\n"))# user in put num1
num2 = int(input("Enter the Second Number\n"))# user in put num2
maxNum = max(num1,num2)#maximum value of num1 and num2 will  assign to variable name maxNum
while True:
        if (maxNum % num1==0 and maxNum % num2==0):#if remainder of maxNum divided by num1 & maxNum divided by num2 is eual to 0
            break# break the while loop
        maxNum = maxNum +1# add 1 to the vlaue of maxNum
print( f"The LCM of {num1} and {num2} is {maxNum}")#display the value of variable lcm as an answer.
