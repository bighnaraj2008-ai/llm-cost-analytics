# Troubleshooting Guide

Common issues and remediation procedures:

## 1. `sqlite3.OperationalError: database is locked`
- **Cause**: Concurrent writers accessing SQLite in standard rollback journal mode.
- **Fix**: The engine automatically enables Write-Ahead Logging (`PRAGMA journal_mode = WAL;`) and sets a 30-second busy timeout. Ensure long transactions call `commit()` promptly.

## 2. `sqlite3.IntegrityError: FOREIGN KEY constraint failed`
- **Cause**: An API request was logged with an unregistered `model_id`.
- **Fix**: Register the target model in `model_pricing` before logging telemetry.

## 3. Discrepancy in UTC Timestamps
- Ensure all dates are stored as ISO-8601 strings (`YYYY-MM-DD HH:MM:SS`) in UTC.
