import pandas as pd
from lab5.decision_tree import DecisionTree


def lab5():
    df = pd.read_csv('lab5/grades.csv', delimiter=',')
    tree = DecisionTree(None, df.drop(columns=['STUDENT ID', 'COURSE ID']), 'GRADE')
    tree.set_threshold(4)

    tree.build_tree()
    tree.print_tree()


def lab5_test():
    df = pd.read_csv('lab5/test.csv', delimiter=';')
    tree = DecisionTree(None, df.drop(columns=['id']), 'Class')
    tree.set_threshold(1)

    tree.build_tree()
    tree.print_tree()
