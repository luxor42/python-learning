## Slicing particular values from a multiindex

# This slices out given tickers dates without resetting the index
# There are other values lexically between AAPL and MSFT, but we're just selecting those



# Selecting individual tickers and dates
all_data.loc[pd.IndexSlice[['AAPL','MSFT'],['2012-01-03','2012-01-04']], :]

# To select a date range
all_data.loc[pd.IndexSlice[['AAPL','MSFT'],pd.date_range('2012-01-03','2012-01-05')], :]


## Slicing single value with .xs

all_data.xs(('UAL','2012-01-03'),level=['Ticker','Date'], drop_level=False)


## Stacking and Unstacking
# Unstack = Rows to Columns - DF GETS SHORTER BUT WIDER
# Stack   = Columns to Rows - DF GETS LONGER BUT THINNER
# https://pandas.pydata.org/pandas-docs/stable/reshaping.html#multiple-levels
'''
	Ticker	Date	Close
0	AAPL	2012-01-03	58.75
1	AAPL	2012-01-04	59.06
2	AAPL	2012-01-05	59.72
'''

all_data.unstack(level=['Ticker'])['Close']

'''
Ticker		AAPL	MSFT	GE		IBM		DAL		UAL		PEP		KO
Date								
2012-01-03	58.75	26.76	18.36	186.30	8.04	18.90	66.40	35.07
2012-01-04	59.06	27.40	18.56	185.54	8.01	18.52	66.74	34.85
'''