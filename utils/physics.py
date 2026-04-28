import numpy as np
from scipy.signal import find_peaks

def analyze_motion(times, positions, length):
    positions = np.array(positions)

    x = positions[:, 0]
    y = positions[:, 1]

    # Peaks über x (stabil)
    peaks, _ = find_peaks(x)

    peak_times = times[peaks]

    if len(peak_times) < 2:
        return 0, 0, 0

    periods = np.diff(peak_times)

    T = np.mean(periods)
    f = 1 / T

    g = (4 * np.pi**2 * length) / (T**2)

    return T, f, g
