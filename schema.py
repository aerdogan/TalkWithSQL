schema = """
Tables and fields:

books(
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    publisher TEXT,
    is_available BOOLEAN
)

users(
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    total_rent_book_count INTEGER,
    current_rent_book_count INTEGER
)

book_events(
    event_id INTEGER PRIMARY KEY,
    event_date DATETIME,
    event_type TEXT, -- 'borrow' veya 'return'
    book_id INTEGER,
    user_id INTEGER
)
"""
