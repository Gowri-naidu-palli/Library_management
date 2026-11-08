from database1 import Base
from sqlalchemy import Column, Integer, String

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    author = Column(String(100))


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))

class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer)
    book_id = Column(Integer)



# from database1 import Base
# from sqlalchemy import Column, Integer, String


# class Book(Base):
#     __tablename__ = "books"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(100))
#     author = Column(String(100))
