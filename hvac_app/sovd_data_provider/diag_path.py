import os
MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

class AppNames():
    hvac = "HvacControl"

class DataDiagLocations():
    if MODE == "DEPLOYMENT": 
        hvac = "lib/python3/site-packages/hvac_app/data_model/hvac_diag/data/general_diag.yaml"
    elif MODE == "TESTING":
        hvac = "hvac_app/data_model/hvac_diag/data/datas.yaml"