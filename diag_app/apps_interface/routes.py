from flask import Blueprint, request, jsonify, Response
import os
import requests

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.data.data_provider import DataProvider, APPs_ADDR
    from diag_app.apps_interface.data.data_saver import DataSaver
if MODE == "TESTING":
    from apps_interface.data.data_provider import DataProvider, APPs_ADDR
    from apps_interface.data.data_saver import DataSaver

routes = Blueprint('routes', __name__)

data_provider = DataProvider()
data_saver = DataSaver()
########
# DATA #
########
# app-id/data
@routes.route("/apps/<app_id>/data", methods=['GET'])
def get_datas_from_application(app_id:str):
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""
    app_data = 0
    # Reading data/general_diag YAML file
    app_data = data_provider.get_dids(app_id)
    return app_data

@routes.route("/apps/<app_id>/data/<data_id>", methods=['GET'])
def get_data_id_from_application(app_id:str,data_id:str):
    #
    #  get the server uri
    app_uri = APPs_ADDR[app_id]
    app_url = app_uri + "apps/" + app_id + "/data/" + data_id
    print(app_url)
    try:
        # Send request to the local C++ HTTP service e.g hvac
        Data_resp = requests.get(app_url, timeout=1.0)
        Data_resp.raise_for_status()

        # save data to yaml format with data_saver
        data_saver.save_data_by_data_id(app_id,data_id,Data_resp.json())
        # get_data_by_id with data_provider
        data_entry = data_provider.get_data_by_id(app_id, data_id)

       # Return same response and content type to client return Response(resp.text, content_type=resp.headers.get("Content-Type", "application/json"))
        return data_entry

    except requests.RequestException as e:
        return jsonify({
            "error": "Failed to reach Application Server",
            "details": str(e)
        }), 502
    