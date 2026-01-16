import csv

def load_reviews_dataset(file_path):
    reviews = []

    with open(file_path, mode="r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            reviews.append(row)

    return reviews


def count_reviews_per_park(reviews):
    counts = {}

    for r in reviews:
        park = r.get("Branch", "").strip()

        if park == "":
            continue

        if park not in counts:
            counts[park] = 0

        counts[park] += 1

    return counts
