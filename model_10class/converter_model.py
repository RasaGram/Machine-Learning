import tensorflow as tf
from tensorflow.keras.models import load_model

# Load your trained Keras model
model = load_model('model (8).h5')

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Optimize for size and speed
tflite_model = converter.convert()

# Save the TensorFlow Lite model
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

print('TensorFlow Lite model conversion complete.')
