from tensorflow.keras.models import load_model
import numpy as np

model_high = load_model("Your model path")
model_low = load_model("Your model path")

_input = np.array([62900])

highest_price = model_high.predict(_input)
lowest_price = model_low.predict(_input)

print(highest_price, lowest_price)
