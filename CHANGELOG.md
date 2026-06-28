# Changelog

All notable changes to BroadTherm will be documented in this file.

---

## [0.2.0] - Unreleased

### Added

- Decision model (`Decision`) replacing raw string commands.
- Decision reasons for every thermostat action.
- Temperature trend based resynchronization.
- `constants.py` to centralize internal constants.
- Centralized application version.

### Improved

- Thermostat is now able to detect probable desynchronization with the air conditioner.
- `run` now displays the previous temperature and decision reason.
- Better separation between configuration, constants and business logic.

---

## [0.1.0] - 2026-06-28

### Added

- BroadLink RM Pro support.
- Temperature reading.
- IR learning.
- IR command repository.
- JSON configuration.
- JSON state persistence.
- Thermostat logic.
- Command Line Interface.
- Status dashboard.
