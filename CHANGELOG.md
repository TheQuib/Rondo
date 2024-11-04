# Changelog

## [2.1.0] - 2024-11-4
### Fixed
 - GPIO not cleaning up after container shutdown

## [2.0.1] - 2024-11-4
### Fixed
 - `config.yml.j2` now includes new variables with default values

## [2.0.0] - 2024-10-31
### Added
 - Ability to add a status LED light
 - Ability to change LED pin
 - Ability to change button pin
### Updated
 - README.md now separates *required* and *optional* variables


## [1.1.1] - 2024-09-12
### Remove
 - Upgrade in first step of deploy playbook

## [1.1.0] - 2024-09-09
### Fixed
 - Updating config.yml not updating environment variables. Added `--force-restart` to container start check.

## [1.0.2] - 2024-09-08
### Fixed
 - Version controls - again - hopefully.

## [1.0.1] - 2024-09-08
### Fixed
- Version controls.

## [1.0.0] - 2024-09-08
### Added
- Initial release.
