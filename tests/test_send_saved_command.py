from broadtherm.config import Config
from broadtherm.broadlink_client import BroadlinkClient
from broadtherm.command_repository import CommandRepository

config = Config.load()

client = BroadlinkClient(config.device)
client.connect()

repo = CommandRepository()

command = repo.load("off")

print(f"Commande chargée : {command.name}")
print(f"Taille : {command.size}")
print(f"SHA1 : {command.sha1}")

client.send(command.data)

print("Commande OFF envoyée.")
