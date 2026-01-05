from netmiko import ConnectHandler

def get_interfaces(device):
    print(f"🔌 Connecting to {device['host']}")
    connection = ConnectHandler(
        device_type="cisco_xr",
        host=device["host"],
        username=device["username"],
        password=device["password"]
    )

    output = connection.send_command("show interfaces brief")
    connection.disconnect()

    interfaces = {}

    for line in output.splitlines():
        if line.startswith(("Gi", "Hu", "Te")):
            parts = line.split()
            if len(parts) >= 3:
                interfaces[parts[0]] = {
                    "admin": "up",
                    "oper": "up" if parts[2].lower() == "up" else "down"
                }

    return interfaces

