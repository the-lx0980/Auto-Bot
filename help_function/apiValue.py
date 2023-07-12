from os import environ

class apiValues(object):
    API_ID = int(environ.get("API_ID"))
    API_HASH = environ.get("API_HASH")
    BOT_TOKEN = environ.get("BOT_TOKEN")
    DB_NAME = environ.get("DB_NAME")
    DB_URL = environ.get("DB_URL")
    
    
                            
