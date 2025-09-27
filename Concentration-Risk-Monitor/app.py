# PULL
# GET market volume & open interest data via API (e.g., exchange feeds, free sources if available)
# GET my portfolio trades & positions from MongoDB
# pull both sets of data into objects

# STORE
# store market data snapshots in MongoDB for historical analysis
# store portfolio trades/positions in MongoDB

# CALCULATE
# pull data into Python objects
# calculate my participation rate = (my_volume / total_market_volume)
# calculate Herfindahl-Hirschman Index (HHI) for concentration across instruments
# flag if participation exceeds thresholds (e.g., >10% of market, or regulatory red lines)
# compare across timeframes (daily, weekly, monthly) to see concentration trends
# restore results to MongoDB for persistence

# DISPLAY
# api GET concentration_by_inst(inst_id, date_range)
# api GET portfolio_concentration(my_id, date_range)
# api GET market_share_trends(inst_id, rolling_window)
