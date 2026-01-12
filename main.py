from process import load_reviews_dataset as load_data
from process import get_parks as get_parks_list
from process import get_locations as get_locations_list
from process import count_reviews_by_park_and_location as count_reviews

import tui

DATASET_FILE = "Disneyland_reviews.csv"


def analysis_menu(reviews):
    while True:
        tui.print_analysis_menu()
        choice = tui.get_menu_choice(["1", "2", "3", "R"])

        if choice == "1":
            parks = get_parks_list(reviews)
            park = tui.ask_for_park(parks)
            print("Showing reviews for:", park)
            print("(Option 1 already completed earlier)")

        elif choice == "2":
            parks = get_parks_list(reviews)
            locations = get_locations_list(reviews)

            park = tui.ask_for_park(parks)
            location = tui.ask_for_location(locations)

            result = count_reviews(reviews, park, location)
            tui.show_count_result(park, location, result)

        elif choice == "3":
            print("Not implemented yet")

        elif choice == "R":
            break


def main():
    reviews = load_data(DATASET_FILE)
    print("Loaded reviews:", len(reviews))

    while True:
        tui.print_main_menu()
        choice = tui.get_menu_choice(["A", "B", "Q"])

        if choice == "A":
            analysis_menu(reviews)

        elif choice == "B":
            print("Visualisation menu not implemented yet")

        elif choice == "Q":
            print("Exiting program")
            break


if __name__ == "__main__":
    main()
