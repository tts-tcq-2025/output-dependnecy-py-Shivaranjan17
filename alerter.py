alert_failure_count = 0

# Modified stub to simulate failure above a certain celcius threshold
def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 500 if celcius exceeds 200, simulating a failure
    if celcius > 200:
        return 500
    return 200

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 0  # BUG still exists

# -----------------------------
# Test: strengthen to catch bug
# -----------------------------
def test_alert_failure_count():
    global alert_failure_count
    alert_failure_count = 0  # Reset count before test

    alert_in_celcius(400.5)  # High temp → should cause alert failure
    alert_in_celcius(303.6)  # Normal temp → no failure

    # Strengthened assertion to expose the bug
    assert alert_failure_count == 1, f"Expected 1 failure, but got {alert_failure_count}"

# Call the test
test_alert_failure_count()

# Final print statements
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')


