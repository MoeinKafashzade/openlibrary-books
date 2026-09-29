import csv
import requests

API_URL = "https://openlibrary.org/search.json"
OUTPUT_FILE = "books.csv"
BOOK_COUNT = 50
MIN_YEAR = 2000
PAGE_SIZE = 50


def fetch_books():
    """Fetch books from Open Library until we collect BOOK_COUNT valid books."""
    books = []
    page = 1

    while len(books) < BOOK_COUNT:
        params = {
            "q": "book",
            "fields": "key,title,author_name,first_publish_year",
            "sort": "new",
            "page": page,
            "limit": PAGE_SIZE,
        }

        response = requests.get(API_URL, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        for book in data.get("docs", []):
            year = book.get("first_publish_year")

            if isinstance(year, int) and year > MIN_YEAR:
                books.append(
                    {
                        "title": book.get("title", "Unknown"),
                        "authors": ", ".join(book.get("author_name", [])),
                        "first_publish_year": year,
                        "openlibrary_key": book.get("key", ""),
                    }
                )

                if len(books) == BOOK_COUNT:
                    break

        if not data.get("docs"):
            break

        page += 1

    return books


def save_to_csv(books):
    """Sort books by publication year and save them to a CSV file."""
    books.sort(key=lambda book: (book["first_publish_year"], book["title"].lower()))

    fieldnames = [
        "title",
        "authors",
        "first_publish_year",
        "openlibrary_key",
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


def main():
    books = fetch_books()

    if not books:
        print("No matching books were found.")
        return

    save_to_csv(books)
    print(f"Saved {len(books)} books to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
