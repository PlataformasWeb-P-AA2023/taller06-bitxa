from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from connection import sqliteEngine, postgresEngine

Base = declarative_base()


class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_id = Column(Integer)
    ITU = Column(String)
    lenguajes = Column(String)
    es_independiente = Column(String)

    def __str__(self):
        return f"Country(id={self.id}, nombre_pais='{self.nombre_pais}', capital='{self.capital}', continente='{self.continente}', dial='{self.dial}', geoname_id={self.geoname_id}, ITU='{self.ITU}', lenguajes='{self.lenguajes}', es_independiente='{self.es_independiente}')"


Base.metadata.create_all(sqliteEngine)
Base.metadata.create_all(postgresEngine)
