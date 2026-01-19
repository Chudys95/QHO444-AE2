import matplotlib.pyplot as plt

def pie_chart_reviews_per_park(counts):
    parks = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=parks, autopct="%1.1f%%")
    plt.title("Number of Reviews per Park")
    plt.tight_layout()
    plt.show()


def bar_chart_top_locations(avg_ratings):
    sorted_ratings = sorted(avg_ratings.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_ratings[:10]

    locations = [item[0] for item in top_10]
    ratings = [item[1] for item in top_10]

    plt.figure(figsize=(10, 5))
    plt.bar(locations, ratings)
    plt.title("Top 10 Reviewer Locations by Average Rating")
    plt.xlabel("Location")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def bar_chart_avg_rating_by_month(avg_by_month):
    months = sorted(avg_by_month.keys())
    ratings = [avg_by_month[m] for m in months]

    plt.figure(figsize=(10, 5))
    plt.bar(months, ratings)
    plt.title("Average Rating by Month")
    plt.xlabel("Month (1–12)")
    plt.ylabel("Average Rating")
    plt.xticks(months)
    plt.tight_layout()
    plt.show()
