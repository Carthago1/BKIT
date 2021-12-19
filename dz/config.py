from enum import Enum

token = '5096756347:AAEyvUCnXOxvB7E6mTUYAIz3pFVIxIei_XQ'

appid = "787682f6a13f2e2fbae3243051e8946a"

db_file = "db.vdb"
CURRENT_STATE = "CURRENT_STATE"

class States(Enum):
    START_STATE = 0
    LOCATION_STATE = 1
    DAY_STATE = 2
    DETAIL_STATE = 3
    END_STATE = 4