import csv


def load_reviews_dataset(file_path):
    reviews = []

    with open(file_path, mode="r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            reviews.append(row)

    return reviews


def get_parks(reviews):
    parks = []

    for row in reviews:
        park = row.get("Branch")
        if park and park not in parks:
            parks.append(park)

    return parks


def get_locations(reviews):
    locations = []

    for row in reviews:
        location = row.get("Reviewer_Location")
        if location and location not in locations:
            locations.append(location)

    return locations


def count_reviews_by_park_and_location(reviews, park, location):
    count = 0

    for row in reviews:
        if row.get("Branch") == park and row.get("Reviewer_Location") == location:
            count += 1

    return count
