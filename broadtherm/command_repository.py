import base64
import hashlib
import json

from datetime import datetime
from pathlib import Path

from .models import IRCommand


class CommandRepository:

    FILE = Path("data/commands.json")

    def __init__(self):

        if not self.FILE.exists():
            self._create()

    def _create(self):

        self.FILE.parent.mkdir(exist_ok=True)

        self.FILE.write_text(
            json.dumps(
                {
                    "version": 1,
                    "commands": {}
                },
                indent=4
            ),
            encoding="utf-8"
        )

    def _read(self):

        return json.loads(self.FILE.read_text(encoding="utf-8"))

    def _write(self, data):

        self.FILE.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8"
        )

    def save(self, name: str, raw: bytes):

        db = self._read()

        db["commands"][name] = {

            "created": datetime.now().isoformat(),

            "size": len(raw),

            "sha1": hashlib.sha1(raw).hexdigest(),

            "data": base64.b64encode(raw).decode()

        }

        self._write(db)

    def load(self, name: str) -> IRCommand:

        db = self._read()

        if name not in db["commands"]:
            raise KeyError(name)

        command = db["commands"][name]

        return IRCommand(

            name=name,

            data=base64.b64decode(command["data"]),

            sha1=command["sha1"],

            size=command["size"],

            created=datetime.fromisoformat(command["created"])

        )

    def exists(self, name: str):

        return name in self._read()["commands"]

    def delete(self, name: str):

        db = self._read()

        db["commands"].pop(name, None)

        self._write(db)

    def list(self):

        return sorted(self._read()["commands"].keys())
