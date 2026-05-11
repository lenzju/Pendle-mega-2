import cv2
from utils.ml_model import classify_frame
import numpy as np


def calculate_physics(video_path, length):
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)

    left_frames = []
    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        state = classify_frame(frame)

        if "Links" in state:
            left_frames.append(frame_idx)

        frame_idx += 1

    cap.release()

    # doppelte Erkennung verhindern
    filtered = []

    for f in left_frames:
        if not filtered or f - filtered[-1] > fps:
            filtered.append(f)

    if len(filtered) < 2:
        return 0, 0, 0

    # Zeit einer Periode
    T = (filtered[1] - filtered[0]) / fps

    # Frequenz
    freq = 1 / T

    # Erdbeschleunigung
    g = (4 * np.pi**2 * length) / (T**2)

    return T, freq, g
