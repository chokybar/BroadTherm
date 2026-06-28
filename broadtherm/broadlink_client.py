from __future__ import annotations

import broadlink

from .models import DeviceConfig


class BroadlinkClient:

    def __init__(self, config: DeviceConfig):

        self.config = config
        self.device = None

    def connect(self):

        self.device = broadlink.gendevice(
            int(self.config.devtype, 16),
            (self.config.ip, self.config.port),
            bytes.fromhex(self.config.mac)
        )

        self.device.auth()

    def get_temperature(self) -> float:

        return self.device.check_temperature()

    def learn(self) -> bytes:

        self.device.enter_learning()

        while True:

            try:
                data = self.device.check_data()

                if data:
                    return data

            except Exception:
                pass

    def send(self, data: bytes):

        self.device.send_data(data)
