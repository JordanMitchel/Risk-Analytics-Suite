# 📊 Risk Analytics Suite  
*A modular risk management platform built with Python + QuantLib + React.*  

This suite brings together **three core risk modules**:  
1. **Fixed Income Portfolio Risk Dashboard** → Yield Curves, DV01, Exposures  
2. **Concentration Risk Monitor** → Market Share & Liquidity Risk  
3. **Monte Carlo VaR Engine (with GARCH)** → Quantile-based Loss Estimates (VaR & ES)  

Each module is designed to plug into a shared API and visualization layer, providing traders, risk managers, and compliance officers with complementary perspectives on portfolio risk.  

---

## 1️⃣ Fixed Income Portfolio Risk Dashboard  
**Project Status**: In Development  
**License**: MIT  

This project is a full-stack, interactive dashboard for fixed-income portfolio risk management. It integrates advanced quantitative finance analytics powered by QuantLib with a modern, real-time web interface built with React.  

### 🚀 Project Overview  
Provides portfolio managers and risk analysts with a consolidated view of **yield curves, DV01, and notional exposures**, updated in real time.  

### ✨ Features  
- **Risk Analytics**: DV01, key-rate DV01, duration, and convexity on bonds and portfolios.  
- **Interactive Visualizations**: Yield curves and sensitivities shown dynamically with Recharts/Plotly.  
- **Portfolio Aggregation**: Consolidated fixed income risk measures across holdings.  
- **Market Data Processing**: Yield curve bootstrapping from deposits, futures, swaps, and bonds.  
- **Volatility Overlays**: Incorporates **GARCH-based volatility forecasts** to stress-test interest rate sensitivity under varying market regimes.  
- **Modern Web Stack**: Python (FastAPI, QuantLib) backend + React/TypeScript frontend.  
- **Containerized Architecture**: Dockerized setup for consistent deployment.  

---

## 2️⃣ Concentration Risk Monitor  
**Project Status**: In Development  
**License**: MIT  

This module monitors **liquidity and market concentration risk**, assessing whether a portfolio or trader holds too large a share of a given market. It helps identify **market impact risk** and **regulatory threshold breaches**.  

### 🚀 Project Overview  
Provides traders and compliance teams with **real-time insights into market share exposure**, using market-wide trade and volume data compared against internal positions.  

### ✨ Features  
- **Market Share Metrics**: % of market volume, open interest, and participation vs ADV.  
- **Liquidity Risk**: Detects when positions dominate daily market flows.  
- **Concentration Indices**: HHI (Herfindahl-Hirschman Index) for position spread.  
- **Threshold Alerts**: Configurable alerts when crossing 10%, 25% market share.  
- **APIs**: Access concentration reports at instrument or portfolio level.  
- **Dashboard Visuals**: Heatmaps and charts to track concentration risk across instruments.  
- **Volatility Context**: Adjusts alerts dynamically if **GARCH forecasts predict elevated volatility**, highlighting times when concentration risk is most dangerous.  

---

## 3️⃣ Monte Carlo VaR Engine (with GARCH)  
**Project Status**: In Development  
**License**: MIT  

This module implements a **Monte Carlo simulation engine** to compute Value-at-Risk (VaR) and Expected Shortfall (ES) for multi-asset portfolios.  

### 🚀 Project Overview  
Uses simulated market scenarios to estimate potential portfolio losses at chosen confidence levels (95%, 99%), giving risk managers a **probabilistic view of downside risk**.  

### ✨ Features  
- **Monte Carlo Simulation**: Generate thousands of market scenarios based on covariance and volatility estimates.  
- **VaR & ES**: Compute 95%/99% quantile VaR and Expected Shortfall.  
- **GARCH Volatility Forecasting**:  
  - Captures **volatility clustering** often seen in markets.  
  - Provides **time-varying volatility inputs** into Monte Carlo simulations.  
  - Extensible to **multivariate/DCC-GARCH** for modeling correlations.  
- **Flexible Inputs**: Works with equities, bonds, FX, and rates.  
- **APIs**: Retrieve VaR metrics and P&L distributions programmatically.  
- **Interactive Visuals**: Histogram of simulated losses and tail risk exposure.  
- **Scalable Compute**: Parallelized simulation for large scenario counts.  

---

## 🛠️ Tech Stack  

