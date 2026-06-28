import json
from datetime import datetime
from pathlib import Path

from .models import AppState


class StateManager:

    FILE = Path("data/state.json")

    def __init__(self):
        if not self.FILE.exists():
            self._create()

    def _create(self):
        self.FILE.parent.mkdir(exist_ok=True)

        self.FILE.write_text(
            json.dumps(
                {
                    "last_command": None,
                    "last_temperature": None,
                    "last_execution": None
                },
                indent=4
            ),
            encoding="utf-8"
        )

    def load(self) -> AppState:
        raw = json.loads(self.FILE.read_text(encoding="utf-8"))

        last_execution = raw.get("last_execution")

        return AppState(
            last_command=raw.get("last_command"),
            last_temperature=raw.get("last_temperature"),
            last_execution=datetime.fromisoformat(last_execution) if last_execution else None
        )

    def save(self, state: AppState):
        self.FILE.write_text(
            json.dumps(
                {
                    "last_command": state.last_command,
                    "last_temperature": state.last_temperature,
                    "last_execution": state.last_execution.isoformat() if state.last_execution else None
                },
                indent=4
            ),
            encoding="utf-8"
        )
