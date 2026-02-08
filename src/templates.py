import json

def export_as_json(case_name, metrics):
    """Creates a machine-readable BMS requirement snippet."""
    requirement = {
        "requirement_id": f"BMS-REQ-{case_name.upper()}",
        "operational_limits": {
            "target_soc_operating_window": metrics["soc_window"],
            "max_discharge_c_rate": metrics["c_rate"],
            "balancing_strategy": "Active" if metrics["c_rate"] > 0.5 else "Passive"
        },
        "sensing_accuracy": {
            "voltage_precision": "±5mV",
            "current_precision": "±10mA"
        }
    }
    return json.dumps(requirement, indent=4)