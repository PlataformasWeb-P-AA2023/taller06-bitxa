from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# make echo = True if wanna see SQL results.
sqliteEngine = create_engine('sqlite:///countries.db', echo=False)
postgresEngine = create_engine(
    "postgresql+psycopg2://postgres@localhost:5432/countriesdb", echo=False)


def create_session(engine):
    return sessionmaker(bind=engine)()
