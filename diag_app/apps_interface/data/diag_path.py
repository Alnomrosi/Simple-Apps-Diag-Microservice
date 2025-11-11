import os
MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

class AppNames():
    hvac = "HvacControl"

class DataDiagLocations():
    if MODE == "DEPLOYMENT": 
        # Apps
        hvac = "var/diagnostics/data_model/apps/hvac_diag/data.yaml"

        # Components
        agl = "var/diagnostics/data_model/components/agl_diag/data.yaml"
    elif MODE == "TESTING":
        # Apps
        hvac = "diag_app/data_model/apps/hvac_diag/data.yaml"

        # Components
        agl = "diag_app/data_model/components/agl_diag/data.yaml"


class FaultsDiagLocations():
    if MODE == "DEPLOYMENT":
        # Apps
        hvac = "var/diagnostics/data_model/apps/hvac_diag/faults.yaml"
    elif MODE == "TESTING":
        hvac = "diag_app/data_model/apps/hvac_diag/faults.yaml"