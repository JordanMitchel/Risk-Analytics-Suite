# 📊 Risk Analytics Suite

<div align="center">

*A production-style portfolio analytics and quantitative risk management platform built with Python, FastAPI, PostgreSQL, QuantLib and React.*

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

---

## Overview

Risk Analytics Suite is a modular portfolio analytics and quantitative risk management platform inspired by systems used by investment banks, hedge funds and asset managers.

The platform is designed to support the complete portfolio workflow:

```text
Portfolio Sources
        ↓
Portfolio Management
        ↓
Market Data
        ↓
Portfolio Analytics
        ↓
Pricing and Risk
        ↓
Stress Testing
        ↓
Interactive Dashboard
```

The project combines production-style software engineering with practical quantitative finance techniques suitable for front-office, quant developer and risk engineering roles.

## Current capabilities

- FastAPI backend
- PostgreSQL persistence
- SQLAlchemy ORM
- Alembic migrations
- Pydantic validation
- Repository and service layers
- Portfolio creation and retrieval
- Duplicate portfolio validation
- Currency normalisation
- Swagger and OpenAPI documentation
- Docker-based local database setup

## Planned capabilities

- CSV portfolio import using Pandas
- Alpaca portfolio synchronisation
- Freetrade activity import
- Historical market data
- Portfolio valuation and P&L
- Exposure and concentration analytics
- Yield curves and fixed-income sensitivities
- Historical, parametric and Monte Carlo VaR
- Expected Shortfall
- Scenario analysis and stress testing
- React and Plotly dashboard

## Technology stack

### Backend

- Python 3.13
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Pandas
- NumPy
- SciPy
- QuantLib
- Pydantic

### Frontend

- React
- TypeScript
- Plotly

### Infrastructure and quality

- Docker
- Docker Compose
- uv
- Pytest
- Ruff
- MyPy
- GitHub Actions

## Project structure

```text
Risk-Analytics-Suite/
├── Backend/
│   ├── app/
│   │   ├── api/
│   │   ├── analytics/
│   │   ├── database/
│   │   ├── integrations/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   ├── alembic/
│   ├── tests/
│   └── alembic.ini
├── Frontend/
├── data/
├── docs/
│   ├── api.md
│   └── architecture.md
├── scripts/
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Quick start

### Prerequisites

- Python 3.13+
- uv
- Docker
- Docker Compose
- Git

### Install dependencies

```bash
uv sync
```

### Configure environment variables

Create `.env` in the repository root:

```env
DATABASE_URL=postgresql+psycopg://risk_user:risk_password@localhost:5432/risk_analytics
ALPACA_API_KEY=
ALPACA_SECRET_KEY=
ALPACA_PAPER=true
FRED_API_KEY=
```

Never commit `.env`.

### Start PostgreSQL

```bash
docker compose up -d
```

### Apply migrations

```bash
uv run alembic -c Backend/alembic.ini upgrade head
```

### Start FastAPI

```bash
uv run uvicorn Backend.app.main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Development commands

```bash
uv run pytest
uv run pytest --cov=Backend.app
uv run ruff check Backend
uv run ruff format Backend
uv run mypy Backend
```

## Current status

| Module | Status |
|---|---|
| Backend foundation | Complete |
| PostgreSQL and migrations | Complete |
| Portfolio management | In progress |
| CSV portfolio import | In progress |
| Alpaca import | Planned |
| Market data | Planned |
| Portfolio analytics | Planned |
| Fixed-income analytics | Planned |
| Risk engine | Planned |
| Dashboard | Planned |

## MVP scope

The first production-style version will support:

- Portfolio and position management
- CSV, Alpaca and Freetrade imports
- Historical prices and market data
- Portfolio valuation and P&L
- Returns, volatility, correlation and covariance
- Exposure and concentration analysis
- Duration, convexity, DV01, PV01 and CS01
- Historical, parametric and Monte Carlo VaR
- Expected Shortfall
- Stress testing
- Interactive dashboards

## Documentation

- [Architecture](docs/architecture.md)
- [API reference](docs/api.md)

## License

This project is licensed under the MIT License.