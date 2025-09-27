# 📊 Risk Analytics Suite  
*A modular risk management platform built with Python + QuantLib + React.*  

This suite brings together **three core risk modules**:  
1. **Fixed Income Portfolio Risk Dashboard** → Yield Curves, DV01, Exposures  
2. **Concentration Risk Monitor** → Market Share & Liquidity Risk  
3. **Monte Carlo VaR Engine** → Quantile-based Loss Estimates (VaR & ES)  

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

---

## 3️⃣ Monte Carlo VaR Engine  
**Project Status**: In Development  
**License**: MIT  

This module implements a **Monte Carlo simulation engine** to compute Value-at-Risk (VaR) and Expected Shortfall (ES) for multi-asset portfolios.  

### 🚀 Project Overview  
Uses simulated market scenarios to estimate potential portfolio losses at chosen confidence levels (95%, 99%), giving risk managers a **probabilistic view of downside risk**.  

### ✨ Features  
- **Monte Carlo Simulation**: Generate thousands of market scenarios based on covariance and volatility estimates.  
- **VaR & ES**: Compute 95%/99% quantile VaR and Expected Shortfall.  
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
- **NumPy / Pandas / SciPy**: Numerical computing and statistical analysis, powering Monte Carlo simulations and matrix operations.  
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
- **Docker**: Containerization for backend and frontend services, ensuring consistent dev/prod environments.  
- **CI/CD Pipelines**: GitHub Actions or GitLab CI for automated testing, build, and deployment.  
- **Kubernetes (optional future extension)**: Orchestration for scaling Monte Carlo simulations and risk services.  
- **Logging & Monitoring**: Structured logs via Python’s `logging` + Prometheus/Grafana for risk service metrics.  

---

## 🔹 Example Use Cases  
- **Fixed Income Desk:** Stress-test portfolio DV01 under yield curve shifts.  
- **Compliance / Risk:** Identify outsized positions that move markets.  
- **Risk Management:** Report 99% Monte Carlo VaR to senior management.  

---

## 🔹 Future Extensions  
- Stress testing (historical scenarios, macro shocks).  
- Liquidity-adjusted VaR (L-VaR).  
- Machine learning models for curve interpolation & risk forecasting.  
- Unified reporting dashboard across all three modules.  

---

⚡ With this Risk Analytics Suite, you gain **three orthogonal lenses** on portfolio risk:  
- **Sensitivity (DV01 & Yield Curves)**  
- **Concentration (Market Share Risk)**  
- **Probabilistic Loss (Monte Carlo VaR)** 
## 📦 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Make sure you have the following installed:
*   [Git](https://git-scm.com/)
*   [Docker](https://www.docker.com/get-started)
*   [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2.  **Start the application with Docker Compose:**
    ```sh
    docker-compose up --build
    ```
    This command will build the Docker images for both the backend and frontend and start the application.

3.  **Access the application:**
    *   **Frontend:** Navigate to `http://localhost:3000` in your web browser.
    *   **Backend API:** The FastAPI service will be running on `http://localhost:8000`. You can view the automatically generated API documentation at `http://localhost:8000/docs`.

## 🤝 Contributing

Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📬 Contact

Your Name - jmitchel24@gmail.com

Project Link: [https://github.com/JordanMitchel/Fixed-Income-Risk-Dashboard](https://github.com/JordanMitchel/Fixed-Income-Risk-Dashboard)
