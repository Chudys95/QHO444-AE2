from process import (
    load_reviews_dataset,
    get_parks,
    get_locations_for_park,
    get_years_for_park,
    get_reviews_for_park,
    count_reviews_by_park_and_location,
    average_score_per_year_for_park,
    average_score_per_park_by_location,
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
    print_title_banner,
    show_main_menu,
    show_analysis_menu,
    show_visual_menu,
    get_choice
)

DATASET_FILE = "Disneyland_reviews.csv"
MIN_REVIEWS_FOR_LOCATION = 10


def analysis_menu(reviews):
    while True:
        show_analysis_menu()
        choice = get_choice("Please enter your choice: ")

        if choice == "A":
            parks = get_parks(reviews)
            print("\nAvailable parks:", ", ".join(parks))
            park = input("Enter park name: ").strip()

            park_reviews = get_reviews_for_park(reviews, park)

            if len(park_reviews) == 0:
                print("No reviews found for that park.\n")
            else:
                print(f"\nReviews for {park}:\n")
                for r in park_reviews:
                    rating = r.get("Rating", "").strip()
                    location = r.get("Reviewer_Location", "").strip()
                    date = r.get("Year_Month", "").strip()

                    if location == "":
                        location = "Unknown"
                    if date == "":
                        date = "Unknown"

                    print(f"Rating: {rating} | Location: {location} | Date: {date}")
                print()

        elif choice == "B":
            parks = get_parks(reviews)
            print("\nAvailable parks:", ", ".join(parks))
            park = input("Enter park name: ").strip()

            locations = get_locations_for_park(reviews, park)
            if len(locations) == 0:
                print("No locations found for that park.\n")
            else:
                print("\nAvailable locations:", ", ".join(locations))
                location = input("Enter reviewer location: ").strip()
                count = count_reviews_by_park_and_location(reviews, park, location)
                print(f"\nNumber of reviews for {park} from {location}: {count}\n")

        elif choice == "C":
            parks = get_parks(reviews)
            print("\nAvailable parks:", ", ".join(parks))
            park = input("Enter park name: ").strip()

            years = get_years_for_park(reviews, park)
            if len(years) == 0:
                print("No years found for that park.\n")
            else:
                print("\nAvailable years:", ", ".join(years))
                year = input("Enter year (YYYY): ").strip()
                avg = average_score_per_year_for_park(reviews, park, year)

                if avg is None:
                    print("No data found for that park/year.\n")
                else:
                    print(f"\nAverage rating for {park} in {year}: {avg:.2f}\n")

        elif choice == "D":
            results = average_score_per_park_by_location(reviews)
            if len(results) == 0:
                print("No data found.\n")
            else:
                for park in sorted(results.keys()):
                    print(f"\n{park}")
                    for loc in sorted(results[park].keys()):
                        print(f"  {loc}: {results[park][loc]:.2f}")
                print()

        elif choice == "R":
            break

        else:
            print("Invalid option, try again.\n")


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
            print("Invalid option, try again.\n")


def main():
    print_title_banner("Disneyland Review Analyser")

    print("Loading dataset...")
    reviews = load_reviews_dataset(DATASET_FILE)
    print(f"Finished reading dataset, {len(reviews)} rows found.\n")

    while True:
        show_main_menu()
        choice = get_choice("Please enter your desired option: ")

        if choice == "A":
            analysis_menu(reviews)

        elif choice == "B":
            visual_menu(reviews)

        elif choice == "X":
            print("Exiting program...")
            break

        else:
            print("Invalid option, try again.\n")


if __name__ == "__main__":
    main()
