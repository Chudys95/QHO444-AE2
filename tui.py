def show_main_menu():
    print("\n=== Main Menu ===")
    print("A - View Data")
    print("B - View Visuals")
    print("C - Export Data (OOP)")
    print("X - Exit")


def show_view_data_menu():
    print("\n=== View Data Menu (A) ===")
    print("1 - View all reviews for a specific park")
    print("2 - Count reviews for a park from a location")
    print("3 - Average rating for a park in a year")
    print("4 - Average score per park by reviewer location")
    print("X - Back")


def show_visual_menu():
    print("\n=== Visual Menu (B) ===")
    print("1 - Pie chart: number of reviews per park")
    print("2 - Bar chart: top locations by highest average rating (per park)")
    print("3 - Bar chart: average rating by month (per park)")
    print("X - Back")


def ask_choice(prompt_text):
    return input(prompt_text).strip()


def ask_park(parks):
    while True:
        print("\nAvailable parks:")
        for p in parks:
            print(f"- {p}")
        park = input("\nEnter park name exactly as shown: ").strip()

        if park in parks:
            return park

        print("\nInvalid park name. Please try again.\n")


def ask_location(all_locations):
    print("\nAvailable locations:")
    for loc in sorted(all_locations):
        print(f"- {loc}")

    while True:
        choice = input("\nEnter location exactly as shown: ").strip()
        if choice in all_locations:
            return choice
        print("Invalid location. Try again.")



def ask_year():
    while True:
        year_text = input("Enter year (e.g., 2019): ").strip()
        if year_text.isdigit() and len(year_text) == 4:
            return int(year_text)
        print("Invalid year. Try again.\n")


def pause():
    input("\nPress Enter to continue...")
