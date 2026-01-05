import yaml

def load_devices():
    with open("inventory/devices.yaml") as f:
        data = yaml.safe_load(f)
    return data["devices"]
