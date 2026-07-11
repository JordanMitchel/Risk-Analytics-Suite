#PULL
# GET data from FRED
# pull data into objects
# try in python first before next version in c++

# STORE
# put data from fred into mongo db
# put mock portfolio data into mongo db

# CALCULATE
# pull data from mongodb into objects
# use quant lib to put object data into functions create a yield curve using quant lib
# build the yield curve from multiple instruments

# do this for bonds,swaps
#QuantLib bootstraps the zero rate curve from the market prices (or rates) of instruments, using the cashflows
# internally
# bootstrapping is the process that will allow us to get zero rates from the market price of instruments
# with this yield curve
# pricing each instrument at its own maturity using the bootstrapped curve.
# increase by 1 bp in a parallel shift for all points in maturity to calculate DV01
# this will show how the portfolio is at risk
# for key-dv01 we only shift specific points of maturity by 1bp this allows  for concentrated bp shifts and awareness
#for missing points depends on the type of inst
# --> for short term bonds: use FRAs
#     for midterm swap rates: interpolate
#     for long term: fall back to gov liquid bonds
# restore the data for the apis from a mongoDB for historical dates and a cache for live rates


# DISPLAY
# api GET yield_curve_for_inst_by_date(month, inst type, inst_id)
# api GET all_yield_Curve_by_date(month) all inst types
# api GET my_portfolio_and_yield_curve(my_id,month,inst_type, inst_id)
# api GET my_portfolio_inst_type(my