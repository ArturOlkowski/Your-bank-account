import random
import string

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "123456789"
symbol = "!@#$%*[]{};_-"

lenght = 9

all = lower + upper + number + symbol

password = "".join(random.sample(all, lenght))
print("The Password Generate for you is: ", password)

balance = 10000
withdraw = None
deposit = None


def count_digits(writing):
    digit = 0
    for i in writing:
        if i.isdigit():
            digit += 1

    return digit


def count_upper_case(writing):
    u_letter = 0
    for i in writing:
        if i.isupper():
            u_letter += 1

    return u_letter


def count_lower_case(writing):
    l_letter = 0
    for i in writing:
        if i.islower():
            l_letter += 1

    return l_letter


def char(writing):
    symbol = 0
    for i in writing:
        if i in string.punctuation:
            symbol += 1

    return symbol


while True:
    login = input("Please enter your login: ")
    new_password = input("Chose your new password: ")

    if len(new_password) < lenght:
        print("Make sure your new password is at least 9 letters.")
    elif len(new_password) > 15:
        print("Your new password is to long, make sure it is not longer then 15 letters.")
    elif count_digits(new_password) == 0:
        print("Make sure your new password has a number in it.")
    elif count_upper_case(new_password) == 0:
        print("Make sure your new password has upper case in it.")
    elif count_lower_case(new_password) == 0:
        print("Make sure your new password has lower case in it. ")
    elif char(new_password) == 0:
        print("Make sure your new password has char in it. ")

    elif login == "Code_me" and new_password != password:
        print("""Success, new password has been activated!\n
*******************************
|Welcome to your bank account!|
*******************************""")
        break
    else:
        print("Incorrect login, please try again!")

while True:

    decision = input("What do you want to do: balance, deposit, withdraw or exit?: ")


    if decision == "deposit":
        deposit = int(input("How much money do you want to deposit?: "))
        decision2 = input(f"Are you sure you want to deposit {deposit}$ ?: ")
        if decision2 == "Yes":
            balance += deposit
            print(f"You have been deposit {deposit}$, now your current account balance is {balance}$")
        else:
            print("You have been removed to Main menu")
            print(input("What do you want to do: balance, deposit, withdraw or exit?"))

    elif decision == "balance":
        balance == balance
        print(f"Your current balance is: {balance}$")
        print(input("What do you want to do: balance, deposit, withdraw or exit?: "))


    if decision == "withdraw":
        withdraw = int(input("How much money do you want to withdraw?: "))
        withdraw2 = input(f"Are you sure you want to withdraw {withdraw}$ ?: ")
        if withdraw2 == "Yes":
            balance -= withdraw
            print(f"You have been withdraw {withdraw}$, now your current balance is {balance}$")
        elif withdraw2 == "No":
            print("You have been removed to Main menu")
            print(input("What do you want to do: balance, deposit, withdraw or exit?: "))

    elif decision == "balance":
            balance == balance
            print(f"Your current balance is: {balance}$")
            print(input("What do you want to do: balance, deposit, withdraw or exit?: "))

    else:
        print("Good bye, have a nice day!")

        break
