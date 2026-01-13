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


def filter_reviews_by_park(reviews, park):
    result = []
    for row in reviews:
        if row.get("Branch") == park:
            result.append(row)
    return result


def get_years(reviews):
    years = []

    for row in reviews:
        year = row.get("Year")

        if not year:
            ym = row.get("Year_Month")
            if ym and len(ym) >= 4:
                year = ym[:4]

        # only allow real 4-digit years
        if year and len(year) == 4 and year.isdigit():
            if year not in years:
                years.append(year)

    years.sort()
    return years


def average_rating_by_park_and_year(reviews, park, year):
    total = 0
    count = 0

    for row in reviews:
        row_year = row.get("Year")

        if not row_year:
            ym = row.get("Year_Month")
            if ym and len(ym) >= 4:
                row_year = ym[:4]

        # skip bad years like "miss"
        if not (row_year and len(row_year) == 4 and row_year.isdigit()):
            continue

        if row.get("Branch") == park and row_year == year:
            rating_text = row.get("Rating")
            if rating_text:
                try:
                    rating_num = int(rating_text)
                    total += rating_num
                    count += 1
                except ValueError:
                    pass

    if count == 0:
        return None

    return total / count
