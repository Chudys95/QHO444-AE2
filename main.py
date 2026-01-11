from process import load_reviews_dataset

DATASET_FILE = "Disneyland_reviews.csv"


def analysis_menu():
    while True:
        print("\nAnalysis Menu")
        print("1 - Option 1 (TEST)")
        print("2 - Option 2 (TEST)")
        print("3 - Option 3 (TEST)")
        print("R - Return to main menu")

        choice = input("Select an option: ").strip().upper()

        if choice == "1":
            print("Option 1 selected (TEST)")
        elif choice == "2":
            print("Option 2 selected (TEST)")
        elif choice == "3":
            print("Option 3 selected (TEST)")
        elif choice == "R":
            break
        else:
            print("Invalid option, please try again")


def main():
    reviews = load_reviews_dataset(DATASET_FILE)
    print("Loaded reviews:", len(reviews))

    while True:
        print("\nMain Menu")
        print("A - Analysis")
        print("B - Visualisation")
        print("Q - Quit")

        choice = input("Select an option: ").strip().upper()

        if choice == "A":
            analysis_menu()
        elif choice == "B":
            print("Visualisation menu selected (Test)")
        elif choice == "Q":
            print("Exiting program")
            break
        else:
            print("Invalid option, please try again")


if __name__ == "__main__":
    main()
