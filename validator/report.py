import json
from datetime import datetime

def generate_report(device_name, issues):
    """
    Generate a validation report for a device
    """
    return {
        "device": device_name,
        "timestamp": datetime.utcnow().isoformat(),
        "issues_found": len(issues),
        "issues": issues
    }

def save_report(report, filename):
    """
    Save report to a JSON file
    """
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)

