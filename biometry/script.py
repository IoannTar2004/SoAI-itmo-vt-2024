import pandas as pd
from matplotlib import pyplot as plt
from scipy import signal

from biometry.spectrum import Spectrum


def execute():
    df = pd.read_csv("D:\\Универ\\3 курс\\системы искусственного интеллекта\\biometry\\VSR_Rubej.csv", sep=';')
    plt.figure(figsize=(12, 6))
    spectrum = Spectrum(plt, df)
    x, y = spectrum.cubic_interpolate()
    y = spectrum.smooth_with_window(signal.windows.hann, x, y)
    frequencies, fft_values = spectrum.fft(y)
    powers = spectrum.power(frequencies, fft_values)

    hf = spectrum.power_sum(powers, 0.15, 0.4)
    lf = spectrum.power_sum(powers, 0.04, 0.15)
    vlf = spectrum.power_sum(powers, 0.015, 0.04)
    vvi = spectrum.indexes(hf, lf, vlf, "ИВВ")

    print("HF:", hf)
    print("LF:", lf)
    print("VLF:", vlf, "\n")

    print("ИВВ:", vvi)
    print("Тип регуляции вегетативной системы:", spectrum.regulation_type(vvi))
