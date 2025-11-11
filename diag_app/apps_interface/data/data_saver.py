
import os, yaml

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.data.diag_path import DataDiagLocations
    from diag_app.apps_interface.data.os_info.os_data import get_cpu_load
if MODE == "TESTING":
    from apps_interface.data.diag_path import DataDiagLocations
    from apps_interface.data.os_info.os_data import get_cpu_load

class DataSaver():
    def __init__(self):
        pass

    def save_data_by_data_id(self, app_id:str, data_id:str,New_data:str):

        diag_path = getattr(DataDiagLocations, app_id)

        # Reading data/xx.yaml YAML file
        with open(diag_path, 'r', encoding='utf-8') as file:
            app_diag_yaml = yaml.safe_load(file)
                
        # write new data
        for entry in app_diag_yaml['data']:
            if entry['id'] == data_id:
                entry['data'] = New_data
        
        # Saving to data/xx.yaml YAML file
        with open(diag_path, 'w', encoding='utf-8') as file:
            yaml.dump(app_diag_yaml, file, default_flow_style=False)

        return 0
    
class ComponentDataSaver():
    def __init__(self):
        pass

    def save_data_by_id(self, component_id:str, data_id:str):

        diag_path = getattr(DataDiagLocations, component_id)

        # open file
        with open(diag_path, 'r') as file:
            comp_data = yaml.safe_load(file)
        
        # change to switch case 
        if data_id == 'cpuload':
            val = get_cpu_load()
            New_data = {'load Percentage': val} 

        # change new data
        for entry in comp_data['data']:
            if entry['id'] == data_id:
                entry['data'] = New_data

        # Saving to data YAML file
        with open(diag_path, 'w', encoding='utf-8') as file:
            yaml.dump(comp_data, file, default_flow_style=False)
        
    