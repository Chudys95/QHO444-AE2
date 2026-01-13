from process import load_reviews_dataset as load_data
from process import get_parks as get_parks_list
from process import get_locations as get_locations_list
from process import count_reviews_by_park_and_location as count_reviews
from process import filter_reviews_by_park as filter_by_park
from process import get_years as get_years_list
from process import average_rating_by_park_and_year as avg_by_park_year

import tui

DATASET_FILE = "Disneyland_reviews.csv"


def analysis_menu(reviews):
    while True:
        tui.print_analysis_menu()
        choice = tui.get_menu_choice(["1", "2", "3", "R"])

        if choice == "1":
            parks = get_parks_list(reviews)
            park = tui.ask_for_park(parks)
            park_reviews = filter_by_park(reviews, park)
            tui.show_reviews(park_reviews)

        elif choice == "2":
            parks = get_parks_list(reviews)
            locations = get_locations_list(reviews)

            park = tui.ask_for_park(parks)
            location = tui.ask_for_location(locations)

            result = count_reviews(reviews, park, location)
            tui.show_count_result(park, location, result)

        elif choice == "3":
            parks = get_parks_list(reviews)
            years = get_years_list(reviews)

            park = tui.ask_for_park(parks)
            year = tui.ask_for_year(years)

            avg_value = avg_by_park_year(reviews, park, year)
            tui.show_average_result(park, year, avg_value)

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
