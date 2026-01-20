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
        park = row.get("Branch", "").strip()
        if park != "" and park not in parks:
            parks.append(park)

    parks.sort()
    return parks


def get_locations_for_park(reviews, park_name):
    locations = []

    for row in reviews:
        if row.get("Branch", "").strip() != park_name:
            continue

        loc = row.get("Reviewer_Location", "").strip()
        if loc != "" and loc not in locations:
            locations.append(loc)

    locations.sort()
    return locations


def get_years_for_park(reviews, park_name):
    years = []

    for row in reviews:
        if row.get("Branch", "").strip() != park_name:
            continue

        ym = row.get("Year_Month", "").strip()
        if ym == "" or "-" not in ym:
            continue

        year = ym.split("-")[0].strip()
        if year != "" and year not in years:
            years.append(year)

    years.sort()
    return years


def get_reviews_for_park(reviews, park_name):
    result = []

    for row in reviews:
        if row.get("Branch", "").strip() == park_name:
            result.append(row)

    return result


def count_reviews_by_park_and_location(reviews, park_name, location_name):
    count = 0

    for row in reviews:
        park = row.get("Branch", "").strip()
        loc = row.get("Reviewer_Location", "").strip()

        if park == park_name and loc == location_name:
            count += 1

    return count


def average_score_per_year_for_park(reviews, park_name, year_text):
    total = 0
    count = 0

    for row in reviews:
        if row.get("Branch", "").strip() != park_name:
            continue

        ym = row.get("Year_Month", "").strip()
        if not ym.startswith(year_text + "-"):
            continue

        rating_text = row.get("Rating", "").strip()
        try:
            rating = int(rating_text)
        except ValueError:
            continue

        total += rating
        count += 1

    if count == 0:
        return None

    return total / count


def average_score_per_park_by_location(reviews):
    data = {}

    for row in reviews:
        park = row.get("Branch", "").strip()
        loc = row.get("Reviewer_Location", "").strip()
        rating_text = row.get("Rating", "").strip()

        if park == "" or loc == "" or rating_text == "":
            continue

        try:
            rating = int(rating_text)
        except ValueError:
            continue

        if park not in data:
            data[park] = {}

        if loc not in data[park]:
            data[park][loc] = {"total": 0, "count": 0}

        data[park][loc]["total"] += rating
        data[park][loc]["count"] += 1

    result = {}

    for park in data:
        result[park] = {}
        for loc in data[park]:
            result[park][loc] = data[park][loc]["total"] / data[park][loc]["count"]

    return result


def count_reviews_per_park(reviews):
    counts = {}

    for row in reviews:
        park = row.get("Branch", "").strip()
        if park == "":
            continue

        if park not in counts:
            counts[park] = 0

        counts[park] += 1

    return counts


def average_rating_per_location_for_park(reviews, park_name, min_reviews):
    data = {}

    for row in reviews:
        if row.get("Branch", "").strip() != park_name:
            continue

        location = row.get("Reviewer_Location", "").strip()
        rating_text = row.get("Rating", "").strip()

        if location == "" or rating_text == "":
            continue

        try:
            rating = int(rating_text)
        except ValueError:
            continue

        if location not in data:
            data[location] = {"total": 0, "count": 0}

        data[location]["total"] += rating
        data[location]["count"] += 1

    avgs = {}

    for loc in data:
        if data[loc]["count"] >= min_reviews:
            avgs[loc] = data[loc]["total"] / data[loc]["count"]

    return avgs


def average_rating_by_month_for_park(reviews, park_name):
    data = {}

    for row in reviews:
        if row.get("Branch", "").strip() != park_name:
            continue

        ym = row.get("Year_Month", "").strip()
        rating_text = row.get("Rating", "").strip()

        if ym == "" or rating_text == "":
            continue

        parts = ym.split("-")
        if len(parts) < 2:
            continue

        try:
            month_num = int(parts[1])
        except ValueError:
            continue

        try:
            rating = int(rating_text)
        except ValueError:
            continue

        if month_num not in data:
            data[month_num] = {"total": 0, "count": 0}

        data[month_num]["total"] += rating
        data[month_num]["count"] += 1

    avgs = {}

    for m in data:
        if data[m]["count"] > 0:
            avgs[m] = data[m]["total"] / data[m]["count"]

    return avgs
