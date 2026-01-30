import csv
from collections import defaultdict


def load_reviews_dataset(filename):
    reviews = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Clean and convert fields
                row["Rating"] = safe_int(row.get("Rating"))
                row["Year_Month"] = (row.get("Year_Month") or "").strip()
                row["Reviewer_Location"] = (row.get("Reviewer_Location") or "").strip()
                row["Branch"] = (row.get("Branch") or "").strip()
                reviews.append(row)

    except FileNotFoundError:
        print(f"ERROR: File not found: {filename}")
        print("Make sure Disneyland_reviews.csv is in the same folder as main.py.")
        return []

    return reviews

def get_locations_for_park(reviews, park):
    locations = set()
    for r in reviews:
        if r.get("Branch") == park:
            loc = (r.get("Reviewer_Location") or "").strip()
            if loc:
                locations.add(loc)
    return locations



def safe_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def get_parks(reviews):
    parks = sorted({r["Branch"] for r in reviews if r.get("Branch")})
    return parks


def get_reviews_for_park(reviews, park):
    return [r for r in reviews if r.get("Branch") == park]


def count_reviews_for_park_from_location(reviews, park, location):
    location_lower = location.strip().lower()
    total = 0

    for r in reviews:
        if r.get("Branch") == park:
            loc = (r.get("Reviewer_Location") or "").lower()
            if loc == location_lower:
                total += 1

    return total


def average_rating_for_park_in_year(reviews, park, year):
    total = 0
    count = 0

    for r in reviews:
        if r.get("Branch") != park:
            continue

        ym = r.get("Year_Month") or ""
        if len(ym) >= 4 and ym[:4].isdigit():
            row_year = int(ym[:4])
            if row_year == year:
                rating = r.get("Rating")
                if rating is not None:
                    total += rating
                    count += 1

    if count == 0:
        return None

    return total / count


def count_reviews_per_park(reviews):
    counts = defaultdict(int)
    for r in reviews:
        park = r.get("Branch")
        if park:
            counts[park] += 1
    return dict(counts)


def average_rating_per_location_for_park(reviews, park, min_reviews=10):
    # Returns dict: location -> (avg_rating, review_count)
    totals = defaultdict(int)
    counts = defaultdict(int)

    for r in reviews:
        if r.get("Branch") != park:
            continue

        location = r.get("Reviewer_Location") or ""
        rating = r.get("Rating")
        if not location or rating is None:
            continue

        totals[location] += rating
        counts[location] += 1

    result = {}
    for location, c in counts.items():
        if c >= min_reviews:
            result[location] = (totals[location] / c, c)

    return result


def average_rating_by_month_for_park(reviews, park):
    # Month here is just the MM part of YYYY-MM.
    totals = defaultdict(int)
    counts = defaultdict(int)

    for r in reviews:
        if r.get("Branch") != park:
            continue

        ym = (r.get("Year_Month") or "").strip()
        rating = r.get("Rating")
        if rating is None or len(ym) < 7 or ym[4] != "-":
            continue

        month = ym[5:7]
        if month.isdigit():
            totals[month] += rating
            counts[month] += 1

    avgs = {}
    for month, c in counts.items():
        avgs[month] = totals[month] / c

    return avgs


def average_score_per_park_by_location(reviews):
    # Returns: park -> { location -> avg }
    totals = defaultdict(lambda: defaultdict(int))
    counts = defaultdict(lambda: defaultdict(int))

    for r in reviews:
        park = r.get("Branch") or ""
        location = r.get("Reviewer_Location") or ""
        rating = r.get("Rating")

        if not park or not location or rating is None:
            continue

        totals[park][location] += rating
        counts[park][location] += 1

    result = {}
    for park in totals:
        result[park] = {}
        for location in totals[park]:
            result[park][location] = totals[park][location] / counts[park][location]

    return result
