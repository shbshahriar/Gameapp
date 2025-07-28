from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

# Specify schema in the metadata
from sqlalchemy.schema import MetaData

SCHEMA_NAME = "backend"
metadata = MetaData(schema=SCHEMA_NAME)

# SQLAlchemy Base with custom metadata (schema-aware)
Base = declarative_base(metadata=metadata)

# Database engine
engine = create_engine(DATABASE_URL)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
