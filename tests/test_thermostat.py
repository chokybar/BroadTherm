from broadtherm.config import Config
from broadtherm.models import AppState
from broadtherm.thermostat import Thermostat

config = Config.load()
thermostat = Thermostat(config)

tests = [
    # Trop chaud, jamais allumé
    (28.0, None, None),

    # Trop chaud, déjà cool24, mais température stable => resync cool24
    (28.0, "cool24", 28.0),

    # Trop chaud, déjà cool24, température baisse nettement => rien
    (27.5, "cool24", 28.0),

    # Zone neutre
    (25.0, "cool24", 26.0),

    # Trop froid, dernière commande cool24 => off
    (23.5, "cool24", 25.0),

    # Trop froid, déjà off, température continue de baisser => resync off
    (23.0, "off", 23.5),

    # Trop froid, déjà off, température remonte/stable => rien
    (23.5, "off", 23.4),
]

for temperature, last_command, last_temperature in tests:
    state = AppState(
        last_command=last_command,
        last_temperature=last_temperature,
        last_execution=None
    )

    decision = thermostat.decide(temperature, state)

    print(
        f"Temp={temperature}°C | last_cmd={last_command} | "
        f"last_temp={last_temperature} -> "
        f"command={decision.command}, reason={decision.reason}"
    )
