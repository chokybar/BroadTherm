from datetime import datetime

from .broadlink_client import BroadlinkClient
from .command_repository import CommandRepository
from .config import Config
from .state import StateManager
from .thermostat import Thermostat


def run():

    config = Config.load()

    client = BroadlinkClient(config.device)
    client.connect()

    repository = CommandRepository()
    state_manager = StateManager()
    thermostat = Thermostat(config)

    temperature = client.get_temperature()
    state = state_manager.load()

    print(f"🌡 Température : {temperature:.1f}°C")
    print(f"📌 Dernière commande : {state.last_command}")

    decision = thermostat.decide(temperature, state)

    if decision is None:

        print("✅ Aucune action nécessaire.")

    else:

        print(f"🚀 Envoi de : {decision}")

        command = repository.load(decision)

        client.send(command.data)

        state.last_command = decision

    state.last_temperature = temperature
    state.last_execution = datetime.now()

    state_manager.save(state)

    print("💾 Etat sauvegardé.")
