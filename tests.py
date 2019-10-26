import pandas as pd
import numpy as np
import ipear


def generate_random_series(n=10):
	return pd.Series((np.random.random() for _ in range(n)))


def generate_random_dataframe(m=4, n=10):
	return pd.DataFrame([generate_random_series(n) for _ in range(m)])


def test_iplot(m=4, n=10, **kwargs):
	df = generate_random_dataframe(m, n)
	fig = df.iplot(**kwargs)
	return fig

if __name__ == '__main__':
	test_iplot()