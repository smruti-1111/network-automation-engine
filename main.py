from inventory.loader import load_devices
from collector.interfaces import get_interfaces
from validator.interface_validator import validate_interfaces
from validator.report import generate_report, save_report

def main():
    print("🚀 Starting Network Automation Validator")

    devices = load_devices()
    print(f"📦 Loaded {len(devices)} device(s) from inventory")

    for device in devices:
        print(f"\n🔍 Processing device: {device['name']}")

        print("📡 Collecting interface data...")
        actual_state = get_interfaces(device)

        print(f"📊 Collected {len(actual_state)} interfaces")

        print("🧠 Validating interface state...")
        issues = validate_interfaces(actual_state)

        report = generate_report(device["name"], issues)
        save_report(report, f"reports/{device['name']}_health.json")

        if issues:
            print(f"❌ Issues detected: {len(issues)}")
            for issue in issues:
                print(issue)
        else:
            print("✅ No issues detected. Device is healthy.")

    print("\n🎉 Validation run completed")

if __name__ == "__main__":
    main()

