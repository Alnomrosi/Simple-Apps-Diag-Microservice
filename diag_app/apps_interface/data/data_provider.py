import os
from typing import List
import yaml

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.data.diag_path import DataDiagLocations, AppNames
    from diag_app.apps_interface.data.common.types import ValueMetaData
    from diag_app.apps_interface.data.data.response import Datas
if MODE == "TESTING":
    from apps_interface.data.diag_path import DataDiagLocations, AppNames
    from apps_interface.data.common.types import ValueMetaData
    from apps_interface.data.data.response import Datas

class DataProvider:
    def __init__(self):
        pass
    
    # data
    def get_dids(self, app_id:str):
        datas = []
        diag_path = getattr(DataDiagLocations, app_id)
        
        # Reading data/general_diag YAML file
        with open(diag_path, 'r') as file:
            app_diag_yaml = yaml.safe_load(file)
    
        data_diag = app_diag_yaml[AppNames.hvac]

        for data in data_diag['data']:
            datas.append(ValueMetaData.model_validate(data))
        
        resp_data = Datas(items=datas)

        return resp_data.model_dump()
