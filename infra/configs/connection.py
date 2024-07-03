from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
class DBConnectionHandler:
    
    def __init__(self) -> None:
        load_dotenv()
        db_password = os.getenv("DB_PASSWORD")
        self.__connection_string = f"sqlite:///infra/db/reconhecimento_facial.db?password={db_password}"
        self.__engine = self.__create_database_engine()
        self.session = None
        
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self
    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
