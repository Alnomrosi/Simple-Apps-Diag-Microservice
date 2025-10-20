#!/usr/bin/env python3
import os
import sys
from flask import Flask

# Ensure Python can find your hvac_interface package
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hvac_interface.routes import routes

# Init app
app = Flask(__name__)

# Register routes
app.register_blueprint(routes)

# Run Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)