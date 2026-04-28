import numpy as np
from scipy.signal import find_peaks

vx = np.gradient(x, times)
vy = np.gradient(y, times)

v = np.sqrt(vx**2 + vy**2)
def analyze_motion(times, positions, length):
    # Peaks finden (Maxima der Bewegung)
    peaks, _ = find_peaks(positions)

    peak_times = times[peaks]

    # Periodendauer berechnen
    periods = np.diff(peak_times)

    if len(periods) == 0:
        return 0, 0, 0

    T = np.mean(periods)
    f = 1 / T

    # g berechnen
    g = (4 * np.pi**2 * length) / (T**2)

    return T, f, g
