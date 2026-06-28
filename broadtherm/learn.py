from .broadlink_client import BroadlinkClient
from .command_repository import CommandRepository
from .config import Config


def learn(name: str):
    config = Config.load()

    client = BroadlinkClient(config.device)
    client.connect()

    repository = CommandRepository()

    print(f"📡 Apprentissage : {name}")
    print("Appuie sur la télécommande...")

    raw = client.learn()
    repository.save(name, raw)

    command = repository.load(name)

    print(f"✅ Commande sauvegardée : {command.name}")
    print(f"📦 Taille : {command.size}")
    print(f"🔐 SHA1 : {command.sha1}")
