# ❄️ BroadTherm

> Turn your old infrared air conditioner into a smart thermostat using a BroadLink RM Pro.

BroadTherm is a lightweight Python application that transforms any infrared air conditioner into a temperature-controlled system.

No cloud.

No Home Assistant.

No additional hardware.

Only a BroadLink RM Pro (or compatible device).

---

## Features

- 🌡 Read room temperature from the RM Pro sensor
- 📡 Learn IR commands directly from your remote
- 📚 Store commands in JSON
- ❄️ Automatic thermostat mode
- 💾 Persistent state
- 📱 Works on Linux, Windows, macOS and Pyto (iPhone)
- ☁️ 100% local

---

## Requirements

- Python 3.10+
- BroadLink RM Pro / RM4
- Infrared air conditioner

---

## Installation

```bash
git clone https://github.com/chokybar/BroadTherm.git

cd BroadTherm

pip install .
```

---

## Configuration

```bash
cp data/config.example.json data/config.json
```

---

## Learn commands

```bash
python -m broadtherm learn off

python -m broadtherm learn cool24
```

---

## Check status

```bash
python -m broadtherm status
```

---

## Run thermostat

```bash
python -m broadtherm run
```

Designed to be executed periodically using:

- cron
- Windows Task Scheduler
- iPhone Shortcuts
- Home Assistant
- etc.

---

## Project status

Current version:

**v0.1.0**

Working features:

- ✅ Read temperature
- ✅ Learn commands
- ✅ Send commands
- ✅ Thermostat
- ✅ CLI
- ✅ JSON storage

---

## License

MIT
