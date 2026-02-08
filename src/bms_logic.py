import numpy as np

def derive_bms_requirements(period_min, eclipse_min, avg_power_w, nominal_voltage_v, mission_life_yrs):
    """
    Translates orbital/load profiles into quantitative BMS operating limits.
    """
    # 1. Energy needed during eclipse
    usable_capacity_wh = avg_power_w * (eclipse_min / 60)
    
    # 2. Discharge Current
    discharge_current_a = avg_power_w / nominal_voltage_v
    
    # 3. Mission-specific Logic (The "Formalization" part)
    # Long missions need restricted SOC windows to preserve SOH
    if mission_life_yrs > 3:
        soc_window = "40% - 70%"
        dod_factor = 0.30
        priority = "Longevity/SOH preservation"
    else:
        soc_window = "20% - 80%"
        dod_factor = 0.60
        priority = "Mass Efficiency/Performance"

    # 4. Total Installed Capacity needed to stay in SOC window
    total_capacity_wh = usable_capacity_wh / dod_factor
    total_capacity_ah = total_capacity_wh / nominal_voltage_v
    
    # 5. C-Rate Calculation
    c_rate = discharge_current_a / total_capacity_ah

    return {
        "usable_wh": round(usable_capacity_wh, 2),
        "total_ah": round(total_capacity_ah, 2),
        "c_rate": round(c_rate, 3),
        "soc_window": soc_window,
        "priority": priority
    }