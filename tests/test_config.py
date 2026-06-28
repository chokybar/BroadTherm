from broadtherm.config import Config

config = Config.load()

print(config)
print(config.device.ip)
print(config.device.port)
print(config.thermostat.temperature_on)
