import os
from typing import List
import yaml
import psutil
import sys

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.data.diag_path import DataDiagLocations, FaultsDiagLocations
    from diag_app.apps_interface.data.common.types import ValueMetaData
    from diag_app.apps_interface.data.data.response import Datas, DataValue
    from diag_app.apps_interface.data.faults.types import Fault
    from diag_app.apps_interface.data.faults.response import ListOfFaults
if MODE == "TESTING":
    from apps_interface.data.diag_path import DataDiagLocations, FaultsDiagLocations
    from apps_interface.data.common.types import ValueMetaData
    from apps_interface.data.data.response import Datas, DataValue
    from apps_interface.data.faults.types import Fault
    from apps_interface.data.faults.response import ListOfFaults
    from apps_interface.data.os_info.os_data import get_cpu_load

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
    

    # faults

    def get_faults(self, app_id:str):
        faults = []
        diag_path = getattr(FaultsDiagLocations, app_id)
        
        # Reading data/xx.yaml YAML file
        with open(diag_path, 'r') as file:
            app_diag_yaml = yaml.safe_load(file)
    
        # data_diag = app_diag_yaml[AppNames.hvac]

        for faults_details in app_diag_yaml['faults']:
            faults.append(Fault.model_validate(faults_details))
        
        resp_faults = ListOfFaults(items=faults)

        return resp_faults.model_dump()
    
    def get_singlefaults(self, app_id:str, fault_id:id):
        faults = []
        diag_path = getattr(FaultsDiagLocations, app_id)

        # Reading faults/xx.yaml YAML file
        with open(diag_path, 'r') as file:
            app_diag_yaml = yaml.safe_load(file)

        for faults_details in app_diag_yaml['faults']:
            if faults_details.get('code') == fault_id:
                faults.append(Fault.model_validate(faults_details))
        
        resp_faults = ListOfFaults(items=faults)

        return resp_faults.model_dump()
    
    def delete_faults(self, app_id:str):
        diag_path = getattr(FaultsDiagLocations, app_id)
        faults = []

        # Reading faults/xx.yaml YAML file
        with open(diag_path, 'r') as file:
            app_diag_yaml = yaml.safe_load(file)
        
        for faults_details in app_diag_yaml.get('faults', []):
            if faults_details.get('status') and faults_details['status']['aggregatedStatus'] == 'active':
                    faults_details['status']['aggregatedStatus'] = 'inactive'

        with open(diag_path,'w') as file:
            yaml.dump(app_diag_yaml, file)
        
        return True
    

class ComponentsDataProvider:
    def __init__(self):
        pass

    def get_component_datas(self, component_id:str):

        diag_path = getattr(FaultsDiagLocations, component_id)
        comp_data = "Nothing to provide"
        comp_data = get_cpu_load(interval=1)

        
        return str(comp_data)

