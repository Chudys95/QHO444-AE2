from process import (
    load_reviews_dataset,
    get_parks,
    get_reviews_for_park,
    count_reviews_for_park_from_location,
    average_rating_for_park_in_year,
    average_score_per_park_by_location,
    get_locations_for_park,
)


from tui import (
    show_main_menu,
    show_view_data_menu,
    show_visual_menu,
    ask_choice,
    ask_park,
    ask_location,
    ask_year,
    pause,
)

from visual import (
    pie_chart_reviews_per_park,
    bar_chart_top_locations_avg_rating,
    bar_chart_avg_rating_by_month,
)

from exporter import ParkDataExporter


DATASET_FILE = "Disneyland_reviews.csv"
MIN_REVIEWS_FOR_LOCATION = 10
TOP_LOCATIONS = 10


def get_locations_for_park(reviews, park):
    locations = set()
    for r in reviews:
        if r.get("Branch") == park:
            loc = (r.get("Reviewer_Location") or "").strip()
            if loc:
                locations.add(loc)
    return locations




def handle_view_data_menu(reviews):
    parks = get_parks(reviews)

    while True:
        show_view_data_menu()
        choice = ask_choice("Select an option: ").upper()

        if choice == "1":
            park = ask_park(parks)
            park_reviews = get_reviews_for_park(reviews, park)
            print(f"\nShowing {len(park_reviews)} reviews for: {park}\n")
            for r in park_reviews:
                rating = r.get("Rating", "")
                ym = r.get("Year_Month", "")
                loc = r.get("Reviewer_Location", "")
                print(f"- Rating: {rating} | {ym} | {loc}")

            pause()




        elif choice == "2":

            park = ask_park(parks)
            all_locations = get_locations_for_park(reviews, park)
            if not all_locations:
                print(f"\nNo location data found for {park}.\n")
                pause()

                return

            location = ask_location(all_locations)
            total = count_reviews_for_park_from_location(reviews, park, location)
            print(f"\n{park} has {total} reviews from {location}.\n")

            pause()




        elif choice == "3":
            park = ask_park(parks)
            year = ask_year()
            avg = average_rating_for_park_in_year(reviews, park, year)
            if avg is None:
                print(f"\nNo reviews found for {park} in {year}.\n")
            else:
                print(f"\nAverage rating for {park} in {year}: {avg:.2f}\n")
            pause()

        elif choice == "4":
            print("\nAverage score per park by reviewer location:\n")
            data = average_score_per_park_by_location(reviews)
            for park, locations in data.items():
                print(f"\n=== {park} ===")
                for location, avg in sorted(locations.items(), key=lambda x: x[0].lower()):
                    print(f"{location}: {avg:.2f}")
            print()
            pause()

        elif choice == "X":
            break

        else:
            print("\nInvalid choice. Try again.\n")

def ask_location(all_locations):
    loc_list = sorted(all_locations)
    display_line = " | ".join(loc_list)

    print("\nAvailable locations:")
    print(display_line)

    while True:
        choice = input("\nEnter location exactly as shown: ").strip()
        if choice in all_locations:
            return choice
        print("Invalid location. Try again.")




def handle_visual_menu(reviews):
    parks = get_parks(reviews)

    while True:
        show_visual_menu()
        choice = ask_choice("Select an option: ").upper()

        if choice == "1":
            pie_chart_reviews_per_park(reviews)
            pause()

        elif choice == "2":
            park = ask_park(parks)
            bar_chart_top_locations_avg_rating(
                reviews,
                park,
                top_n=TOP_LOCATIONS,
                min_reviews=MIN_REVIEWS_FOR_LOCATION,
            )
            pause()

        elif choice == "3":
            park = ask_park(parks)
            bar_chart_avg_rating_by_month(reviews, park)
            pause()

        elif choice == "X":
            break

        else:
            print("\nInvalid choice. Try again.\n")


def handle_export_menu(reviews):
    exporter = ParkDataExporter(reviews)

    while True:
        print("\n--- Export Data (OOP) ---")
        print("Choose export format:")
        print("1 - TXT")
        print("2 - CSV")
        print("3 - JSON")
        print("X - Back")

        choice = ask_choice("Select an option: ").upper()

        if choice == "1":
            filename = "park_summary.txt"
            exporter.export_txt(filename)
            print(f"\nExported to {filename}\n")
            pause()

        elif choice == "2":
            filename = "park_summary.csv"
            exporter.export_csv(filename)
            print(f"\nExported to {filename}\n")
            pause()

        elif choice == "3":
            filename = "park_summary.json"
            exporter.export_json(filename)
            print(f"\nExported to {filename}\n")
            pause()

        elif choice == "X":
            break

        else:
            print("\nInvalid choice. Try again.\n")


def main():
    print("Disneyland Review Analysis Tool\n")

    reviews = load_reviews_dataset(DATASET_FILE)
    print(f"Dataset loaded. Rows read: {len(reviews)}\n")

    while True:
        show_main_menu()
        choice = ask_choice("Select an option: ").upper()
        print(f"\nYou selected: {choice}\n")

        if choice == "A":
            handle_view_data_menu(reviews)

        elif choice == "B":
            handle_visual_menu(reviews)

        elif choice == "C":
            handle_export_menu(reviews)

        elif choice == "X":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose A, B, C or X.\n")


if __name__ == "__main__":
    main()
