def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,  # > 60 → high precipitation
        'humidity': 26,
        'windSpeedKMPH': 52   # > 50 → stormy (but may override logic)
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather

# -------------------------
# Strengthened test cases
# -------------------------

def testRainy():
    weather = report(sensorStub)
    print(f"Weather from testRainy: {weather}")
    # Stronger test: ensure "rain" is mentioned
    assert("rain" in weather.lower()), f"Expected 'rain' in weather report, got: {weather}"

def testHighPrecipitation():
    # Use a stub that gives high precipitation and low wind — should still NOT say "Sunny"
    def highPrecipStub():
        return {
            'temperatureInC': 40,
            'precipitation': 80,  # High
            'humidity': 50,
            'windSpeedKMPH': 30   # Low wind
        }

    weather = report(highPrecipStub)
    print(f"Weather from testHighPrecipitation: {weather}")
    
    # Fails because logic doesn't handle this → still returns "Sunny Day"
    assert(weather != "Sunny Day"), f"Expected non-sunny report for high precipitation, got: {weather}"

if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)")
