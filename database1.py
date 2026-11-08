from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
DATABASE_URL= "mysql+pymysql://root:Gowri%40123@localhost/library_db"

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base=declarative_base()

try:
    connection = engine.connect()
    print("Database connected successfully!")
    connection.close()
except Exception as e:
    print("Database connection failed:", e)