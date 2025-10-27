from flask import Blueprint, request, jsonify, Response
import os
import requests

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.data.data_provider import DataProvider
if MODE == "TESTING":
    from apps_interface.data.data_provider import DataProvider

routes = Blueprint('routes', __name__)

########
# DATA #
########
data_provider = DataProvider()
# app-id/data
@routes.route("apps/<app_id>/data", methods=['GET'])
def get_datas_from_application(app_id:str):
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""
    app_data = 0
    # Reading data/general_diag YAML file
    app_data = data_provider.get_dids(app_id)
    return app_data

@routes.route("apps/<app_id>/data/<data_id>", methods=['GET'])
def get_data_id_from_application(app_id:str,data_id:str):

    data_entry = data_provider.get_data_by_id(app_id, data_id)

    return data_entry

    app_url = "http://127.0.0.1:6000/" + app_id + "/data/" + data_id
    try:
        # Send request to the local C++ HTTP service e.g hvac
        resp = requests.get("http://127.0.0.1:6000/hvac/data/FrontTemp", timeout=1.0)
        resp.raise_for_status()

        # Return same response and content type to client return Response(resp.text, content_type=resp.headers.get("Content-Type", "application/json"))

    except requests.RequestException as e:
        return jsonify({
            "error": "Failed to reach HVAC service",
            "details": str(e)
        }), 502
    
    
    