from fetch_data import get_data
from country_scheme import Country
import connection


def createEntities(data, *sessions):

    for row in data:
        for session in sessions:
            country = Country(nombre_pais=row["CLDR display name"],
                              capital=row["Capital"],
                              continente=row["Continent"],
                              dial=row["Dial"],
                              geoname_id=row["Geoname ID"],
                              ITU=row["ITU"],
                              lenguajes=row["Languages"],
                              es_independiente=row["is_independent"]
                              )
            session.add(country)


def insertAllData():
    countries = get_data()

    sqliteSession = connection.create_session(connection.sqliteEngine)
    '''
    Before running postsgress session, run the following commands in psql using postgres user:
        CREATE USER postgres SUPERUSER;
        CREATE DATABASE countriesdb WITH OWNER postgres;
    '''
    postgresSession = connection.create_session(connection.postgresEngine)

    createEntities(countries, sqliteSession, postgresSession)

    sqliteSession.commit()
    postgresSession.commit()
