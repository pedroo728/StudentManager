from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .interface_db_handler import IDbHandler
from src.infra.adapters.db_config.db_config import DbConfig

from typing import List, Optional

class DbHandler(IDbHandler):
    session: Session = None

    def __init__(self, db_config: DbConfig):
        self.db_path: str=f"{db_config.driver}://{db_config.user}:{db_config.password}@{db_config.host}/{db_config.db_name}"
        self.db_timout = db_config.timeout
        self.db_echo = db_config.echo.upper() == "TRUE"

    def get_session(self) -> Session:
        return self.session

    def commit(self):
        self.session.commit()

    def flush(self):
        self.session.flush()

    def close(self) -> None:
        self.session.close()
        self.engine.dispose(close=True)

    def open(self) -> None:
        self.engine = create_engine(self.db_path, echo=self.db_echo)
        self.session_maker = sessionmaker()
        self.session = self.session_maker(bind=self.engine)