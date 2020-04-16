# Import pandas
import pandas as pd

# Read in dataset from csv file
trends = pd.read_csv("google_trends_data.csv")

# Inspect top rows of data
print(trends.head())

# Inspect data types
print(trends.info())

# Change column names
trends.columns = ['month', 'mayweather', 'ronaldo', 'messi', 'james', 'federer']

# Convert month to type datetime
trends['month'] = pd.to_datetime(trends['month'])

# Set month as DataFrame index
trends = trends.set_index('month')

# Inspect the data
print(trends.head())

# Import pyplot from matplotlib
from matplotlib import pyplot as plt

# Plot search interest with months on horizontal axis
trends.plot()
plt.show() 

# Zoom in from beginning of 2015 to end of 2017

trends.loc['2015-01-01':'2017-12-31'].plot()
plt.show()
    	
# Smooth the data with a 12-month rolling average
trends.rolling(window=12).mean().plot()
plt.show()

# Create new columns with search interest for soccer stars vs other 3
trends['soccer stars'] = (trends.ronaldo + trends.messi)/2
trends['other 3 stars'] = (trends.mayweather + trends.james + trends.federer)/3

# Plot rolling search interest soccer vs other 
trends.loc[:,['soccer stars','other 3 stars']].rolling(window=12).mean().plot()
plt.show()

# Show average interest for each athlete in bar chart 
trends.iloc[:,0:5].mean().plot.bar()
plt.show()