import sys

from broadtherm.config import Config
from broadtherm.broadlink_client import BroadlinkClient
from broadtherm.command_repository import CommandRepository

if len(sys.argv) != 2:
    print("Usage : python -m tests.test_learn_command <nom_commande>")
    sys.exit(1)

name = sys.argv[1]

config = Config.load()

client = BroadlinkClient(config.device)
client.connect()

repo = CommandRepository()

print(f"Apprentissage commande : {name}")
print("Appuie sur la télécommande maintenant...")

raw = client.learn()
repo.save(name, raw)

command = repo.load(name)

print(f"Commande sauvegardée : {command.name}")
print(f"Taille : {command.size}")
print(f"SHA1 : {command.sha1}")
