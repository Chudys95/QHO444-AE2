from process import load_reviews_dataset

DATASET_FILE = "Disneyland_reviews.csv"


def main():
    reviews = load_reviews_dataset(DATASET_FILE)
    print("Loaded reviews:", len(reviews))


if __name__ == "__main__":
    main()
