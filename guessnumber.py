import random

def get_random_number():
     
     secret_number = random.randint(1,25)
     return secret_number


def print_greeting():
     print("welcome to the number_guessing_game")
     print("enter the number between 1 to 25")



def number_guessing_name():
     max_attempts = 5
     secret_number = get_random_number()
     attempts = 0
     print_greeting()
    
   

   


     while True:
          guess = int(input("enter the number : "))
          
          attempts = attempts + 1

          if   guess < secret_number:
               print("too low - try another no")
          elif guess > secret_number:
               print("too high - try another no")    
          else:
               print("congratulations  ! ! ! you have found " + str(attempts) + " attempts")  
               break
          if attempts == max_attempts:
               print("sorry ! you have reached max attempts")
          

number_guessing_name()          


 