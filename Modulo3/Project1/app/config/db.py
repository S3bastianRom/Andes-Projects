from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

def execute_query(sql_query, params=None):
    return db.session.execute(sql_query, params or {})  # Removed redundant text()