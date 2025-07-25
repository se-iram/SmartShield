import tensorflow as tf
import numpy as np
import os

# Load the SavedModel
model = tf.saved_model.load('model/siamesemodel')  # Adjust path if needed


def preprocess(file_path):
    byte_img = tf.io.read_file(file_path)
    img = tf.io.decode_jpeg(byte_img)
    img = tf.image.resize(img, (105, 105))  # Match original training shape
    img = img / 255.0
    return img


def verify(input_img_path, anchor_dir='anchor'):
    input_img = preprocess(input_img_path)
    results = []

    for filename in os.listdir(anchor_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            anchor_path = os.path.join(anchor_dir, filename)
            anchor_img = preprocess(anchor_path)

            # Run model
            result = model.serve([tf.expand_dims(input_img, 0), tf.expand_dims(anchor_img, 0)])
            results.append(result.numpy()[0][0])

    avg_score = np.mean(results)
    return avg_score
