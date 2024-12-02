import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from lab6.log_regression import LogRegression


def draw_bars(log):
    log.draw_bar('Pregnancies', ('месяц', 'кол-во'), (3, 3, 1))
    log.draw_bar('Glucose', ('уровень', 'кол-во'), (3, 3, 2))
    log.draw_bar('BloodPressure', ('давление', 'count'), (3, 3, 3))
    log.draw_bar('SkinThickness', ('толщина', 'count'), (3, 3, 4))
    log.draw_bar('Insulin', ('уровень', 'count'), (3, 3, 5))
    log.draw_bar('BMI', ('индекс', 'count'), (3, 3, 6))
    log.draw_bar('Pedigree', ('индекс', 'кол-во'), (3, 3, 7))
    log.draw_bar('Age', ('возраст', 'кол-во'), (3, 3, 8))
    log.plt.show()


def lab6():
    plt.subplots_adjust(hspace=0.5)
    df = pd.read_csv('lab4/diabetes.csv')
    target = 'Outcome'

    frac = 0.8
    log = LogRegression(plt, df.iloc[:int(len(df) * frac)], target)
    draw_bars(log)
    log.scaling()
    log.gradient_descent(0.01, 100)
    print(log.params)
    print(log.log_loss())

    df_test = df.drop(columns=[target]).iloc[int(len(df) * frac):]
    estimations = log.class_estimation(df_test, df, target)

    accuracy = (estimations["TP"] + estimations["TN"]) / len(df_test)
    precision = estimations["TP"] / (estimations["TP"] + estimations["FP"])
    recall = estimations["TP"] / (estimations["TP"] + estimations["FN"])
    f1_score = 2 * (precision * recall) / (precision + recall)
    print("Accuracy = ", accuracy)
    print("Precision = ", precision)
    print("Recall = ", recall)
    print("F1 Score = ", f1_score, "\n")

