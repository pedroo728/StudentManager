from typing import Any

from src.infra.adapters.database.db_handler import DbHandler
from src.infra.adapters.db_config.db_config import DbConfig


TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InVzZXJfaWQiOjAsImVtYWlsIjoic2VyZ2lvLndlbGxpbmd0b24xQHRyYW5zZmVyby5jb20ifSwiZXhwIjoxNjgxNDAzOTY4fQ.mmnbpZXl88yLn4RtnxEC-m1_gQRh6_i4x2OjYHBud4I'
URL = 'http://127.0.0.1:5000'


def get_header() -> dict:
    #return { 'Authorization': f'Bearer {TOKEN}'}
    return {}

def get_url() -> str:
    return URL

def get_db() -> Any:
    db_config = DbConfig()
    db = DbHandler(db_config)
    db.open()

    return db
