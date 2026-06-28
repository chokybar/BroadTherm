from .models import AppConfig, AppState


class Thermostat:

    def __init__(self, config: AppConfig):
        self.config = config

    def decide(self, temperature: float, state: AppState) -> str | None:
        last_command = state.last_command

        if temperature >= self.config.thermostat.temperature_on:
            if last_command != "cool24":
                return "cool24"

        if temperature <= self.config.thermostat.temperature_off:
            if last_command != "off":
                return "off"

        return None
