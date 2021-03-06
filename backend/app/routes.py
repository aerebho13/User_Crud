from flask import (
    Flask,
    request
)

from datetime import datetime

from app.database import user
from app.database import vehicle

app = Flask(__name__)
VERSION = "1.0.0"

@app.get("/version")
def get_version():
    out = {
        "server_time": datetime.now().strftime("%F %H:%M:%S"),
        "version": VERSION
    }
    return out

@app.get("/users/")
def get_all_users():
    user_list = user.scan()
    resp = {
        "status": "ok",
        "message": "success",
        "users": user_list
    }
    return resp

@app.get("/users/<int:pk>/")
def get_user_by_id(pk):
    target_user = user.select_by_id(pk)
    resp = {
        "status": "ok",
        "message": "success",
    }
    if target_user:
        resp["user"] = target_user
        return resp
    else:
        resp["status"] = "error"
        resp["message"] = "User not found"
        return resp, 404

@app.post("/users/")
def create_user():
    user_data = request.json
    user.insert(user_data)
    return "", 204

@app.put("/users/<int:pk>/")
def update_user(pk):
    user_data = request.json
    user.update(pk, user_data)
    return "", 204

@app.delete("/users/<int:pk>/")
def deactivate_user(pk):
    user_data = request.json
    user.deactivate(pk, user_data)
    return "", 204

# VEHICLES

@app.get("/vehicles/")
def get_all_vehicles():
    vehicle_list = vehicle.scan()
    resp = {
        "status": "ok",
        "message": "success",
        "vehicles": vehicle_list
    }
    return resp

@app.get("/vehicles/<int:pk>/")
def get_vehicle_by_id(pk):
    target_vehicle = user.select_by_id(pk)
    resp = {
        "status": "ok",
        "message": "success",
    }
    if target_vehicle:
        resp["vehcile"] = target_vehicle
        return resp
    else:
        resp["status"] = "error"
        resp["message"] = "Vehicle not found"
        return resp, 404

@app.post("/vehicles/")
def new_vehicle():
    vehicle_data = request.json
    vehicle.insert(vehicle_data)
    return "", 204

@app.put("/vehicle/<int:pk>/")
def update_vehicle(pk):
    vehicle_data = request.json
    vehicle.update(pk, vehicle_data)
    return "", 204

@app.delete("/vehicle/<int:pk>/")
def deactivate_user(pk):
    vehicle_data = request.json
    vehicle.deactivate(pk, vehicle_data)
    return "", 204

