#Function to add two number
def sum(a,b):
    return a+b

#Function to subtract two number
def sub(a,b):
    return a-b

#Function to multiply two number
def mul(a,b):
    return a*b

#Function to divide two number
def div(a,b):
    return a/b

#Function to avg two number
def avg(a,b):
    return (a+b)/2

#user input
print("Please select an option : \n"\
      "1.Addition\n"\
      "2.Subtraction\n"\
      "3.Multiplication\n"\
      "4.Division\n"\
      "5.Average\n")
select = int(input(("Select an operation from 1,2,3,4,5 : ")))

if select in [1,2,3,4,5]:
    num1 = int(input("Please Enter the value of first number : "))
    num2 = int(input("Please Enter the value of second number : "))

    #print the result

    if select == 1:
        print("The value of sum is : ", sum(num1,num2))
    elif select == 2:
        print("The value of subtraction is : ", sub(num1,num2))
    elif select == 3:
        print("The value of multiplication is : ", mul(num1,num2))
    elif select == 4:
        print("The value of division is : ", div(num1,num2))
    elif select == 5:
        print("The value of average is : ", avg(num1,num2))
else:
    print("Invalid Option! Please select the correct option!")

