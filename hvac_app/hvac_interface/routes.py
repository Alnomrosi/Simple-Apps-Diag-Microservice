from flask import Blueprint, request, jsonify
from data_model.model import Temprature
from hvac_interface.diag_information import DiagLocations, DiagNames
import yaml

routes = Blueprint('routes', __name__)

# app/app-id/data
@routes.route('/hvac/data', methods=['GET'])
def hvac_get_tempratures():
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""

    hvac_diag = 0
    data = {}
    # Reading a YAML file
    with open(DiagLocations.HVAC_GEN_DATA_DIAG_LOC, 'r') as file:
        hvac_diag = yaml.safe_load(file) 
    
    data_diag = hvac_diag["HvacControl"]
    yaml_output = yaml.dump(data_diag, default_flow_style=False)

    return yaml_output