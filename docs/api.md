# API Reference

## Overview

The Risk Analytics Suite exposes a versioned REST API through FastAPI.

Base path:

```text
/api/v1
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

OpenAPI schema:

```text
http://127.0.0.1:8000/openapi.json
```

## Response conventions

Typical error response:

```json
{
  "detail": "Description of the error"
}
```

| Status | Meaning |
|---|---|
| `200` | Request completed |
| `201` | Resource created |
| `400` | Invalid request |
| `404` | Resource not found |
| `409` | Duplicate or conflicting resource |
| `422` | Request validation failed |
| `500` | Internal server error |
| `502` | External provider unavailable |

## Health

```http
GET /health
```

```json
{
  "status": "ok"
}
```

## Portfolios

### Create portfolio

```http
POST /api/v1/portfolios
```

```json
{
  "name": "Global Macro Portfolio",
  "base_currency": "GBP"
}
```

```json
{
  "id": "7a34fc39-45d2-4ea8-84b3-632cf477af47",
  "name": "Global Macro Portfolio",
  "base_currency": "GBP",
  "created_at": "2026-07-13T12:00:00"
}
```

### List portfolios

```http
GET /api/v1/portfolios
```

### Get portfolio

```http
GET /api/v1/portfolios/{portfolio_id}
```

### Get portfolio positions

```http
GET /api/v1/portfolios/{portfolio_id}/positions
```

## Portfolio imports

### CSV import

```http
POST /api/v1/imports/portfolio
Content-Type: multipart/form-data
```

Required CSV columns:

```text
portfolio_name
base_currency
symbol
instrument_name
instrument_type
currency
quantity
average_cost
```

Optional columns:

```text
sector
cusip
isin
sedol
```

Example:

```csv
portfolio_name,base_currency,symbol,instrument_name,instrument_type,currency,sector,quantity,average_cost
Global Macro Portfolio,GBP,AAPL,Apple Inc,EQUITY,USD,Technology,100,185.50
Global Macro Portfolio,GBP,MSFT,Microsoft Corp,EQUITY,USD,Technology,75,420.25
```

Planned response:

```json
{
  "portfolio_name": "Global Macro Portfolio",
  "rows_received": 2,
  "instruments_created": 2,
  "instruments_reused": 0,
  "positions_created": 2,
  "positions_updated": 0,
  "rows_rejected": 0,
  "errors": []
}
```

### Alpaca import

```http
POST /api/v1/imports/alpaca
```

```json
{
  "portfolio_name": "Alpaca Paper Portfolio",
  "base_currency": "USD"
}
```

### Freetrade import

```http
POST /api/v1/imports/freetrade
Content-Type: multipart/form-data
```

Planned functionality:

- Parse activity statements
- Reconstruct holdings
- Process buys and sells
- Calculate average cost
- Create or update positions

## Market data

```http
POST /api/v1/prices/import
GET /api/v1/instruments/{instrument_id}/prices
GET /api/v1/instruments/{instrument_id}/prices/latest
```

## Portfolio analytics

```http
GET /api/v1/portfolios/{portfolio_id}/valuation
GET /api/v1/portfolios/{portfolio_id}/statistics
GET /api/v1/portfolios/{portfolio_id}/exposures
```

Planned outputs include valuation, P&L, weights, returns, volatility, Sharpe Ratio, drawdown, correlation, covariance and exposures.

## Fixed-income analytics

```http
GET /api/v1/portfolios/{portfolio_id}/duration
GET /api/v1/portfolios/{portfolio_id}/convexity
GET /api/v1/portfolios/{portfolio_id}/dv01
GET /api/v1/portfolios/{portfolio_id}/pv01
GET /api/v1/portfolios/{portfolio_id}/cs01
```

## Portfolio risk

```http
POST /api/v1/portfolios/{portfolio_id}/risk/historical-var
POST /api/v1/portfolios/{portfolio_id}/risk/parametric-var
POST /api/v1/portfolios/{portfolio_id}/risk/monte-carlo-var
```

Example planned request:

```json
{
  "confidence_level": 0.95,
  "lookback_days": 252,
  "holding_period_days": 1
}
```

## Stress testing

```http
POST /api/v1/portfolios/{portfolio_id}/stress-tests
```

Planned scenarios:

- Interest-rate shocks
- Credit-spread shocks
- FX shocks
- Equity shocks
- Historical stress scenarios