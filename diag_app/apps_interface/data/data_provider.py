import os
from typing import List
import yaml

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.data.diag_path import DataDiagLocations, AppNames
    from diag_app.apps_interface.data.common.types import ValueMetaData
    from diag_app.apps_interface.data.data.response import Datas, DataValue
if MODE == "TESTING":
    from apps_interface.data.diag_path import DataDiagLocations, AppNames
    from apps_interface.data.common.types import ValueMetaData
    from apps_interface.data.data.response import Datas, DataValue

APPs_ADDR = {"hvac":"http://127.0.0.1:6000/"}

class DataProvider:
    def __init__(self):
        pass
    
    # data
    def get_dids(self, app_id:str):
        datas = []
        diag_path = getattr(DataDiagLocations, app_id)
        
        # Reading data/xx.yaml YAML file
        with open(diag_path, 'r') as file:
            app_diag_yaml = yaml.safe_load(file)
    
        # data_diag = app_diag_yaml[AppNames.hvac]

        for data in app_diag_yaml['data']:
            datas.append(ValueMetaData.model_validate(data))
        
        resp_data = Datas(items=datas)

        return resp_data.model_dump()
    
    def get_data_by_id(self, app_id:str, data_id:str):
        data_value = {}
        diag_path = getattr(DataDiagLocations, app_id)

        with open(diag_path,'r') as file:
            app_data = yaml.safe_load(file)

        # App_Data = app_data[AppNames.hvac]

        for data in app_data['data']:
            if data_id == data.get('id'):
                data_value.update(DataValue.model_validate(data)) 

        return data_value
