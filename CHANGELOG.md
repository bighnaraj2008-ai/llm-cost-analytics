# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-10-19
### Added
- Relational schema migration scripts for `model_pricing` and `api_requests`.
- SQL analytical workloads: daily cost per user, model utilization breakdown, cost spike detector, and token trend analysis.
- Pure Python mathematical `CostCalculator` supporting rate multipliers.
- `AnalyticsService` report generator.
- SQLite foreign key and WAL mode connection manager.
- Comprehensive unit and integration test suites.
- CLI supporting migrations, seeding, report formatting, and CSV exports.
