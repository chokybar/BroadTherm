from .broadlink_client import BroadlinkClient
from .command_repository import CommandRepository
from .config import Config


def send(name: str):
    config = Config.load()

    client = BroadlinkClient(config.device)
    client.connect()

    repository = CommandRepository()
    command = repository.load(name)

    print(f"🚀 Envoi : {command.name}")

    client.send(command.data)

    print("✅ Commande envoyée.")
