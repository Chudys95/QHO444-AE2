import matplotlib.pyplot as plt

from process import (
    count_reviews_per_park,
    average_rating_per_location_for_park,
    average_rating_by_month_for_park,
)


def pie_chart_reviews_per_park(reviews):
    counts = count_reviews_per_park(reviews)
    if not counts:
        print("No data available for chart.")
        return

    labels = list(counts.keys())
    sizes = list(counts.values())

    plt.figure()
    plt.title("Number of Reviews per Park")
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.show()


def bar_chart_top_locations_avg_rating(reviews, park, top_n=10, min_reviews=10):
    data = average_rating_per_location_for_park(reviews, park, min_reviews=min_reviews)
    if not data:
        print(
            f"No location data found for {park}. "
            f"(Try lowering min_reviews.)"
        )
        return

    # Sort by average rating (high to low)
    sorted_items = sorted(data.items(), key=lambda x: x[1][0], reverse=True)[:top_n]

    locations = [x[0] for x in sorted_items]
    avgs = [x[1][0] for x in sorted_items]
    counts = [x[1][1] for x in sorted_items]

    plt.figure()
    plt.title(f"Top {top_n} Locations by Highest Average Rating\n{park}")
    plt.bar(locations, avgs)
    plt.xlabel("Reviewer Location")
    plt.ylabel("Average Rating (out of 5)")
    plt.xticks(rotation=45, ha="right")

    # Add count labels above bars (how many reviews that avg is based on)
    for i, v in enumerate(avgs):
        plt.text(i, v, str(counts[i]), ha="center", va="bottom")

    plt.tight_layout()
    plt.show()


def bar_chart_avg_rating_by_month(reviews, park):
    avgs = average_rating_by_month_for_park(reviews, park)
    if not avgs:
        print(f"No monthly data found for {park}.")
        return

    month_names = {
        "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
        "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
        "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec",
    }

    # Ensure month order Jan..Dec
    ordered_months = [f"{i:02d}" for i in range(1, 13)]
    x_labels = []
    y_values = []

    for m in ordered_months:
        if m in avgs:
            x_labels.append(month_names[m])
            y_values.append(avgs[m])

    plt.figure()
    plt.title(f"Average Rating by Month\n{park}")
    plt.bar(x_labels, y_values)
    plt.xlabel("Month")
    plt.ylabel("Average Rating (out of 5)")
    plt.ylim(0, 5)
    plt.tight_layout()
    plt.show()
