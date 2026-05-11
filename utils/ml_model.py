from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2

model = load_model("model/keras_model.h5", compile=False)
class_names = open("model/labels.txt", "r").readlines()


def classify_frame(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    image = Image.fromarray(frame_rgb)
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

    image_array = np.asarray(image)
    normalized = (image_array.astype(np.float32) / 127.5) - 1

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized

    prediction = model.predict(data, verbose=0)

    index = np.argmax(prediction)

    return class_names[index].strip()
