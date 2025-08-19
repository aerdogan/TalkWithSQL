schema = """
Tables and fields:

books(
    id INTEGER PRIMARY KEY,
    title TEXT,
    publisher TEXT,
    is_available BOOLEAN
)

users(
    id INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    age INTEGER,
    total_rent_book_count INTEGER,
    current_rent_book_count INTEGER
)

book_events(
    id INTEGER PRIMARY KEY,
    create_date DATETIME,
    book_id INTEGER,
    user_id INTEGER,
    given TEXT
)
"""
