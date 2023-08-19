import random
import os

cust_data = {}
NEW_USER_ATTRIBUTES = ['name', 'address', 'phone num', 'govt id', 'amount']

# The 'new_user()' function to add a new user to the 'cust_data' dictionary.
def new_user():
    # Step 1: Create a random five-digit account number and store it in 'acc_num' variable
    accno = random.randint(10000,99999)
    while accno in cust_data:
        accno = random.randint(10000,99999)

    # Step 2: Create an empty list and store it in the 'new_user_inputs' variable.

    temp = NEW_USER_ATTRIBUTES.copy()

    # Step 3: Prompting the user to enter all of their required details one-by-one and add them to the list new_user_input.

    for i in range(len(temp)-1):
        temp[i] = input(f"Enter the {temp[i]} - ")
    temp[len(temp)-1] = int(input("Enter the Amount - "))

    # Step 4: Creating a dictionary for the new user and add it to the cust_data dictionary.

    tempdict = {}
    for i in range(len(temp)):
        tempdict[NEW_USER_ATTRIBUTES[i]] = temp[i]

    cust_data[accno] = tempdict

    # Step 5: Display the message on successfull account creation to the user.
  
    print(f'''
    Your details are added successfully.
    Your account number is {accno}
    Please don't lose it.
    ''')
    input("Enter anything to continue - ")

# The 'existing_user()' function to get the account details of an existing user from the 'cust_data' dictionary.
def existing_user():
    # Step 1: Ask the user to enter the existing account number and store it as an integer.
  
    accno = int(input("Enter Your Account No. : "))
    while accno not in cust_data:
        accno = int(input("Not found. Please enter your correct account number : "))

    # Step 2: Print the welcome message to the user.
  
    print(f'''
    Welcome, {cust_data[accno]['name']}!
    
    Enter 1 to check your balance.
    Enter 2 to withdraw an amount.
    Enter 3 to deposit an amount.
    ''')
  
    # Step 3: Asking the user to select a valid choice.
    user_choice = input("Enter your choice :")
    while user_choice not in ['1','2','3']:
        print('''
    Invalid input!
              
    Enter 1 to check your balance.
    Enter 2 to withdraw an amount.
    Enter 3 to deposit an amount.
        ''')
        user_choice = input("Enter your choice :")

    # Step 4:
    # If 'user_choice == 1' then display the account balance i.e. 'cust_data[acc_num]['amount']'
    if user_choice == '1':
        print("Account Balance is - ",cust_data[accno]['amount'])
        input("Enter anything to continue - ")

    # Else if 'user_choice == 2' then subtract the withdrawal amount from the available balance.
    elif user_choice == '2':
        w = int(input("Enter the amount to withdraw :"))
        if cust_data[accno]['amount'] < w:
            print('''
    Insufficient balance.
    Available balance: ''',cust_data[accno]['amount'])
        else:
            cust_data[accno]['amount'] -= w
            print('''
    Withdrawal successful.
    Available Balance: ''',cust_data[accno]['amount'])
        input("Enter anything to continue - ")
    # Else if 'user_choice == 3' then add the deposit amount to the available balance.
    elif user_choice == '3':
        d = int(input("Enter the amount to deposit :"))
        cust_data[accno]['amount'] += d
        print('''
    Deposit successful.
    Available Balance: ''',cust_data[accno]['amount'])
        input("Enter anything to continue - ")
    
while(True):
    os.system('cls')
    print('''
    Welcome to the Horizon Bank!
          
    Enter 1 if you are a new customer.
    Enter 2 if you are an existing customer.
    Enter 3 to terminate the application.
    ''')

    user_choice = input("Enter your choice :")

    while user_choice not in ['1','2','3']:
        os.system('cls')
        print('''
    Invalid input!
              
    Enter 1 if you are a new customer.
    Enter 2 if you are an existing customer.
    Enter 3 to terminate the application.
        ''')
        user_choice = input("Enter your choice :")

    if user_choice == '1':
        new_user()
    elif user_choice == '2':
        existing_user()
    else:
        os.system('cls')
        print('''
    Thank you, for banking with us!
        ''')
        exit()