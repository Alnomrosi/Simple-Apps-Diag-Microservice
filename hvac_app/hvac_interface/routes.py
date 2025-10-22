from flask import Blueprint, request, jsonify
import yaml
import os

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from hvac_app.data_model.model import Temprature
    from hvac_app.hvac_interface.diag_information import DiagLocations, DiagNames
if MODE == "TESTING":
    from data_model.model import Temprature
    from hvac_interface.diag_information import DiagLocations, DiagNames


routes = Blueprint('routes', __name__)

# app/data
@routes.route('/hvac/data', methods=['GET'])
def hvac_get_tempratures():
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""

    hvac_diag = 0
    # Reading a YAML file
    with open(DiagLocations.HVAC_GEN_DATA_DIAG_LOC, 'r') as file:
        hvac_diag = yaml.safe_load(file)
    
    data_diag = hvac_diag[DiagNames.APP_NAME]

    return data_diag