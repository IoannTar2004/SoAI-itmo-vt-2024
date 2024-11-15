import pandas as pd
from lab5.decision_tree import DecisionTree
import matplotlib.pyplot as plt


def lab5():
    plt.subplots_adjust(hspace=0.5)

    df = pd.read_csv('lab5/grades.csv', delimiter=',')
    frac = 0.95
    df_ed = df.iloc[:int(len(df) * frac)]
    df_test = df.iloc[int(len(df) * frac):]
    tree = DecisionTree(plt, df_ed.drop(columns=['STUDENT ID', 'COURSE ID']), 'GRADE')
    tree.set_threshold(4)

    tree.build_tree()
    tree.print_tree()
    estimations = tree.class_estimation(df_test.drop(columns=['STUDENT ID', 'COURSE ID']))
    print()

    accuracy = (estimations["TP"] + estimations["TN"]) / len(df_test)
    precision = estimations["TP"] / (estimations["TP"] + estimations["FP"])
    recall = estimations["TP"] / (estimations["TP"] + estimations["FN"])
    print("Accuracy = ", accuracy)
    print("Precision = ", precision)
    print("Recall = ", recall, "\n")

    fpr = estimations["FP"] / (estimations["FP"] + estimations["TN"])
    area_roc = tree.draw_roc(fpr, recall)
    area_pr = tree.draw_pr(precision, recall)

    print("Area AUC-ROC: ", area_roc)
    print("Area AUC-PR: ", area_pr)


def lab5_test():
    df = pd.read_csv('lab5/test.csv', delimiter=';')
    tree = DecisionTree(None, df.drop(columns=['id']), 'Class')
    tree.set_threshold(1)

    tree.build_tree()
    tree.print_tree()
    features = {'Outlook': 'Sunny', 'Temperature': 'Hot'}
    print(tree.get_class(features, "Success", "Not Success"))
