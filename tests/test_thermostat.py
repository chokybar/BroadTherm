from broadtherm.config import Config
from broadtherm.models import AppState
from broadtherm.thermostat import Thermostat

config = Config.load()
thermostat = Thermostat(config)

tests = [
    (28.0, None),
    (28.0, "cool24"),
    (25.0, "cool24"),
    (23.5, "cool24"),
    (23.5, "off"),
]

for temperature, last_command in tests:
    state = AppState(
        last_command=last_command,
        last_temperature=None,
        last_execution=None
    )

    decision = thermostat.decide(temperature, state)

    print(
        f"Temp={temperature}°C | last={last_command} -> decision={decision}"
    )
