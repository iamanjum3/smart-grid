device_status = {
    "AC": "ON",
    "Fan": "ON",
    "Heater": "ON"
}

THRESHOLD = 2000
PRICE_PER_UNIT = 5  # ₹ per kWh

def process_data(device_data_list):
    valid_data = []

    for d in device_data_list:
        if isinstance(d, dict) and "power" in d:
            valid_data.append(d)

    total_power = sum(d["power"] for d in valid_data)

    # Convert W → kW
    total_power_kw = total_power / 1000

    # Assume usage for 1 hour (simplified)
    energy_consumed = total_power_kw * 1  # kWh

    # Cost calculation
    cost = energy_consumed * PRICE_PER_UNIT

    # Reset device status
    for d in device_status:
        device_status[d] = "ON"

    # Smart control
    if total_power > THRESHOLD:
        device_status["Heater"] = "OFF"

    return total_power, energy_consumed, cost, device_status