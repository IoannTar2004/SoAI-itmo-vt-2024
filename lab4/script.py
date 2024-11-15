import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from lab4.kNN import KNN


def part1(knn):
    knn.draw_bar('Pregnancies', ('месяц', 'кол-во'), (3, 3, 1))
    knn.draw_bar('Glucose', ('уровень', 'кол-во'), (3, 3, 2))
    knn.draw_bar('BloodPressure', ('давление', 'count'), (3, 3, 3))
    knn.draw_bar('SkinThickness', ('толщина', 'count'), (3, 3, 4))
    knn.draw_bar('Insulin', ('уровень', 'count'), (3, 3, 5))
    knn.draw_bar('BMI', ('индекс', 'count'), (3, 3, 6))
    knn.draw_bar('Pedigree', ('индекс', 'кол-во'), (3, 3, 7))
    knn.draw_bar('Age', ('возраст', 'кол-во'), (3, 3, 8))
    knn.plt.show()


def part2(knn):
    fig = knn.plt.figure()
    ax1 = fig.add_subplot(131, projection='3d')
    knn.draw_3d_scatter(0.8, ('Pregnancies', 'Glucose', 'BloodPressure'), ax1)
    ax2 = fig.add_subplot(132, projection='3d')
    knn.draw_3d_scatter(0.8, ('SkinThickness', 'Insulin', 'BMI'), ax2)
    ax3 = fig.add_subplot(133, projection='3d')
    knn.draw_3d_scatter(0.8, ('Age', 'Insulin', 'BloodPressure'), ax3)
    knn.plt.show()


k = 10


def part3(knn, isRandom, test=None):
    if isRandom:
        random_length = np.random.randint(1, 9)
        selection = np.random.choice(list(knn.df.keys()), size=random_length, replace=False)
    else:
        selection = test
    sum_yes, sum_no = 0, 0
    yes, no = 0, 0

    for i in range(int(knn.df_len * 0.8), knn.df_len):
        if knn.df["Outcome"][i] == 1:
            yes += 1
        else:
            no += 1
        features = {}
        for j in selection:
            features[j] = knn.df[j][i]
        result = knn.knn_method(features, k)
        if result == 1:
            sum_yes += 1
        else:
            sum_no += 1

    print(f"\tk = {k}\n----------------")
    print(selection)
    print(f"[{yes, sum_yes}]")
    print(f"[{no, sum_no}]")


def lab4():
    plt.subplots_adjust(hspace=0.5)
    df = pd.read_csv('lab4/diabetes.csv')
    knn = KNN(plt, df)
    knn.scaling()

    # part1(knn)
    # part2(knn)
    part3(knn, True)
    part3(knn, False, {'Pregnancies', 'Glucose', 'BloodPressure'})