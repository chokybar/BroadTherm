from .broadlink_client import BroadlinkClient
from .command_repository import CommandRepository
from .config import Config
from .state import StateManager


def status():
    config = Config.load()
    state = StateManager().load()
    repository = CommandRepository()

    rm_connected = False
    current_temperature = None

    try:
        client = BroadlinkClient(config.device)
        client.connect()
        rm_connected = True
        current_temperature = client.get_temperature()
    except Exception:
        rm_connected = False

    print("══════════════════════════════════")
    print("        BroadTherm 0.1")
    print("══════════════════════════════════")
    print()

    print("📡 RM Pro")
    print(f"   {'✅ Connecté' if rm_connected else '❌ Hors ligne'}")
    print()

    print("🌡 Température actuelle")
    if current_temperature is not None:
        print(f"   {current_temperature:.1f}°C")
    else:
        print("   Indisponible")
    print()

    print("🎯 Thermostat")
    print(f"   ON  : {config.thermostat.temperature_on}°C")
    print(f"   OFF : {config.thermostat.temperature_off}°C")
    print()

    print("📌 État")
    print(f"   Dernière commande     : {state.last_command}")
    print(f"   Dernière température  : {state.last_temperature}")
    print(f"   Dernière exécution    : {state.last_execution}")
    print()

    print("📚 Commandes connues")
    commands = repository.list()

    if commands:
        for command in commands:
            print(f"   • {command}")
    else:
        print("   Aucune commande")
    print()

    print("══════════════════════════════════")
