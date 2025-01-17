print("Hello and Welcome to the Elite 101 Chatbot.\n")
name = input("What is your name? \n")
age = input("Hello "+ name +", how old are you? \n")

print("Welcome "+name+"! WOW, you're "+age+", that's awesome. How can I help you today?\n")

print("Please choose the following options: \n")
print("1. Chill Comment")
print("2. Mystery Choice")
print("3. Read Something Nice")
print("4. Exit\n")

def user_selection():
    
    user_choice = int(input("Enter a number between 1-4: "))
    if user_choice == 1: 
        print('Hope you have a good day')
    elif user_choice == 2:
        print('Nice Choice, you picked 2')   
    elif user_choice == 3: 
        print('Cannot wait to see what how bright your future will be.')
    elif user_choice == 4:  #Exit the program
        print("Thank you "+name+" for using the Chat Bot! Have a great day!"
              )  # adds thank you message before exiting the program
    
      
user_selection()
