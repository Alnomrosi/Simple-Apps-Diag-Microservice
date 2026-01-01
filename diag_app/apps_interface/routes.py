from flask import Blueprint, request, jsonify, Response
import os
import requests

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.data.data_provider import DataProvider,ComponentsDataProvider, APPs_ADDR
    from diag_app.apps_interface.data.data_saver import DataSaver, ComponentDataSaver
if MODE == "TESTING":
    from apps_interface.data.data_provider import DataProvider, ComponentsDataProvider, APPs_ADDR
    from apps_interface.data.data_saver import DataSaver, ComponentDataSaver

routes = Blueprint('routes', __name__)

data_provider = DataProvider()
component_provider = ComponentsDataProvider()
ComponentDataSaver = ComponentDataSaver()
data_saver = DataSaver()
########
# DATA #
########
# app-id/data
@routes.route("/apps/<app_id>/data", methods=['GET'])
def get_datas_from_application(app_id:str):
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""
    app_data = 0
    # Reading apps data YAML file
    app_data = data_provider.get_dids(app_id)
    return app_data

@routes.route("/apps/<app_id>/data/<data_id>", methods=['GET'])
def get_data_id_from_application(app_id:str,data_id:str):
    """Return data inside Application"""
    app_uri = APPs_ADDR[app_id]
    app_url = app_uri + "apps/" + app_id + "/data/" + data_id
    try:

        # Send PUT request to the local C++ HTTP service e.g hvac
        Data_resp = requests.get(app_url, timeout=1.0)
        Data_resp.raise_for_status()

        # save data to yaml format with data_saver
        data_saver.save_data_by_data_id(app_id,data_id,Data_resp.json())

        # Reading apps data YAML file
        data_entry = data_provider.get_data_by_id(app_id, data_id)

       # Return same response and content type to client return Response(resp.text, content_type=resp.headers.get("Content-Type", "application/json"))
        return data_entry

    except requests.RequestException as e:
        return jsonify({
            "error": "Failed to reach Application Server",
            "details": str(e)
        }), 502


@routes.route("/apps/<app_id>/data/<data_id>", methods=['PUT'])
def put_data_id_to_application(app_id:str,data_id:str):
    """Update data inside Application"""
    # get the server uri
    app_uri = APPs_ADDR[app_id]
    app_url = app_uri + "apps/" + app_id + "/data/" + data_id
    
    try:
        # Get new data from request body
        new_data = request.get_json(force=True, silent=False)
        
        # Send PUT request to the local C++ HTTP service e.g hvac
        Data_resp = requests.put(app_url, json=new_data, timeout=1.0)
        Data_resp.raise_for_status()

        # save data to yaml format with data_saver
        data_saver.save_data_by_data_id(app_id,data_id,new_data)

        return jsonify({
            "HTTP/1.1 204 No Content"
        }), 204

    except requests.RequestException as e:
        return jsonify({
            "error": "Failed to reach Application Server",
            "details": str(e)
        }), 502
    
# component-id/data
@routes.route("/components/<component_id>/data", methods=['GET'])
def get_datas_from_component(component_id:str):
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""
    # Reading components data YAML file
    comp_data = data_provider.get_dids(component_id)

    return comp_data

# component-id/data/data-id
@routes.route("/components/<component_id>/data/<data_id>", methods=['GET'])
def get_data_id_from_component(component_id:str, data_id:str):
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""
    # save all comps values
    ComponentDataSaver.save_data_by_id(component_id, data_id)
    # Reading components data YAML file
    comp_data = data_provider.get_data_by_id(component_id, data_id)

    return comp_data

##########
# Faults #
##########
@routes.route("/apps/<app_id>/faults", methods=['GET'])
def get_faults_of_application(app_id:str):
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""
    app_faults = 0
    # Reading data/general_diag YAML file
    app_faults = data_provider.get_faults(app_id)
    return app_faults

@routes.route("/apps/<app_id>/faults/<fault_id>", methods=['GET'])
def get_Singe_fault_of_application(app_id:str, fault_id:str):
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""
    app_faults = 0
    # Reading data/general_diag YAML file
    app_faults = data_provider.get_singlefaults(app_id,fault_id)
    return app_faults

@routes.route("/apps/<app_id>/faults", methods=['DELETE'])
def delete_faults_of_application(app_id:str):
    """Return information about the available data to be diagnostic inside HVAC CONTROL Application"""
    try:
        # delete faults
        del_faults_resp = data_provider.delete_faults(app_id)
        
        return Response(status=204)
    
    except requests.RequestException as e:
        return jsonify({
            "error": "Failed to reach Application Server",
            "details": str(e)
        }), 502