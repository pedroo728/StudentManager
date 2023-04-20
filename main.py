from dotenv import load_dotenv
from src.webapp.web_app import WebApp

if __name__ == '__main__':
    load_dotenv()
    WebApp.execute()
