import sys

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
        elif choice == "2":
            print("Exiting...")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please give a correct input.")
