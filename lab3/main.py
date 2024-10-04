import pandas as pd
import matplotlib.pyplot as plt
from linear_regression import Stat

if __name__ == '__main__':
    plt.figure(1)
    plt.subplots_adjust(hspace=0.3)

    df = pd.read_csv("D:\\Downloads\\Student_Performance.csv", sep=';')
    stat = Stat(plt, df)
    stat.draw_bar('Hours Studied', ('hours', 'count'), (2, 3, 1))
    stat.draw_bar('Previous Scores', ('scores', 'count'), (2, 3, 2))
    stat.draw_bar('Extracurricular Activities', ('activity', 'count'), (2, 3, 3))
    stat.draw_bar('Sleep Hours', ('hours', 'count'), (2, 3, 4))
    stat.draw_bar('Sample Question Papers Practiced', ('papers', 'count'), (2, 3, 5))
    stat.draw_bar('Performance Index', ('index', 'count'), (2, 3, 6))
    plt.show()

    ratios1 = stat.approximate(['Extracurricular Activities', 'Sleep Hours'], 'Performance Index', 0.8)
    ratios2 = stat.approximate(['Hours Studied', 'Previous Scores', 'Extracurricular Activities',
                      'Sleep Hours', 'Sample Question Papers Practiced'], 'Performance Index', 0.8)
    ratios3 = stat.approximate(['Hours Studied'], 'Performance Index', 0.8)

    r1 = stat.getDeterminantRatio(ratios1, ['Extracurricular Activities', 'Sleep Hours'], 'Performance Index', 0.2)
    r2 = stat.getDeterminantRatio(ratios2, ['Hours Studied', 'Previous Scores', 'Extracurricular Activities',
                      'Sleep Hours', 'Sample Question Papers Practiced'], 'Performance Index', 0.2)
    r3 = stat.getDeterminantRatio(ratios3, ['Hours Studied'], 'Performance Index', 0.2)

    df['Synthetic feature'] = 24 - (df['Hours Studied'] + df['Sleep Hours'])
    r4 = stat.getDeterminantRatio(ratios1, ['Extracurricular Activities', 'Synthetic feature'], 'Performance Index', 0.2)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
