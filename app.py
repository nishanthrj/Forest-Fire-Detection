import cv2
import numpy as np

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model



model = load_model("./model.h5")

video = cv2.VideoCapture("")
