from app.database.utils import create_tables, get_session
from app.database.models import Driver, Result


create_tables()
session = get_session()

# add some data to the tables
hakkinen = Driver(name="Mika Hakkinen", team="McLaren Mercedes")
schumacher = Driver(name="Michael Schumacher", team="Ferrari")

session.add(hakkinen)
session.add(schumacher)

race1 = Result(grand_prix="1998 Australia", position=1, driver=hakkinen)
race2 = Result(grand_prix="1998 Australia", position=None, driver=schumacher)
race3 = Result(grand_prix="1998 Brasil", position=1, driver=hakkinen)
race4 = Result(grand_prix="1998 Brasil", position=3, driver=schumacher)

session.add(race1)
session.add(race2)
session.add(race3)
session.add(race4)

# Commit the changes to the database
session.commit()
