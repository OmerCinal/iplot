from dataclasses import dataclass


class DefaultsDict(dict):
    def __missing__(self, key):
        return FigureDefaults.__dict__[key]


@dataclass
class FigureDefaults:
    kind: str = 'scatter'
