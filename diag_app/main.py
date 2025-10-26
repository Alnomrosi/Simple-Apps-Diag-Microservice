#!/usr/bin/env python3
import os
import sys
from flask import Flask

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

# Add the package directory to Python path
sys.path.insert(0, '/usr/lib/python3.9/site-packages')

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.routes import routes
if MODE == "TESTING":
    from apps_interface.routes import routes


# Init app
app = Flask(__name__)

# Register routes
app.register_blueprint(routes)

# Run Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)