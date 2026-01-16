import matplotlib.pyplot as plt

def pie_chart_reviews_per_park(counts):
    parks = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=parks, autopct="%1.1f%%")
    plt.title("Number of Reviews per Park")
    plt.show()
