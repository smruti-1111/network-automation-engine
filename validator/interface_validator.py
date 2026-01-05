from validator.desired_state import EXPECTED_INTERFACES

def validate_interfaces(actual_state):
    """
    Compare actual interface state with desired state
    """
    issues = []

    for interface, expected in EXPECTED_INTERFACES.items():
        if interface not in actual_state:
            issues.append({
                "interface": interface,
                "issue": "Interface missing"
            })
            continue

        actual = actual_state[interface]

        if actual["admin"] != expected["admin"]:
            issues.append({
                "interface": interface,
                "issue": "Admin state mismatch",
                "expected": expected["admin"],
                "actual": actual["admin"]
            })

        if actual["oper"] != expected["oper"]:
            issues.append({
                "interface": interface,
                "issue": "Operational state mismatch",
                "expected": expected["oper"],
                "actual": actual["oper"]
            })

    return issues

