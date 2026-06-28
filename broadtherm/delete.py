from .command_repository import CommandRepository


def delete(name: str):
    repository = CommandRepository()

    if not repository.exists(name):
        print(f"⚠️ Commande inconnue : {name}")
        return

    repository.delete(name)

    print(f"🗑 Commande supprimée : {name}")
