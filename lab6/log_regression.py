import numpy as np
from pandas import DataFrame

from utils.Stat import Stat


def hypothesis_function(df, row: int, ratios: list):
    z = np.dot(df.iloc[row], ratios)
    return 1 / (1 + np.exp(-z))


class LogRegression(Stat):

    def __init__(self, plt, df: DataFrame, target):
        self.df_target = df[[target]]
        self.params = np.random.uniform(-0.1, 0.1, len(df.columns) - 1)
        df_filtered = df.drop(columns=[target])
        super().__init__(plt, df_filtered)

    def scaling(self):
        for col in self.df.keys():
            if col not in ['Outcome', 'Ones']:
                self.df[col] = (self.df[col] - np.min(self.df[col])) / (np.max(self.df[col]) - np.min(self.df[col]))

    def log_loss(self):
        s = 0
        eps = 1e-10
        for i in range(self.df_len):
            hyp = hypothesis_function(self.df, i, self.params)
            y = self.df_target.iloc[i, 0]
            s += y * np.log(hyp + eps) + (1 - y) * np.log(1 - hyp + eps)
        return -s / self.df_len

    def gradient(self):
        gradient = np.zeros(len(self.params))
        for k in range(self.df_len):
            gradient += (hypothesis_function(self.df, k, self.params) - self.df_target.iloc[k, 0]) \
                        * self.df.iloc[k].values
        return gradient / self.df_len

    def newton(self, iterations):
        h = 0
        for i in range(iterations):
            g = self.gradient()
            for k in range(self.df_len):
                hyp = hypothesis_function(self.df, k, self.params)
                h += hyp * (1 - hyp) * np.dot(self.df.iloc[k].values, self.df.iloc[k].values)
            self.params -= h / self.df_len * g

    def gradient_descent(self, a, iterations):
        for i in range(iterations):
            gradient = self.gradient()
            self.params -= a * gradient

    def class_estimation(self, df_test: DataFrame, df_all: DataFrame, target):
        estimations = {"TP": 0, "FN": 0, "TN": 0, "FP": 0}
        for i in range(len(df_test)):
            real = df_all[[target]].iloc[i, 0]
            test = 1 if hypothesis_function(df_test, i, self.params) >= 0.5 else 0
            print(hypothesis_function(df_test, i, self.params))

            if real == 1:
                if test == 1:
                    estimations["TP"] += 1
                else:
                    estimations["FN"] += 1
            else:
                if test == 0:
                    estimations["TN"] += 1
                else:
                    estimations["FP"] += 1
        return estimations
