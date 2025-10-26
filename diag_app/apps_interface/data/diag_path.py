import os
MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

class AppNames():
    hvac = "HvacControl"

class DataDiagLocations():
    if MODE == "DEPLOYMENT": 
        hvac = "lib/python3/site-packages/diag_app/data_model/hvac_diag/data/datas.yaml"
    elif MODE == "TESTING":
        hvac = "diag_app/data_model/hvac_diag/data/datas.yaml"