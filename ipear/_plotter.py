import pandas as pd
import plotly.graph_objects as go
from ipear._utils import DefaultsDict


class Iplot:

    _kinds = {
        'scatter': go.Scatter,
        'bar': go.Bar
    }

    def __new__(cls, df, *args, **kwargs):
        instance = super(Iplot, cls).__new__(cls, *args, **kwargs)
        instance.__init__(df, *args, **kwargs)
        return instance.get_figure()

    def __init__(self, df, *args, **kwargs):
        self._df = df.copy(deep=True)
        if isinstance(self._df, pd.Series):
            self._df = self._df.to_frame(self._df.name)

        self._defaults = DefaultsDict(kwargs)

    def get_figure(self):
        self.figure = go.Figure(
                data=self.get_data(),
                layout=self.get_layout(),
            )
        return self.figure

    def get_data(self):
        charts = [
            self._kinds[self._defaults['kind']](
                    name=str(column),
                    x=self._df[column],
                    y=self._df.index,
                )
            for column in self._df.columns
        ]
        return charts

    def get_layout(self):
        return None



def _iplot(df, *args, **kwargs):
    return Iplot(df, *args, **kwargs)


pd.DataFrame.iplot = _iplot
pd.Series.iplot = _iplot
