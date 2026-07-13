# Database Design

## Overview

The Risk Analytics Suite uses PostgreSQL with SQLAlchemy ORM and Alembic migrations.

The database is designed around a small number of core entities that represent portfolios, financial instruments, holdings, market data and calculated risk metrics.

---

# Entity Relationship Diagram

```text
Portfolio
    │
    │ 1
    │
    ▼
Position
    ▲
    │ *
    │
Instrument
    │
    ├──────────► Price
    │
    └──────────► RiskResult
```

---

# Tables

## Portfolio

Represents a logical investment portfolio.

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary key |
| name | String | Portfolio name |
| base_currency | String | Reporting currency |
| source | String | Manual, CSV, Alpaca, Freetrade |
| created_at | Timestamp | Creation time |

Relationships

- One Portfolio has many Positions
- One Portfolio has many Risk Results

---

## Instrument

Represents a tradable financial instrument.

| Column | Type |
|---------|------|
| id | UUID |
| symbol | String |
| name | String |
| instrument_type | String |
| currency | String |
| sector | String |
| cusip | String |
| isin | String |
| sedol | String |

Relationships

- One Instrument has many Prices
- One Instrument has many Positions

---

## Position

Represents an instrument held within a portfolio.

| Column | Type |
|---------|------|
| id | UUID |
| portfolio_id | FK |
| instrument_id | FK |
| quantity | Decimal |
| average_cost | Decimal |

Unique Constraint

```
(portfolio_id, instrument_id)
```

---

## Price

Stores historical market prices.

| Column | Type |
|---------|------|
| id | UUID |
| instrument_id | FK |
| price_date | Date |
| close_price | Decimal |
| currency | String |

Unique Constraint

```
(instrument_id, price_date)
```

---

## RiskResult

Stores calculated analytics.

| Column | Type |
|---------|------|
| id | UUID |
| portfolio_id | FK |
| metric | String |
| value | Decimal |
| calculation_date | DateTime |
| method | String |
| parameters | JSONB |

Examples

- historical_var
- expected_shortfall
- dv01
- pv01
- cs01
- volatility
- sharpe_ratio

---

# Indexes

Recommended indexes

Portfolio

- name

Instrument

- symbol
- isin
- cusip
- sedol

Position

- portfolio_id
- instrument_id

Price

- instrument_id
- price_date

RiskResult

- portfolio_id
- calculation_date
- metric

---

# Migration Workflow

Generate migration

```bash
uv run alembic -c Backend/alembic.ini revision --autogenerate -m "description"
```

Apply migration

```bash
uv run alembic -c Backend/alembic.ini upgrade head
```

Current revision

```bash
uv run alembic -c Backend/alembic.ini current
```

---

# Future Tables

Planned additions

- YieldCurve
- DiscountCurve
- FXRate
- CreditSpread
- Trade
- Cashflow
- CouponSchedule
- Scenario
- StressTest