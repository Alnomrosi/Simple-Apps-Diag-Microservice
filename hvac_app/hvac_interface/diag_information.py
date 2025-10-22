import os
MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

class DiagNames():
    APP_NAME = "HvacControl"

class DiagLocations():
    if MODE == "DEPLOYMENT": 
        HVAC_DATA_DIAG_LOC = "lib/python3/site-packages/hvac_app/data_model/hvac_diag/data/data_diag.yaml"
        HVAC_GEN_DATA_DIAG_LOC = "lib/python3/site-packages/hvac_app/data_model/hvac_diag/data/general_diag.yaml"
    elif MODE == "TESTING":
        HVAC_DATA_DIAG_LOC = "hvac_app/data_model/hvac_diag/data/data_diag.yaml"
        HVAC_GEN_DATA_DIAG_LOC = "hvac_app/data_model/hvac_diag/data/general_diag.yaml"