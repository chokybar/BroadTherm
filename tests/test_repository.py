from broadtherm.config import Config
from broadtherm.broadlink_client import BroadlinkClient
from broadtherm.command_repository import CommandRepository

config = Config.load()

client = BroadlinkClient(config.device)
client.connect()

repo = CommandRepository()

print("Appuie sur OFF de la télécommande...")

raw = client.learn()

repo.save("off", raw)

print(repo.list())

command = repo.load("off")

print(command)
print(len(command.data))

client.send(command.data)

print("Commande renvoyée.")
