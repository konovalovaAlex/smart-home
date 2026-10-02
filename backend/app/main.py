from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Device(BaseModel):
    id: int
    name: str
    status: str  # "on" / "off"

devices = {
    1: {"id": 1, "name": "Умный свет", "status": "off"},
    2: {"id": 2, "name": "Термостат", "status": "on"},
}

@app.get("/devices")
def get_devices():
    return devices

@app.post("/devices/{device_id}/toggle")
def toggle_device(device_id: int):
    if device_id not in devices:
        return {"error": "Устройство не найдено"}
    devices[device_id]["status"] = "on" if devices[device_id]["status"] == "off" else "off"
    return {"status": "success", "device": devices[device_id]}