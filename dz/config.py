from enum import Enum

token = "token"

appid = "appid"

db_file = "db.vdb"
CURRENT_STATE = "CURRENT_STATE"

class States(Enum):
    START_STATE = 0
    LOCATION_STATE = 1
    DAY_STATE = 2
    DETAIL_STATE = 3
    END_STATE = 4
