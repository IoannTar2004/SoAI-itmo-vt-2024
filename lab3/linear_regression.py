import matplotlib.pyplot as plt
import numpy as np


class Stat:

    def __init__(self, plt, df):
        self.plt = plt
        self.df = df

    def getSelection(self, key):
        count = self.df[key].value_counts()
        return count.index, count.values

    def print_stat(self, key):
        feature = self.df[key]
        print('Количество: ', feature.count)

    def draw_bar(self, key: str, labels: tuple, position):
        self.plt.subplot(position[0], position[1], position[2])
        self.plt.title(key)
        i, v = self.getSelection(key)
        self.plt.xlabel(labels[0])
        self.plt.ylabel(labels[1])
        self.plt.bar(i, v)

        print(self.df[key].describe(), '\n')

    def approximate(self, x_features: list, y_feature: str, frac):
        print('Независимые признаки: ', x_features)
        print('Зависимый признак: ', y_feature)
        length = int(len(self.df[x_features[0]]) * (1 - frac))
        a_raw = []
        for i in range(length):
            a_raw.append([])
            for j in range(len(x_features) + 1):
                if j == 0:
                    append = 1
                else:
                    if self.df[x_features[j-1]][i] == 'No':
                        append = 0
                    elif self.df[x_features[j-1]][i] == 'Yes':
                        append = 1
                    else:
                        append = self.df[x_features[j-1]][i]
                a_raw[i].append(append)

        a = np.array(a_raw)
        y = np.array(self.df[y_feature][:length])
        at = np.transpose(a)
        at_a = np.matmul(at, a)
        at_a_inv = np.linalg.inv(at_a)
        at_a_inv_at = np.matmul(at_a_inv, at)
        ratios = np.matmul(at_a_inv_at, y)
        print('ratios: ', ratios)

        if len(ratios) == 2:
            self.plt.subplot()
            for i in range(100):
                self.plt.scatter(self.df[x_features[0]][i], y[i])
            x = np.array([self.df[x_features].values.min(), self.df[x_features].values.max()])
            x = np.array([0, 1]) if x[0] == 'No' else x
            y1 = ratios[0] + ratios[1] * x
            self.plt.plot(x, y1)
            plt.show()
        print()
        return ratios

    def getDeterminantRatio(self, ratios: list, x_features: list, y_feature: str, frac):
        length = int(len(self.df[x_features[0]]))
        pos = int(len(self.df[x_features[0]]) * frac)
        y = self.df[y_feature]
        sum1 = 0
        sum2 = 0
        for i in range(pos):
            y_predicted = ratios[0]
            for j in range(0, len(x_features)):
                if self.df[x_features[j]][length - pos + j] == 'No':
                    add = 0
                elif self.df[x_features[j]][length - pos + j] == 'Yes':
                    add = 1
                else:
                    add = self.df[x_features[j]][length - pos + j]
                y_predicted += ratios[j+1] * add
            sum1 += (y[i] - y_predicted)**2
            sum2 += (y[i] - y.mean())**2
        return 1 - sum1/sum2


