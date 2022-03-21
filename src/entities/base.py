from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

base = SQLAlchemy(metadata=MetaData())
