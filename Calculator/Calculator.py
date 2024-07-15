print("========================== Calculator Pro ==========================")
print("============================================= By: Karan Sethi ======")

def Add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The sum is: ", num1 + num2)
    Main_menu()

def Sub():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The difference is: ", num1 - num2)
    Main_menu()

def Mul():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The product is: ", num1 * num2)
    Main_menu()

def Div():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The quotient is: ", num1 / num2)
    Main_menu()

def Main_menu():
    print("============================ Main Menu =============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = (input("Enter your choice: "))
    if choice.isdigit():
        choice = int(choice)
    
    if choice == 1:
        Add()
    
    elif choice == 2:
        Sub()
    
    elif choice == 3:
        Mul()
    
    elif choice == 4:
        Div()
    
    elif choice == 5:
        exit()
        
    else:
        print("Invalid choice! Please try again.")
        Main_menu() 
        
Main_menu()