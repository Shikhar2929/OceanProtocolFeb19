import random
import yfinance

class Model:

	def __init__(self, data, generator):
		self.data = data
		self.generator = generator

	def predict(self, iterations):
		return [self.generator(self.data, i) for i in range(iterations)]


def fetch_data():
	eth = yfinance.Ticker('ETH-USD')
	data = eth.history(period='1d', interval='1m')
	return data['Close'][-1]


threshold = 0.00219454
flat_generator = lambda x, i: x + threshold * x * random.random() * random.choice((-1, 1))
increase_generator = lambda x, i: x + (threshold * x * random.random() * random.choice((-1, 1)) ) + (threshold * x * i)
decrease_generator = lambda x, i: x + (threshold * x * random.random() * random.choice((-1, 1)) ) - (threshold * x * i)

current_price = fetch_data()
#flat_model = Model(current_price, flat_generator)
#increase_model = Model(current_price, increase_generator)
decrease_model = Model(1682, decrease_generator)

#print('flat model: ', flat_model.predict(iterations=12))
#print('increase model: ', increase_model.predict(iterations=12))
#l = str(decrease_model.predict(iterations=12))
print('increase model: ', decrease_model.predict(iterations=12))