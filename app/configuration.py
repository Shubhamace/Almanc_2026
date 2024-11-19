import os
from dotenv import load_dotenv
class configure:
    load_dotenv()
    db_uname  = os.getenv('DB_User')
    db_name  = os.getenv('DB_Name')
    db_pass  = os.getenv('DB_Password')
    db_host  = os.getenv('DB_Host')
    db_port = os.getenv('DB_Port')
    BEARER_TOKEN = os.getenv('BEARER_TOKEN')
    SQLALCHEMY_DATABASE_URI = f'mssql+pymssql://{db_uname}:{db_pass}@{db_host}:{db_port}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False