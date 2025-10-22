from flask import Blueprint, request, jsonify
import yaml
import os

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from hvac_app.hvac_interface.diag_path import DiagLocations, DiagNames
if MODE == "TESTING":
    from hvac_interface.diag_path import DiagLocations, DiagNames


routes = Blueprint('routes', __name__)

########
# DATA #
########
# app-id/data
@routes.route('/hvac/data', methods=['GET'])
def hvac_get_tempratures():
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""
    hvac_diag = 0
    # Reading data/general_diag YAML file
    with open(DiagLocations.HVAC_GEN_DATA_DIAG_LOC, 'r') as file:
        hvac_diag = yaml.safe_load(file)
    
    data_diag = hvac_diag[DiagNames.APP_NAME]
    return data_diag