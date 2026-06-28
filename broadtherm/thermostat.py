from .models import AppConfig, AppState, Decision


class Thermostat:

    TEMPERATURE_MARGIN = 0.2

    def __init__(self, config: AppConfig):
        self.config = config

    def decide(self, temperature: float, state: AppState) -> Decision:
        last_command = state.last_command
        last_temperature = state.last_temperature

        if temperature >= self.config.thermostat.temperature_on:
            if last_command != "cool24":
                return Decision(
                    command="cool24",
                    reason="temperature_above_on_threshold"
                )

            if last_temperature is not None:
                if temperature >= last_temperature - self.TEMPERATURE_MARGIN:
                    return Decision(
                        command="cool24",
                        reason="temperature_not_decreasing_resync"
                    )

            return Decision(
                command=None,
                reason="cooling_already_active_temperature_decreasing"
            )

        if temperature <= self.config.thermostat.temperature_off:
            if last_command != "off":
                return Decision(
                    command="off",
                    reason="temperature_below_off_threshold"
                )

            if last_temperature is not None:
                if temperature <= last_temperature - self.TEMPERATURE_MARGIN:
                    return Decision(
                        command="off",
                        reason="temperature_still_decreasing_resync"
                    )

            return Decision(
                command=None,
                reason="already_off_temperature_stable"
            )

        return Decision(
            command=None,
            reason="temperature_within_comfort_range"
        )
