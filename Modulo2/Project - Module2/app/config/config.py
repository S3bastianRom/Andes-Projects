from dotenv import load_dotenv
import os

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
class SK():    
    SECRET_KEY = f"{os.getenv('SECRET_KEY')}"