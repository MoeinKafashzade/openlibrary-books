# Open Library Books Collector

A small Python project that retrieves books from the public Open Library Search API, keeps books whose first publication year is after 2000, sorts them, and saves the result to a CSV file.

## Features

- Uses the public Open Library Search API
- Collects 50 matching books
- Filters books with `first_publish_year > 2000`
- Sorts the CSV by publication year and title
- Handles multiple API pages when necessary
- Uses `requests` and Python's standard `csv` library
- UTF-8 CSV output

## Project structure

```text
openlibrary-books/
├── books_api.py
├── books.csv
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.9+
- `requests`

## Installation

```bash
pip install -r requirements.txt
```

If you use Conda:

```bash
conda create -n openlibrary-books python=3.11
conda activate openlibrary-books
pip install -r requirements.txt
```

## Run

```bash
python books_api.py
```

After execution, the script creates:

```text
books.csv
```

The CSV contains:

- `title`
- `authors`
- `first_publish_year`
- `openlibrary_key`

## API

This project uses the Open Library Search API:

https://openlibrary.org/search.json

The script requests only the fields it needs and uses pagination until it has collected 50 books published after 2000.

## GitHub

Suggested repository name:

```text
openlibrary-books
```

## Notes

Open Library's API is intended for book discovery and public-good/library projects. The project keeps API requests small and uses pagination instead of bulk downloading the Open Library dataset.
