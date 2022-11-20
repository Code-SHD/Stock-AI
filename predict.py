from tensorflow.keras.models import load_model
import numpy as np

model = load_model("E:\\Programming Projects\\Doing\\Stock AI\\Samsung Electron\\model\\2.hdf5")

_input = np.array([62900])

print(model.predict(_input))