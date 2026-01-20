def print_title_banner(title):
    dashes = "-" * len(title)
    print(dashes)
    print(title)
    print(dashes)


def show_main_menu():
    print("Please enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")


def show_analysis_menu():
    print("Please enter one of the following options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per Year by Park")
    print("[D] Average Score per Park by Reviewer Location")
    print("[R] Return to Main Menu")


def show_visual_menu():
    print("\nVisualisation Menu")
    print("1 - Pie Chart: Reviews per Park")
    print("2 - Bar Chart: Top 10 Locations by Average Rating")
    print("3 - Bar Chart: Average Rating by Month")
    print("R - Return to main menu")


def get_choice(text):
    return input(text).strip().upper()
