# Fixed-Income-Risk-Dashboard
A full-stack risk management dashboard for fixed income portfolios, built with Python + QuantLib + React.

# Fixed Income Portfolio Risk Dashboard

[![Project Status: In Development](https://img.shields.io/badge/Status-In%20Development-yellow)](https://github.com/badges/shields)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This project is a full-stack, interactive dashboard for fixed-income portfolio risk management. It integrates advanced quantitative finance analytics powered by QuantLib with a modern, real-time web interface built with React.

## 🚀 Project Overview

This application showcases a robust architecture for integrating complex financial models with a highly responsive user interface. The system is designed to provide portfolio managers and risk analysts with a real-time, consolidated view of key risk metrics.

## ✨ Features

*   **Risk Analytics:** Perform key risk calculations, including DV01, duration, and convexity, on fixed-income portfolios.
*   **Interactive Visualizations:** Dynamically display financial data through interactive charts and tables using Recharts and Plotly.
*   **Portfolio Aggregation:** Aggregate risk metrics at the portfolio level for a complete risk picture.
*   **Market Data Processing:** Bootstraps yield curves from market instruments to derive accurate risk measures.
*   **Modern Web Stack:** A full-stack solution featuring a high-performance backend (Python/FastAPI) and a modern, responsive frontend (React/TypeScript).
*   **Containerized Architecture:** Uses Docker to ensure a consistent and isolated development, testing, and production environment.

## 📊 System Flow

This section outlines the primary data and processing workflow within the application.

### Data Ingestion and Storage
*   **Pull:** Retrieves market data from sources like the FRED (Federal Reserve Economic Data) API. Python is used for prototyping data models before production implementation.
*   **Store:** Persists the market data (e.g., from FRED) and mock portfolio data into a MongoDB database for efficient access.

### Calculation and Analysis
*   **Load:** Loads the market data from MongoDB into Python objects for processing.
*   **QuantLib Processing:** Uses the QuantLib library to build yield curves from various market instruments, such as bonds and interest rate swaps.
*   **Bootstrapping:** The QuantLib engine bootstraps zero rates from the market prices and cash flows of instruments to construct a precise yield curve.
*   **Pricing:** Instruments are priced based on the bootstrapped yield curve at their respective maturities.
*   **Risk Metrics:** Calculates key risk metrics:
    *   **DV01:** Measures the price sensitivity to a one basis point (1bp) parallel shift of the entire yield curve.
    *   **Key-Rate DV01:** Measures the price sensitivity to 1bp shifts at specific, critical maturities.
*   **Interpolation:** Fills in missing maturities for the yield curve using appropriate methods:
    *   **Short-term:** Forward Rate Agreements (FRAs).
    *   **Mid-term:** Swap interpolation.
    *   **Long-term:** Liquid government bonds.
*   **Data Source:** Historical data is sourced from MongoDB, while live rates are retrieved from a cache for speed.

### API Endpoints (Display)
The backend exposes several API endpoints for the frontend to consume data:
*   `GET /yield_curve_for_inst_by_date/{month}/{inst_type}/{inst_id}`: Fetches the yield curve for a specific instrument on a given date.
*   `GET /all_yield_curve_by_date/{month}`: Retrieves all yield curves for a given month.
*   `GET /portfolio/{portfolio_id}/risk`: Provides aggregated risk metrics for a specific portfolio.
*   `GET /portfolio/{portfolio_id}/{instrument_type}`: Returns portfolio data filtered by instrument type.

## 🛠️ Tech Stack

### Backend
*   **Python:** The core language for the backend service.
*   **FastAPI:** A high-performance web framework for creating the risk calculation APIs.
*   **QuantLib:** A powerful C++ library for quantitative finance, exposed to Python to perform complex calculations.

### Frontend
*   **React:** A JavaScript library for building the user interface.
*   **TypeScript:** Used for type-safe and more robust frontend development.
*   **Recharts / Plotly:** Libraries for creating interactive and customizable charts.

### Infrastructure
*   **Docker:** Used to containerize the backend and frontend services, simplifying setup and deployment.
*   **JSON Schemas:** Enforces a clear and standardized contract between the frontend and backend APIs.
*   **CI/CD:** Prepared for automated continuous integration and deployment with GitHub Actions or GitLab CI.

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
