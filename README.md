# HVAC Diagnostic Application

## Overview
This is a lightweight Python-based diagnostic microservice designed to interface with HVAC control systems via a RESTful API. The application used for testing of SOVD (Service-Oriented Vehicle Diagnostics) functionality within the AGL (Automotive Grade Linux) environment. This Microservice is a middle layer between SOVD server and actual application.

## Purpose
The primary goal of this application is to test SOVD integration using a simplified diagnostics middleware to diagnose HVAC control app.

### Key Features:
- Store temperature control for front and rear HVAC fans.
- Acts as a middleware between the SOVD server and the HVAC control application.
- Enables SOVD clients to query available temperature values for front and rear fans.
- Routes diagnostic requests from the SOVD server to the HVAC application.

## Installation Requirements
To install the necessary dependencies, run:

- ` pip install -r requirements.txt ` 

## Running Diag Hvac app
- ` python hvac_app/main.py `

