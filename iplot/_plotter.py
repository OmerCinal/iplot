import pandas as pd
import plotly.graph_objects as go
from ._utils import DefaultsDict


class Iplot:

    _kinds = {
        'scatter': go.Scatter,
        'bar': go.Bar
    }

    def __new__(cls, *args, **kwargs):
        instance = super(Iplot, cls).__new__(cls, *args, **kwargs)
        return instance.get_figure()

    def __init__(self, df, *args, **kwargs):
        self.df = df.copy(deep=True)
        if isinstance(self.df, pd.Series):
            self.df = self.df.to_frame(self.df.name)

        self._defaults = DefaultsDict(kwargs)

    def get_figure(self):
        self.figure = go.Figure([
                data=self.get_data(),
                layout=self.get_layout(),
            ])
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
