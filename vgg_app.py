import os
import numpy as np

# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from tensorflow.keras.applications.vgg19 import VGG19
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
print(APP_ROOT)

# Define a flask app
app = Flask(__name__)
# model = VGG19(weights='imagenet')
# Model saved with Keras model.save()
MODEL_PATH = '/Users/aj/Downloads/vgg_1.h5'

# Load your trained model
model = load_model(MODEL_PATH)
#model._make_predict_function()          # Necessary



def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x)

    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index_vgg.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = APP_ROOT
        file_path = os.path.join(
            basepath, secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)

        # Process your result for human
        # pred_class = preds.argmax(axis=-1)            # Simple argmax
        pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
        result = str(pred_class[0][0][1])               # Convert to string
        return result
    return None



if __name__ == '__main__':
    app.run(debug=True)