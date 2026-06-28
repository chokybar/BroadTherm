from datetime import datetime

from .broadlink_client import BroadlinkClient
from .command_repository import CommandRepository
from .config import Config
from .logger import get_logger
from .state import StateManager
from .thermostat import Thermostat


def run(quiet: bool = False):

    logger = get_logger()

    config = Config.load()

    client = BroadlinkClient(config.device)
    client.connect()

    repository = CommandRepository()
    state_manager = StateManager()
    thermostat = Thermostat(config)

    temperature = client.get_temperature()
    state = state_manager.load()

    previous_temperature = state.last_temperature
    previous_command = state.last_command

    decision = thermostat.decide(temperature, state)

    ir_sent = False

    if decision.command is not None:
        command = repository.load(decision.command)
        client.send(command.data)

        ir_sent = True
        state.last_command = decision.command

    state.last_temperature = temperature
    state.last_execution = datetime.now()

    state_manager.save(state)

    if quiet:
        print(f"{temperature:.1f}°C | {decision.command or 'none'} | {decision.reason}")
        return

    logger.execution(
        current_temperature=temperature,
        previous_temperature=previous_temperature,
        previous_command=previous_command,
        decision_command=decision.command,
        decision_reason=decision.reason,
        ir_sent=ir_sent,
    )
