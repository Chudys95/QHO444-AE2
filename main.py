from process import load_reviews_dataset

DATASET_FILE = "Disneyland_reviews.csv"


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
            print("Analysis menu selected (not working yet)")
        elif choice == "B":
            print("Visualisation menu selected (not working yet)")
        elif choice == "Q":
            print("Exiting program")
            break
        else:
            print("Invalid option, please try again")


if __name__ == "__main__":
    main()
