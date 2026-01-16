from process import load_reviews_dataset, count_reviews_per_park
from visual import pie_chart_reviews_per_park

DATASET_FILE = "Disneyland_reviews.csv"

def analysis_menu(reviews):
    while True:
        print("\nAnalysis Menu")
        print("1 - View Reviews by Park")
        print("2 - Count Reviews by Park and Location")
        print("3 - Average Rating by Park and Year")
        print("R - Return to main menu")

        choice = input("Select an option: ").strip().upper()

        if choice == "1":
            park = input("Enter park name: ").strip()
            park_reviews = [r for r in reviews if r["Park"] == park]
            print("Found", len(park_reviews), "reviews for", park)
        elif choice == "2":
            print("Option 2 already implemented earlier.")
        elif choice == "3":
            print("Option 3 already implemented earlier.")
        elif choice == "R":
            break
        else:
            print("Invalid option, try again.")

def visual_menu(reviews):
    while True:
        print("\nVisualisation Menu")
        print("1 - Pie Chart: Reviews per Park")
        print("R - Return to main menu")

        choice = input("Select an option: ").strip().upper()

        if choice == "1":
            counts = count_reviews_per_park(reviews)
            pie_chart_reviews_per_park(counts)
        elif choice == "R":
            break
        else:
            print("Invalid option, try again.")

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
            analysis_menu(reviews)
        elif choice == "B":
            visual_menu(reviews)
        elif choice == "Q":
            print("Exiting program")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
