import numpy as np

from utils.Stat import Stat
import collections


class KNN(Stat):
    def __init__(self, plt, df):
        super().__init__(plt, df)

    def scaling(self):
        for col in self.df.keys():
            if col != 'Outcome':
                self.df[col] = (self.df[col] - np.min(self.df[col])) / (np.max(self.df[col]) - np.min(self.df[col]))

    def draw_3d_scatter(self, frac: float, features: list, ax):
        x = self.getPartialSelection(frac, features[0], "learning")
        y = self.getPartialSelection(frac, features[1], "learning")
        z = self.getPartialSelection(frac, features[2], "learning")
        c = self.getPartialSelection(frac, "Outcome", "learning")

        ax.set_xlabel(features[0])
        ax.set_ylabel(features[1])
        ax.set_zlabel(features[2])

        ax.scatter(x, y, z, c=c, cmap='autumn', marker='o')

    def knn_method(self, values: dict, k):
        features = list(values.keys())
        y_list = list(values.values())
        near_dict = {}
        for i in range(self.df_len):
            cur_dist = 0
            for n, j in enumerate(features):
                cur_dist += abs(self.df[j][i] - y_list[n])
            near_dict[cur_dist] = self.df["Outcome"][i]

        near_dict = list(collections.OrderedDict(sorted(near_dict.items())).values())
        sum_classes = {0: 0, 1: 0}
        for i in range(k):
            sum_classes[near_dict[i]] += 1
        return 0 if sum_classes[0] > sum_classes[1] else 1

