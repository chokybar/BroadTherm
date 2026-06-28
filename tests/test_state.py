from datetime import datetime

from broadtherm.models import AppState
from broadtherm.state import StateManager

manager = StateManager()

state = manager.load()
print("Avant :", state)

state.last_command = "off"
state.last_temperature = 25.4
state.last_execution = datetime.now()

manager.save(state)

state = manager.load()
print("Après :", state)