### **Backend**  
- **Python**: Core language for risk engines, data processing, and backend services.  
- **FastAPI**: High-performance web framework to expose risk calculation APIs.  
- **QuantLib (C++ / Python bindings)**: Industry-standard quantitative finance library for yield curves, bond pricing, and risk measures.  
- **arch**: GARCH volatility forecasting library.  
- **NumPy / Pandas / SciPy**: Numerical computing and statistical analysis.  
- **C++ Extensions**: For performance-critical routines in curve construction and simulation.  

### **Frontend**  
- **React**: JavaScript library for building a responsive and modular user interface.  
- **TypeScript**: Type-safe, robust frontend development.  
- **Recharts / Plotly**: For interactive yield curve plots, VaR histograms, and heatmaps of concentration risk.  
- **TailwindCSS**: Utility-first CSS framework for clean and modern UI styling.  

### **Database / Data Layer**  
- **MongoDB**: Stores market data, portfolio holdings, yield curves, and simulation results.  
- **JSON Schemas**: Enforce a standardized contract between backend APIs and frontend consumers.  
- **External APIs**:  
  - **FRED API** → Free economic data (Treasury yields, benchmarks).  
  - **Market / Exchange APIs** → For trading volumes and open interest (concentration risk).  
  - **Mock Portfolio Generator** → For testing and backfilling scenarios.  

### **Infrastructure**  
- **Docker**: Containerization for backend and frontend services.  
- **CI/CD Pipelines**: GitHub Actions or GitLab CI for automated testing, build, and deployment.  
- **Kubernetes (optional future extension)**: Orchestration for scaling Monte Carlo simulations and risk services.  
- **Logging & Monitoring**: Structured logs via Python’s `logging` + Prometheus/Grafana for metrics.  

---

## 🔹 Example Use Cases  
- **Fixed Income Desk:** Stress-test portfolio DV01 under yield curve shifts.  
- **Compliance / Risk:** Identify outsized positions that move markets.  
- **Risk Management:** Report 99% Monte Carlo VaR to senior management.  
- **Research:** Fit GARCH models to interest rates or FX returns to test volatility persistence.  

---

## 📘 What is GARCH?  

**GARCH (Generalized Autoregressive Conditional Heteroskedasticity)** is a statistical model that estimates **time-varying volatility** in financial markets.  

Key ideas:  
- Volatility is not constant — markets experience **clusters of high and low volatility**.  
- GARCH uses past **returns and past volatility** to forecast future volatility.  
- GARCH(1,1) is the most common form, balancing simplicity with accuracy.  

### 🔢 Formula (GARCH(1,1))  

The conditional variance (σ²ₜ) is modeled as:  

$$
\sigma_t^2 = \omega + \alpha \cdot \varepsilon_{t-1}^2 + \beta \cdot \sigma_{t-1}^2
$$  

Where:  
- **σ²ₜ** = forecast variance at time *t*  
- **ω** = long-run variance (baseline level of volatility)  
- **α** = weight on yesterday’s squared shock (**ε²**) → “news” impact  
- **β** = weight on yesterday’s variance (**σ²**) → “volatility persistence”  

### 📈 Why use GARCH in this suite?  
- In **Monte Carlo VaR Engine** → feeds **time-varying volatility forecasts** into simulations, improving tail risk accuracy.  
- In **Fixed Income Dashboard** → overlays volatility-adjusted DV01 sensitivity under turbulent conditions.  
- In **Concentration Risk Monitor** → adjusts alerts dynamically when GARCH predicts volatility spikes, highlighting periods when concentrated positions are riskiest.  

This makes GARCH especially valuable for **risk managers and researchers** seeking realistic modeling of volatility dynamics.  


---

## 🔹 Future Extensions  
- **DCC-GARCH** for modeling time-varying correlations.  
- Stress testing (historical scenarios, macro shocks).  
- Liquidity-adjusted VaR (L-VaR).  
- Machine learning models for curve interpolation & risk forecasting.  
- Unified reporting dashboard across all three modules.  

---

⚡ With this Risk Analytics Suite, you gain **three orthogonal lenses** on portfolio risk:  
- **Sensitivity (DV01 & Yield Curves)**  
- **Concentration (Market Share Risk)**  
- **Probabilistic Loss (Monte Carlo VaR with GARCH)**  

---

## 📦 Getting Started  

### Prerequisites  
Make sure you have the following installed:  
* [Git](https://git-scm.com/)  
* [Docker](https://www.docker.com/get-started)  
* [Docker Compose](https://docs.docker.com/compose/install/)  

### Installation  

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
