# Fixed Income Analytics

## Overview

The Fixed Income module provides institutional-grade bond pricing and interest-rate risk analytics using QuantLib.

The module is designed to support government bonds, corporate bonds and credit products while exposing reusable pricing and sensitivity APIs.

---

# Roadmap

## Stage 1

- Bond pricing
- Clean price
- Dirty price
- Accrued interest
- Cashflow generation

---

## Stage 2

- Treasury curve construction
- Discount curves
- Spot curves
- Forward curves
- Curve bootstrapping

---

## Stage 3

Interest-rate sensitivities

- Duration
- Modified Duration
- Convexity
- DV01
- PV01
- Key Rate DV01
- Key Rate PV01

---

## Stage 4

Credit analytics

- Credit spread curves
- Hazard rates
- Z-Spread
- Option Adjusted Spread
- CS01
- Key Spread CS01

---

# Architecture

```text
Portfolio
      │
      ▼
Position
      │
      ▼
Bond Instrument
      │
      ▼
Yield Curve
      │
      ▼
QuantLib Pricing
      │
      ▼
Risk Measures
```

---

# Analytics Pipeline

```text
Portfolio
      │
      ▼
Market Data
      │
      ▼
Yield Curve
      │
      ▼
Pricing Engine
      │
      ▼
Risk Engine
      │
      ▼
     API
```

---

# Supported Analytics

## Bond Pricing

- Clean Price
- Dirty Price
- Accrued Interest
- Yield to Maturity
- Cashflows

---

## Interest Rate Risk

- Duration
- Modified Duration
- Convexity

---

## First Order Sensitivities

- DV01
- PV01
- Key Rate DV01
- Key Rate PV01

---

## Credit Risk

- Credit Spread
- CS01
- Key Spread CS01
- Z-Spread
- OAS

---

# Market Data Sources

Planned providers

- FRED
- US Treasury
- ECB
- CSV
- Manual
- Mock Data

---

# QuantLib Components

The project will make use of:

- Dates
- Calendars
- Day Count Conventions
- Schedules
- YieldTermStructure
- Piecewise Yield Curves
- FixedRateBond
- DiscountingBondEngine
- Zero Spreaded Curves

---

# Planned API

```http
GET /portfolio/{id}/duration

GET /portfolio/{id}/convexity

GET /portfolio/{id}/dv01

GET /portfolio/{id}/pv01

GET /portfolio/{id}/cs01

GET /portfolio/{id}/yield-curve
```

---

# Planned Dashboard

Interactive views

- Yield Curve
- Cashflow Schedule
- Bond Analytics
- Duration Breakdown
- DV01 Heatmap
- Credit Spread Analysis
- Portfolio Interest Rate Risk