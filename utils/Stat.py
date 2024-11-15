from pandas import DataFrame


class Stat:
    df: DataFrame

    def __init__(self, plt, df):
        self.plt = plt
        self.df = df
        self.df_len = len(df)

    def getCounts(self, key):
        count = self.df[key].value_counts()
        return count.index, count.values

    def draw_bar(self, key: str, labels: tuple, position):
        self.plt.subplot(position[0], position[1], position[2])
        self.plt.title(key)
        i, v = self.getCounts(key)
        self.plt.xlabel(labels[0])
        self.plt.ylabel(labels[1])
        self.plt.xlim(min(i), max(i))
        self.plt.bar(i, v)

        print(self.df[key].describe(), '\n')

    def getPartialSelection(self, frac, feature, type):
        sels = {"learning": self.df[feature][:int(self.df_len * 0.8)],
                "testing": self.df[feature][int(self.df_len * (1 - frac)):]}
        return sels[type]
