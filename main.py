from math_operation import add,subtract,multiply,divide


print("\n\n===== Basic Calculator =====\n\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n0. Exit\n")

def get_integer(message):
    while True:
        try:
            number=int(input(message))
            return number
        except ValueError:
            print("Invalid Input")

while True:
    try:
        number=int(input("Choose: "))
        if number==0:
            break
        elif 1<=number<=4:
            number1=get_integer("number1: ")
            number2=get_integer("number2: ")
            if number==1:
                result=add(number1,number2)
                print(result)
            elif number==2:
                result=subtract(number1,number2)
                print(result)
            elif number==3:
                result=multiply(number1,number2)
                print(result)
            elif number==4:
                result=divide(number1,number2)
                print(result)
        else:
            print("Invalid choice")
                
    except ValueError:
        print("Just number")
