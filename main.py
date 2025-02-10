import sys, os
from verify.checkers import Checkers

def test_email_address():
    os.system('cls' if os.name == 'nt' else 'clear')
    user_mail = input("Please enter your email address: ")
    local_part = Checkers.check_if_name_before_at_sign(user_mail)
    at_sign = Checkers.check_if_there_is_one_at_sign(user_mail)
    domain = Checkers.check_for_domain_name(user_mail)
    count = 0
    if local_part == True:
        print("\nYour email have a correct local part.")
        count += 1
    else:
        print("There is an issue with your email local part.")
    if at_sign == True:
        print("Your email have one at sign.")
        count += 1
    else:
        print("There is an issue with your email at sign.")
    if domain == True:
        print("Your email have a correct domain name.")
        count += 1
    else:
        print("There is an issue with your email domain name.")
    if count == 3:
        print("\nYour email address respect all naming rules.")
    else:
        print("\nYour email address present some issues, see above prompt to see what's wrong.")

if __name__ == "__main__":
    print("Welcome to this email checker!")
    while True:
        print("\n-------------------------------------------------")
        print("Please select an option:")
        print("1. Run Email Verifier")
        print("2. Exit")
        choice = input("Enter your choice [1/2]: ").strip()
        if choice == "1":
            print("Running Email Verifier...")
            test_email_address()
        elif choice == "2":
            print("Exiting...")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please give a correct input.")
