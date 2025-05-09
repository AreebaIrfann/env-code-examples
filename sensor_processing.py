# --- Task 1: Average Calculator ---
def calculate_average(data):
    return sum(data) / len(data)

# Given list
sensor_data = [72, 55, 101, 90]
average = calculate_average(sensor_data)
print("Average PM2.5 value:", average)

# --- Task 2: Stations List & Display ---
stations = [
    ["A1", 62],
    ["B2", 110],
    ["C3", 45],
    ["D4", 97]
]

# Printing each station on its own line
for station in stations:
    print(f"{station[0]} → {station[1]}")

# --- Task 3: Status Reporter ---
def report_status(stations_list, threshold):
    for station in stations_list:
        name, pm25 = station
        if pm25 > threshold:
            status = "⚠️ Alert: High pollution"
        else:
            status = "✅ Safe"
        print(f"{name}: {pm25} μg/m³ — {status}")

# Calling the function with a threshold of 100
report_status(stations, 100)

