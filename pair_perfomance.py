import pandas as pd

class PairPerformance:
	def __init__(self, pair, trades):
		self.pair = pair
		self.trades = trades
	def to_dataframe(self):
		df = pd.DataFrame(self.trades)
		df['pair'] = self.pair
		return df
	def win_rate(self):
		df = self.to_dataframe()
		wins = df[df['outcome'] == 'win']
		win_rate = (len(wins) / len(df)) * 100
		return f'Your Win Rate: {win_rate}%'
	def pip_summary(self):
		df = self.to_dataframe()
		pips = df['pips']
		total_pips = pips.sum() # # Pandas in-built function for average calculations
		average_pips = pips.mean() # Pandas in-built function for average calculations
		return f'Total Pips: {total_pips}' , f'Average Pips: {average_pips}'

trades = [{'pips': 40, 'outcome': 'win'},
		  {'pips': -20, 'outcome': 'loss'},
		  {'pips': -10, 'outcome': 'loss'},
		  {'pips': -32, 'outcome': 'loss'},
		  {'pips': 100, 'outcome': 'win'},
		  {'pips': 50, 'outcome': 'win'},
		  {'pips': -20, 'outcome': 'loss'},
		  {'pips': -30, 'outcome': 'loss'}]

objects = PairPerformance('EURUSD', trades)
print(objects.to_dataframe())
print(objects.win_rate())
print(objects.pip_summary())
