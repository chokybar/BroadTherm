from dataclasses import dataclass
from datetime import datetime

@dataclass
class IRCommand:
    name: str
    data: bytes
    sha1: str
    size: int
    created: datetime

@dataclass
class DeviceConfig:
    ip: str
    port: int
    mac: str
    devtype: str

@dataclass
class ThermostatConfig:
    temperature_on: float
    temperature_off: float

@dataclass
class AppConfig:
    device: DeviceConfig
    thermostat: ThermostatConfig

@dataclass
class AppState:
    last_command: str | None
    last_temperature: float | None
    last_execution: datetime | None

@dataclass
class Decision:
    command: str | None
    reason: str
