def show_main_menu():
    print("\nMain Menu")
    print("A - Analysis")
    print("B - Visualisation")
    print("Q - Quit")


def show_visual_menu():
    print("\nVisualisation Menu")
    print("1 - Pie Chart: Reviews per Park")
    print("2 - Bar Chart: Top 10 Locations by Average Rating")
    print("3 - Bar Chart: Average Rating by Month")
    print("R - Return to main menu")


def get_choice(text):
    return input(text).strip().upper()
