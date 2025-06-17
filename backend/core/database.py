from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+asyncmy://root:rootpassword@localhost:3306/HackMySignIn"

#ForAsyncAccess
database = Database(DATABASE_URL)

# For migration and orm
metadata = MetaData()
engine = create_engine(DATABASE_URL.replace("asyncmy", "pymysql"))