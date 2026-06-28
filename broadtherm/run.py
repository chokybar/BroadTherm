from datetime import datetime

from .broadlink_client import BroadlinkClient
from .command_repository import CommandRepository
from .config import Config
from .state import StateManager
from .thermostat import Thermostat


def run(quiet: bool = False):

    config = Config.load()

    client = BroadlinkClient(config.device)
    client.connect()

    repository = CommandRepository()
    state_manager = StateManager()
    thermostat = Thermostat(config)

    temperature = client.get_temperature()
    state = state_manager.load()

    decision = thermostat.decide(temperature, state)

    if not quiet:

        print(f"🌡 Température : {temperature:.1f}°C")
        print(f"📌 Dernière commande : {state.last_command}")
        print(f"🌡 Température précédente : {state.last_temperature}")
        print(f"🧠 Raison : {decision.reason}")

    if decision is None:

        if not quiet:
            print("✅ Aucune action nécessaire.")

    else:

        if not quiet:
            print(f"🚀 Envoi de : {decision.command}")

        command = repository.load(decision.command)

        client.send(command.data)

        state.last_command = decision.command

    state.last_temperature = temperature
    state.last_execution = datetime.now()

    state_manager.save(state)

    if quiet:
        print(f"{temperature:.1f}|{decision or 'none'}")
    else:
        print("💾 Etat sauvegardé.")
