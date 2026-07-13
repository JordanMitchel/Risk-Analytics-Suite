# Architecture

## Overview

Risk Analytics Suite uses a modular layered architecture designed to separate HTTP concerns, business logic, persistence and quantitative analytics.

```text
React Dashboard
      │
      ▼
FastAPI API Layer
      │
      ▼
Service Layer
      │
      ├───────────────┐
      ▼               ▼
Repository Layer   Analytics Engines
      │               │
      └───────┬───────┘
              ▼
         SQLAlchemy
              │
              ▼
         PostgreSQL
```

The core application flow is:

```text
API → Services → Repositories → Database
```

## API layer

Location:

```text
Backend/app/api/
```

Responsibilities:

- Define routes
- Validate requests
- Select response models
- Map application errors to HTTP status codes
- Inject database sessions and services

The API layer should not contain SQL queries or complex business rules.

## Schema layer

Location:

```text
Backend/app/schemas/
```

Responsibilities:

- Request validation
- Response serialisation
- Currency and identifier normalisation
- API contracts
- Import summaries

Pydantic schemas remain separate from SQLAlchemy models so the public API does not depend directly on persistence objects.

## Service layer

Location:

```text
Backend/app/services/
```

Responsibilities:

- Business rules
- Transaction boundaries
- Import orchestration
- Coordination across repositories
- Portfolio lifecycle workflows

Examples:

- Reject duplicate portfolio names
- Validate base currency consistency
- Reuse existing instruments
- Create or update positions
- Commit or roll back an import

## Repository layer

Location:

```text
Backend/app/repositories/
```

Responsibilities:

- Encapsulate SQLAlchemy queries
- Retrieve and persist entities
- Keep database access out of routes
- Expose focused data-access methods

Examples:

```text
PortfolioRepository.get_by_name()
InstrumentRepository.get_by_symbol()
PositionRepository.get_by_portfolio_and_instrument()
PriceRepository.get_latest_price()
```

## Database layer

Location:

```text
Backend/app/database/
```

Core models:

```text
PortfolioModel
InstrumentModel
PositionModel
PriceModel
RiskResultModel
```

Relationships:

```text
Portfolio 1 ───── * Position * ───── 1 Instrument
    │                                  │
    *                                  *
RiskResult                           Price
```

Important constraints:

- Unique portfolio name
- Unique instrument symbol
- Unique portfolio and instrument position
- Unique instrument and price date
- Unique risk metric per portfolio, date and method where appropriate

## Migrations

Location:

```text
Backend/alembic/
```

Commands:

```bash
uv run alembic -c Backend/alembic.ini current
uv run alembic -c Backend/alembic.ini heads
uv run alembic -c Backend/alembic.ini revision --autogenerate -m "describe change"
uv run alembic -c Backend/alembic.ini upgrade head
```

Generated migrations should be reviewed before application.

## Portfolio import architecture

```text
CSV ─────────┐
Alpaca ──────┼──► Normalised holdings ─► Import service ─► Repositories ─► PostgreSQL
Freetrade ───┘
```

### CSV import

```text
UploadFile
    ↓
Pandas read_csv
    ↓
Column validation
    ↓
String and numeric normalisation
    ↓
Row validation
    ↓
Portfolio, instrument and position persistence
```

Pandas handles parsing, cleaning and validation. The service owns the transaction and persistence workflow.

### Alpaca integration

Location:

```text
Backend/app/integrations/
```

The adapter:

- Authenticates with Alpaca
- Retrieves open positions
- Converts provider objects into normalised holdings
- Keeps provider-specific models outside the core application

### Transaction behaviour

Imports initially use an all-or-nothing transaction:

```text
Begin
  ↓
Create or reuse portfolio
  ↓
Create or reuse instruments
  ↓
Create or update positions
  ↓
Commit
```

Any unrecoverable error triggers a rollback.

## Analytics architecture

Location:

```text
Backend/app/analytics/
```

Planned modules:

```text
portfolio_analytics/
fixed_income/
market_data/
monte_carlo_var/
concentration_risk/
scenario_analysis/
monitoring/
yield_curves/
```

Pipeline:

```text
Portfolio positions
        ↓
Market data
        ↓
Pricing
        ↓
Portfolio analytics
        ↓
Risk analytics
        ↓
RiskResult persistence
        ↓
API and dashboard
```

## Risk result design

`RiskResultModel` uses a flexible metric-based structure.

Examples:

```text
historical_var
expected_shortfall
annualised_volatility
dv01
pv01
cs01
maximum_drawdown
```

Each record can include portfolio ID, metric name, value, calculation date, method, currency and JSON parameters.

## Configuration

Configuration is loaded using `pydantic-settings`.

```env
DATABASE_URL=
ALPACA_API_KEY=
ALPACA_SECRET_KEY=
ALPACA_PAPER=true
FRED_API_KEY=
```

Secrets must never be committed.

## Dependency injection

```text
get_db()
   ↓
Route
   ↓
Service
   ↓
Repositories
```

For the MVP, services can receive the session and coordinate repositories. A future unit-of-work abstraction may encapsulate transactions more fully.

## Error handling

Application-specific exceptions should be mapped to HTTP responses in the API layer.

Examples:

```text
PortfolioAlreadyExistsError
PortfolioNotFoundError
InstrumentNotFoundError
InvalidPortfolioImportError
ExternalProviderError
```

## Testing strategy

```text
Backend/tests/
├── unit/
├── integration/
└── fixtures/
```

Unit tests cover validation, business rules and analytics. Integration tests cover repositories, API workflows, imports and transaction rollback.

Tests should use a dedicated test database.

## Design principles

- Separation of concerns
- Explicit transaction boundaries
- Provider-independent core models
- Repository pattern
- Service-layer orchestration
- Type-safe schemas
- Reproducible migrations
- Testable analytics
- Incremental vertical slices

## Future evolution

```text
Portfolio Sources
(CSV / Alpaca / Freetrade)
            │
            ▼
Portfolio Management
            │
            ▼
Market Data
            │
            ▼
Pricing and Valuation
            │
      ┌─────┴─────┐
      ▼           ▼
Fixed Income   Portfolio Risk
      │           │
      └─────┬─────┘
            ▼
     Scenario Analysis
            ▼
     React Dashboard
```