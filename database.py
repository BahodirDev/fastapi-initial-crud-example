from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f"postgresql://postgres:sqlme@localhost:5433/test"

engine = create_engine(DATABASE_URL)

Base = declarative_base()
metadata = MetaData()