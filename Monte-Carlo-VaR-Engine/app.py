# PULL
# GET historical price data for assets (from FRED, Yahoo Finance API, or other sources)
# GET portfolio holdings from MongoDB
# pull into objects with returns data

# STORE
# store historical return series in MongoDB
# store portfolio weights/positions in MongoDB

# CALCULATE
# pull historical returns & portfolio weights into Python/QuantLib
# generate correlated random scenarios (e.g., 100,000 paths) using Monte Carlo
# compute simulated portfolio returns distribution
# extract Value-at-Risk at chosen quantiles (95%, 99%)
# compute Expected Shortfall (conditional tail expectation)
# persist VaR results and distribution snapshots back into MongoDB

# DISPLAY
# api GET var_estimates(my_id, confidence_level, horizon)
# api GET return_distribution(my_id, date_range)
# api GET stress_test_results(my_id, scenario_id)
