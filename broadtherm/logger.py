from pathlib import Path
import logging


LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "broadtherm.log"


class BroadThermLogger:

    def __init__(self):
        LOG_DIR.mkdir(exist_ok=True)

        self.logger = logging.getLogger("broadtherm")

        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            formatter = logging.Formatter("%(asctime)s | %(message)s")

            file_handler = logging.FileHandler(LOG_FILE)
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    def execution(
        self,
        current_temperature: float,
        previous_temperature: float | None,
        previous_command: str | None,
        decision_command: str | None,
        decision_reason: str,
        ir_sent: bool,
    ):
        self.logger.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        self.logger.info("🌡 Température actuelle   : %.1f°C", current_temperature)
        self.logger.info("🌡 Température précédente : %s", previous_temperature)
        self.logger.info("📌 Commande précédente    : %s", previous_command)
        self.logger.info("🧠 Décision               : %s", decision_command or "none")
        self.logger.info("🧠 Raison                 : %s", decision_reason)
        self.logger.info("🚀 IR envoyé              : %s", "oui" if ir_sent else "non")
        self.logger.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


def get_logger() -> BroadThermLogger:
    return BroadThermLogger()
