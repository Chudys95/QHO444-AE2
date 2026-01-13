def print_main_menu():
    print("\nMain Menu")
    print("A - Analysis")
    print("B - Visualisation")
    print("Q - Quit")


def print_analysis_menu():
    print("\nAnalysis Menu")
    print("1 - View Reviews by Park")
    print("2 - Number of Reviews by Park and Location")
    print("3 - Average Rating by Park and Year")
    print("R - Return to main menu")


def get_menu_choice(valid_choices):
    while True:
        choice = input("Select an option: ").strip().upper()
        if choice in valid_choices:
            return choice
        print("Invalid option, please try again")


def ask_for_park(parks):
    print("\nAvailable parks:")
    for p in parks:
        print("-", p)

    while True:
        park = input("\nType park name exactly as shown: ").strip()
        if park in parks:
            return park
        print("Invalid park, try again")


def ask_for_location(locations):
    print("\nAvailable reviewer locations:")
    for l in locations:
        print("-", l)

    while True:
        location = input("\nType location exactly as shown: ").strip()
        if location in locations:
            return location
        print("Invalid location, try again")


def ask_for_year(years):
    print("\nAvailable years:")
    for y in years:
        print("-", y)

    while True:
        year = input("\nType year exactly as shown: ").strip()
        if year in years:
            return year
        print("Invalid year, try again")


def show_count_result(park, location, count):
    print("\nResult")
    print("Park:", park)
    print("Reviewer location:", location)
    print("Number of reviews:", count)


def show_reviews(reviews_list):
    print("\nTotal reviews found:", len(reviews_list))
    print("-" * 40)

    for r in reviews_list:
        print("Park:", r.get("Branch", "N/A"))
        print("Reviewer location:", r.get("Reviewer_Location", "N/A"))
        print("Rating:", r.get("Rating", "N/A"))

        if "Review_Text" in r:
            print("Review:", r.get("Review_Text", "").strip())
        elif "Review" in r:
            print("Review:", r.get("Review", "").strip())

        print("-" * 40)


def show_average_result(park, year, avg_value):
    print("\nResult")
    print("Park:", park)
    print("Year:", year)

    if avg_value is None:
        print("No reviews found for that park/year.")
    else:
        print("Average rating:", round(avg_value, 2))
