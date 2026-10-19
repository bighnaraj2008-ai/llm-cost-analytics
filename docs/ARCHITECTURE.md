# System Architecture & Design Documentation

## Overview
LLM Cost Analytics is an enterprise-grade analytics engine and relational schema tailored for tracking LLM token consumption, calculating tiered pricing models, detecting sudden cost spikes, and generating aggregated utilization telemetry.

## Component Breakdown
1. **Migrations Engine (`migrations/`)**: Sequential declarative SQL migration scripts establishing relational schemas and initial seed datasets.
2. **Analytical Workloads (`queries/`)**: Optimized SQL analytical aggregation queries utilizing indexes and window functions.
3. **Core Services (`src/services/`)**:
   - `CostCalculator`: Pure mathematical token pricing engine supporting rate multipliers and tier matching.
   - `AnalyticsService`: Query orchestrator returning structured telemetry objects.
4. **Data Access Layer (`src/database.py`)**: SQLite connection manager configured with write-ahead logging (WAL) and strict foreign key pragmas.
5. **CLI Interface (`src/cli.py`)**: Command line runner providing commands for migrations, seeding, report generation, and CSV export.
