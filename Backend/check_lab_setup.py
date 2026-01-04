import tensorflow as tf
import keras
from scikeras.wrappers import KerasClassifier
import pydot

print(f"TensorFlow Version: {tf.__version__}")
print(f"Keras Version: {keras.__version__}")
print("SciKeras wrapper loaded successfully.")
print("Pydot loaded successfully.")

# Check if Keras sees a GPU (Likely '[]' on Windows, which is fine for this lab)
print("Physical Devices:", tf.config.list_physical_devices())