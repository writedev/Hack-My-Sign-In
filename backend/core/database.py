from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+asyncmy://root:rootpassword@localhost:3306/nom_de_ta_db"

# Pour accès async
database = Database(DATABASE_URL)

# Pour les migrations et ORM
metadata = MetaData()
engine = create_engine(DATABASE_URL.replace("asyncmy", "pymysql"))