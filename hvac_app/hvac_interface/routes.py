from flask import Blueprint, request, jsonify
import os

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from hvac_app.sovd_data_provider.data_provider import DataProvider
if MODE == "TESTING":
    from sovd_data_provider.data_provider import DataProvider

routes = Blueprint('routes', __name__)

########
# DATA #
########
data_provider = DataProvider()
# app-id/data
@routes.route("/<app_id>/data", methods=['GET'])
def get_datas_from_application(app_id:str):
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""
    app_data = 0
    
    # Reading data/general_diag YAML file
    app_data = data_provider.get_dids(app_id)
    
    return app_data