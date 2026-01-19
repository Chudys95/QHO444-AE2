import matplotlib.pyplot as plt


def pie_chart_reviews_per_park(counts):
    parks = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=parks, autopct="%1.1f%%")
    plt.title("Number of Reviews per Park")
    plt.tight_layout()
    plt.show()


def bar_chart_top_locations(avg_ratings, park_name, min_reviews):
    if len(avg_ratings) == 0:
        print("No location data with at least", min_reviews, "reviews for:", park_name)
        return

    sorted_ratings = sorted(avg_ratings.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_ratings[:10]

    locations = [item[0] for item in top_10]
    ratings = [item[1] for item in top_10]

    plt.figure(figsize=(10, 5))
    plt.bar(locations, ratings)
    plt.title("Top 10 Locations by Average Rating (" + park_name + ")")
    plt.xlabel("Location (min " + str(min_reviews) + " reviews)")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def bar_chart_avg_rating_by_month(avg_by_month, park_name):
    if len(avg_by_month) == 0:
        print("No month data found for:", park_name)
        return

    months = list(range(1, 13))
    ratings = []

    for m in months:
        if m in avg_by_month:
            ratings.append(avg_by_month[m])
        else:
            ratings.append(0)

    plt.figure(figsize=(10, 5))
    plt.bar(months, ratings)
    plt.title("Average Rating by Month (" + park_name + ")")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.xticks(months)
    plt.tight_layout()
    plt.show()
