from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()

class Lithuanian_cities(base):
    __tablename__ = "Lithuanian Cities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    region = Column(String)
    population = Column(String)
    # country = Column(String)

# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the session() sublass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# create cities 
# vilnius = Lithuanian_cities(
#     name = "Vilnius",
#     region = "Aukštaitija",
#     population = 542000
# )

# kaunas = Lithuanian_cities(
#     name = "Kaunas",
#     region = "Suvalkija",
#     population = 292000
# )

# klaipeda = Lithuanian_cities(
#     name = "Klaipipėda",
#     region = "Žemaitija",
#     population = 147000
# )

# siauliai = Lithuanian_cities(
#     name = "Šiauliai",
#     region = "Žemaitija",
#     population = 103000
# )

# panevezys = Lithuanian_cities(
#     name = "Panevvėžys",
#     region = "Aukštaitija",
#     population = 94400
# )

# session.add(vilnius)
# session.add(kaunas)
# session.add(klaipeda)
# session.add(siauliai)
# session.add(panevezys)

# session.commit()

# alytus = Lithuanian_cities(
#     name = "Alytus",
#     region = "Aukstaitija",
#     population = 100
# )

# session.add(alytus)

# update_alytus = session.query(Lithuanian_cities).filter_by(id=6).first()
# update_alytus.population = 53400
# update_alytus.region = "Dzūkija"
# session.commit()

# london = Lithuanian_cities(
#     name = "London",
#     region = "Greater London",
#     population = 8982000
# )

# session.add(london)
# session.commit()

# delete london

# delete_london = session.query(Lithuanian_cities).filter_by(name="London").first()
# session.delete(delete_london)

# session.commit()

# add country to cities

# l_cities = session.query(Lithuanian_cities)
# for i in l_cities:
#     i.country = "Lithuania"
#     session.commit()


cities = session.query(Lithuanian_cities)
for city in cities:
    print(
         city.id,
        "Name: " + city.name,
        "Region: " +city.region,
        "Population: " + city.population,
        # "Country: " + city.country,
        sep=" | "
    )