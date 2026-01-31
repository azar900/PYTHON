

# get user intention
print("""
      1.addition \n
      2.subtraction \n
      3.muliplication \n
      4.division \n
      5.press 5 to exit

""")

calucaltor_condition = True

while calucaltor_condition:
    print("\n")
    print("welcome to calculator !")

    user_operation = int(input("enter your option : "))



    if user_operation == 1:
    
        # addition
        print("addition")
        number_1 = int(input("enter the number 1"))
        number_2 = int(input("enter the number 2"))
        result = number_1 + number_2

        print("the result is", result) 



    elif user_operation == 2:
    
        # subtraction
        print("subtraction")
        number_1 = int(input("enter the number 1"))
        number_2 = int(input("enter the number 2"))
        result = number_1 - number_2

        print("the result is", result) 




    elif user_operation == 3:
    
        # multify
        print("multiplication")
        number_1 = int(input("enter the number 1"))
        number_2 = int(input("enter the number 2"))
        result = number_1 * number_2

        print("the result is", result) 




 
    elif user_operation == 4:

        # divi
        print("division")
        number_1 = int(input("enter the number 1"))
        number_2 = int(input("enter the number 2"))
        result = number_1 / number_2
        print("the result is", result) 

    elif user_operation == 5:
        print("thanks for using calculator, see you again. ")
        calucaltor_condition = False




