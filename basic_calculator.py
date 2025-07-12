#calculator
num1 = float(input("num1\t="))
num2 = float(input("num2\t="))
operator = input("+\t-\t/\t*\t")
if operator=='+':
    print("sum=",(num1+num2))
if operator== '-':
    print("sub=",(num1-num2))
if operator=='/':
    print("div=",(num1/num2))
if  operator=='*':
    print("mul",(num1*num2))