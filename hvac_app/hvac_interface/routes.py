from flask import Blueprint, request, jsonify, Response
import os
import requests

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

@routes.route("/<app_id>/data/<data_id>", methods=['GET'])
def set_data_id_from_application(app_id:str,data_id:str):
    try:
        # Send request to your local C++ HTTP service
        resp = requests.get("http://127.0.0.1:6000/hvac/FrontLeftTemp", timeout=1.0)
        resp.raise_for_status()

        # Return same response and content type to client
        return Response(resp.text, content_type=resp.headers.get("Content-Type", "application/json"))

    except requests.RequestException as e:
        return jsonify({
            "error": "Failed to reach HVAC service",
            "details": str(e)
        }), 502
    