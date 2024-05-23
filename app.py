# Import Dependencies
import os
import io
import numpy as np
import tensorflow as tf
from PIL import Image
from keras.models import load_model
from keras.preprocessing import image
from flask import Flask, render_template, jsonify, request


# Initializing Flask Application
app = Flask(__name__, template_folder='template')
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Initializing AI Model
classifier = (os.path.join(os.getcwd(),'model','BTC Model.h5'))
model = load_model(classifier)
model.load_weights(os.path.join(os.getcwd(),'model', 'BTC Weights.h5'))

# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Classification page
@app.route('/classify')
def classify():
    return render_template('classify.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        class_labels = ['Astrocytoma 😔','Glioma 😔','Meningioma 😔','Neurocytoma 😔','Normal 😃','Pituitary 😔']
        img = request.files['file'].read()
        img = Image.open(io.BytesIO(img))

        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        predictions = model.predict(img_array)[0]
        pred_index = np.argmax(predictions)
        predicted_class = class_labels[pred_index]
        prediction_probability = predictions[pred_index] * 100

        print(f'Predicted Class: {predicted_class}')
        print(f'Predicted Probability: {prediction_probability:.2f}%')

        return jsonify({
            'Predicted Class': predicted_class,
            'Prediction Probability': f'{prediction_probability:.2f}%'
        })

        

# Running the flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)