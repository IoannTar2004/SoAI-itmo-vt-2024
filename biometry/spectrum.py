import math

import numpy as np
import scipy.fft
from statsmodels.tsa.stattools import acf
from scipy import interpolate


class Spectrum:

    def __init__(self, plt, df):
        self.plt = plt
        self.plt.grid(True)
        self.intervals = df['cardio'].values
        self.time = np.cumsum(self.intervals) / 1000

    def pyplot_setup(self, xlabel, ylabel):
        self.plt.grid(True)
        self.plt.xlabel(xlabel)
        self.plt.ylabel(ylabel)

    def autocorrelogram(self, m):
        autocorr_values = acf(self.intervals, nlags=127)
        x = np.arange(0, 32, 0.25)
        self.plt.plot(x, autocorr_values, color='black')
        self.pyplot_setup("с", "r")
        self.plt.show()

    def scatterogram(self):
        low, high = -0.5, 3
        autocorr_values = acf(self.intervals, nlags=127)
        x = autocorr_values[:-1]
        y = autocorr_values[1:]
        self.plt.scatter(x, y, color='blue', s=10)
        self.plt.xlim(low, high)
        self.plt.ylim(low, high)
        self.plt.plot([low, high], [low, high], color='orange', linestyle='-')
        self.pyplot_setup("с", "с")
        self.plt.show()

    def draw_rhythmogram(self):
        x = np.arange(0, 300, 1)
        self.plt.plot(x, self.intervals, marker='o', color='black')
        self.pyplot_setup("Длительность измерений, с", "Кардиоинтервалы, мс")
        self.plt.show()

    # обычная числовая последовательность из измерений
    def draw_cardiointervalogram(self):
        self.plt.plot(self.time, self.intervals, marker='o', color='black')
        self.pyplot_setup("Длительность измерений, с", "Кардиоинтервалы, мс")
        self.plt.show()

    # кубическая интерполяция
    def cubic_interpolate(self):
        spline = interpolate.CubicSpline(self.time, self.intervals)
        x_new = np.arange(0, self.time[-1], 0.25)
        y_new = spline(x_new)

        self.pyplot_setup("Длительность измерений, с", "Кардиоинтервалы, мс")
        # self.plt.plot(x_new, y_new)
        # self.plt.show()

        return x_new, y_new

    # сглаживание интерполяционной функции с помощью окон
    def smooth_with_window(self, method, x, y):
        window = method(len(x))
        y_smoothed = y * window

        self.pyplot_setup("Длительность измерений, с", "Кардиоинтервалы, мс")
        # self.plt.plot(x, y_smoothed, color="red")
        # self.plt.show()

        return y_smoothed

    # дискретное преобразование Фурье
    def fft(self, y):
        frequencies = np.fft.fftfreq(len(y), 0.25)
        fft_values = np.fft.fft(y)
        return frequencies, fft_values

    # вычисление спектральной мощности
    def power(self, frequencies, fft_values):
        N = len(fft_values)
        powers = (np.abs(fft_values) ** 2 / N ** 2)
        vlf, lf, hf = [], [], []
        x1, x2, x3 = [], [], []

        for i in range(5, N // 8):
            if 0.015 <= frequencies[i] <= 0.04:
                x1.append(frequencies[i])
                vlf.append(powers[i])
            elif 0.04 <= frequencies[i] <= 0.15:
                x2.append(frequencies[i])
                lf.append(powers[i])
            else:
                x3.append(frequencies[i])
                hf.append(powers[i])
        x1.append(x2[0])
        x2.append(x3[0])
        vlf.append(lf[0])
        lf.append(hf[0])

        self.pyplot_setup("Частота", "Спектральная мощность")
        self.plt.plot(x1, vlf)
        self.plt.plot(x2, lf)
        self.plt.plot(x3, hf)
        self.plt.show()

        return powers

    # расчет мощности спектров в диапазоне
    def power_sum(self, powers, low, up):
        sum = 0
        for i in powers:
            if low < i <= up:
                sum += i
        return sum

    # расчёт индексов
    def indexes(self, hf, lf, vlf, index):
        indexes = {
            'ИЦ': (vlf + lf) / hf,
            'ИВВ': lf / hf,
            'ИАП': lf / vlf
        }
        return indexes[index]

    def regulation_type(self, vvi):
        if vvi < 0.5:
            return 'Ваготония'
        elif 0.5 <= vvi <= 2:
            return 'Нормотония'
        else:
            return 'Симпатикотония'