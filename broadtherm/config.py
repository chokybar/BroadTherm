import json
from pathlib import Path

from .models import AppConfig, DeviceConfig, ThermostatConfig


class Config:

    DEFAULT_PATH = Path("data/config.json")

    @staticmethod
    def load(path: str | Path = DEFAULT_PATH) -> AppConfig:

        path = Path(path)

        with path.open("r", encoding="utf-8") as f:
            raw = json.load(f)

        device = DeviceConfig(
            ip=raw["device"]["ip"],
            port=raw["device"]["port"],
            mac=raw["device"]["mac"],
            devtype=raw["device"]["devtype"],
        )

        thermostat = ThermostatConfig(
            temperature_on=raw["thermostat"]["temperature_on"],
            temperature_off=raw["thermostat"]["temperature_off"],
        )

        return AppConfig(
            device=device,
            thermostat=thermostat,
        )
