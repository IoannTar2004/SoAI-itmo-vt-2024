import math

import numpy as np
from pandas import DataFrame

from utils.Stat import Stat


class Node:

    def __init__(self, feature):
        self.feature = feature
        self.edges = {}
        self.is_leaf = False
        self.stat = {"Y": 0, "N": 0}

    def __repr__(self):
        return f"Feature = {self.feature}; Edges = {self.edges}; Stat = {self.stat}"


def write_node(node: Node, location: str):
    print(f"{location} -> ", end='')
    for i in node.edges:
        edge = node.edges[i]
        feature = edge.feature if not edge.is_leaf else f"<{edge.feature}>"
        print(f"{i}({feature}), ", end='')
    print()
    for j in node.edges:
        edge = node.edges[j]
        if not edge.is_leaf:
            write_node(edge, location + f"/{j}({edge.feature})")


def find_path(node: Node, features: dict):
    edge = features.get(node.feature)
    if edge is not None and node.edges.get(edge) is not None:
        return find_path(node.edges[edge], features)
    if node.is_leaf:
        return node.feature
    return "Y" if node.stat["Y"] >= node.stat["N"] else "N"


class DecisionTree(Stat):

    def __init__(self, plt, df: DataFrame, target: str):
        super().__init__(plt, df)
        self.threshold = 0
        self.target = target
        self.node = Node('')

    def set_threshold(self, threshold):
        self.threshold = threshold

    def info(self, data, frame=None, value=None):
        if frame is None and value is None:
            sum1 = (data[self.target] >= self.threshold).sum()
            length = len(data)
        else:
            sum1 = ((data[self.target] >= self.threshold) & (data[frame] == value)).sum()
            length = (data[frame] == value).sum()

        sum2 = length - sum1

        frac1, frac2 = sum1 / length, sum2 / length
        expression1 = frac1 * math.log2(frac1) if frac1 != 0 else 0
        expression2 = frac2 * math.log2(frac2) if frac2 != 0 else 0
        return -(expression1 + expression2)

    def info_feature(self, data: DataFrame):
        info = {}
        for c in data.drop(columns=[self.target]).columns:
            sum1 = 0
            unique = data[c].unique().tolist()
            for v in unique:
                sum1 += (data[c] == v).sum() / len(data) * self.info(data, c, v)
            info[c] = sum1
        return info

    def split_info(self, data: DataFrame):
        info = {}
        for c in data.drop(columns=[self.target]).columns:
            sum1 = 0
            unique = data[c].unique().tolist()
            for v in unique:
                frac = (data[c] == v).sum() / len(data)
                sum1 += frac * math.log2(frac)
            info[c] = -sum1
        return info

    def create_node(self, data: DataFrame, node: Node):
        info = self.info(data)
        if info == 0:
            node.is_leaf = True
            node.feature = "N" if data[self.target].values[0] < self.threshold else "Y"
            node.stat[node.feature] = 1
            return
        info_x = self.info_feature(data)
        split = self.split_info(data)

        max_x = float('-inf')
        max_value = ''
        for i in info_x:
            gain = (info - info_x[i]) / split[i] if split[i] != 0 else float('inf')
            if gain > max_x:
                max_x = gain
                max_value = i

        node.feature = max_value
        for i in data[max_value].unique().tolist():
            new_node = Node('')
            node.edges[i] = new_node
            new_data = data[data[max_value] == i].drop(columns=[max_value])
            self.create_node(new_data, new_node)
            for j in node.stat:
                node.stat[j] += new_node.stat[j]

    def build_tree(self):
        self.create_node(self.df, self.node)

    def print_tree(self):
        write_node(self.node, self.node.feature)

    def get_class(self, features: dict, true: str, false: str):
        result = find_path(self.node, features)
        return true if result == "Y" else false

    def class_estimation(self, df_test: DataFrame):
        estimations = {"TP": 0, "FN": 0, "TN": 0, "FP": 0}
        for i, row in df_test.iterrows():
            real = "Y" if row[self.target] >= self.threshold else "N"
            test = self.get_class(row.to_dict(), "Y", "N")

            if real == "Y":
                if test == "Y":
                    estimations["TP"] += 1
                else:
                    estimations["FN"] += 1
            else:
                if test == "N":
                    estimations["TN"] += 1
                else:
                    estimations["FP"] += 1
        return estimations

    def draw_curve(self, name, x, y, xlabel, ylabel):
        x_points = np.array([0, x, 1])
        y_points = np.array([0, y, 0])

        coefficients = np.polyfit(x_points, y_points, 2)
        polynomial = np.poly1d(coefficients)

        x_dense = np.linspace(x_points.min(), x_points.max(), 100)
        y_dense = polynomial(x_dense)

        self.plt.plot(x_dense, y_dense, color="blue")
        self.plt.scatter(x_points, y_points, color="red")
        self.plt.fill_between(x_dense, y_dense, color="lightblue", alpha=0.4)
        self.plt.xlabel(xlabel)
        self.plt.ylabel(ylabel)
        self.plt.title(name)
        self.plt.show()

        return np.trapezoid(y_dense, x_dense)

    def draw_roc(self, fpr, tpr):
        return self.draw_curve("AUC-ROC", fpr, tpr, "FPR", "TPR")

    def draw_pr(self, precision, recall):
        return self.draw_curve("AUC-PR", precision, recall, "Precision", "Recall")


