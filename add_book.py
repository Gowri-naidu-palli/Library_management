from database1 import SessionLocal
from models import Book

db = SessionLocal()

book = Book(
    title="Python Programming",
    author="Gowri"
)

db.add(book)
db.commit()
db.refresh(book)

print("Book added successfully!")
print("Book ID:", book.id)

db.close()