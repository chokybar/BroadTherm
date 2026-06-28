import sys

from .run import run
from .learn import learn
from .send import send
from .status import status
from .delete import delete

def main():
    if len(sys.argv) < 2:
        print("Usage : python -m broadtherm [run|learn|send|status] [commande]")
        return

    action = sys.argv[1]

    if action == "run":
        run()
    elif action == "learn":
        if len(sys.argv) != 3:
            print("Usage : python -m broadtherm learn <nom_commande>")
            return
        learn(sys.argv[2])
    elif action == "send":
        if len(sys.argv) != 3:
            print("Usage : python -m broadtherm send <nom_commande>")
            return
        send(sys.argv[2])
    elif action == "status":
        status()
    elif action == "delete":
        if len(sys.argv) != 3:
            print("Usage : python -m broadtherm delete <nom_commande>")
            return
        delete(sys.argv[2])
    else:
        print(f"Commande inconnue : {action}")


if __name__ == "__main__":
    main()
