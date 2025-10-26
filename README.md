# Applications Diagnostic Microservice

## Overview
This is a lightweight Python-based diagnostic microservice designed to interface with applications via a RESTful API. The Microservice used for testing of SOVD (Service-Oriented Vehicle Diagnostics) functionality within the AGL (Automotive Grade Linux) environment. This Microservice is a middle layer between SOVD server and the actual application.

## Purpose
The primary goal of this Microservice is to test SOVD integration using a simplified diagnostics middleware to diagnose apps .

### Key Features:
- Store actual data of an application in a yaml format.
- Acts as a middleware between the SOVD server and the application.
- Routes diagnostic requests from the SOVD server to the application.
- Enables SOVD clients to query available data/faults/configs and more.

## Installation Requirements
To install the necessary dependencies, run:

- ` pip install -r requirements.txt ` 

## Running Diag Hvac app
- ` python diag_app/main.py `

