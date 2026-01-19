from process import (
    load_reviews_dataset,
    get_parks,
    count_reviews_per_park,
    average_rating_per_location_for_park,
    average_rating_by_month_for_park
)

from visual import (
    pie_chart_reviews_per_park,
    bar_chart_top_locations,
    bar_chart_avg_rating_by_month
)

from tui import (
    show_main_menu,
    show_visual_menu,
    get_choice
)


DATASET_FILE = "Disneyland_reviews.csv"
MIN_REVIEWS_FOR_LOCATION = 10


def visual_menu(reviews):
    while True:
        show_visual_menu()
        choice = get_choice("Select an option: ")

        if choice == "1":
            counts = count_reviews_per_park(reviews)
            pie_chart_reviews_per_park(counts)

        elif choice == "2":
            parks = get_parks(reviews)
            print("\nParks:", ", ".join(parks))
            park = input("Enter park name: ").strip()

            avgs = average_rating_per_location_for_park(reviews, park, MIN_REVIEWS_FOR_LOCATION)
            bar_chart_top_locations(avgs, park, MIN_REVIEWS_FOR_LOCATION)

        elif choice == "3":
            parks = get_parks(reviews)
            print("\nParks:", ", ".join(parks))
            park = input("Enter park name: ").strip()

            avgs = average_rating_by_month_for_park(reviews, park)
            bar_chart_avg_rating_by_month(avgs, park)

        elif choice == "R":
            break

        else:
            print("Invalid option, try again.")


def main():
    reviews = load_reviews_dataset(DATASET_FILE)
    print("Loaded reviews:", len(reviews))

    while True:
        show_main_menu()
        choice = get_choice("Select an option: ")

        if choice == "A":
            print("Analysis menu not included here.")

        elif choice == "B":
            visual_menu(reviews)

        elif choice == "Q":
            print("Exiting program")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
