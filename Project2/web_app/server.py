from flask import Flask, render_template, request, send_from_directory
import os
import urllib
from keras.models import load_model
from keras.applications import resnet50, mobilenet, vgg19
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
import cv2
import numpy as np

app = Flask(__name__)

PORT = '8888'
UPLOAD = 'uploads'

@app.route('/')
def index():
    return render_template("index.html",
                           title='Image Classification Demo')


@app.route('/download', methods=['POST'])
def download_image():
    address = request.form['address']
    modelname = request.form['modelname']
    filename = os.path.join(UPLOAD, address.split('/')[-1])
    return predict(filename)


@app.route('/upload', methods=['POST'])
def upload_image():
    f = request.files['image']
    filename = os.path.join(UPLOAD, f.filename)
    f.save(filename)
    return predict(filename)


@app.route('/' + UPLOAD + '/<path:path>')
def serve_files(path):
    return send_from_directory(UPLOAD, path)


def predict(filename):
    img = cv2.imread(filename)
    img = cv2.resize(img, (224,224))[...,::-1]
    img = np.expand_dims(img, axis=0).astype(np.float32)
    x_batch = preprocess_input(img)
    pred = model.predict(x_batch)
    decode_result = decode_predictions(pred)[0]
    result = []
    for r in decode_result:
        result.append({'name':r[1], 'prob':r[2]*100})

    return render_template('predict.html',
                           filename=filename,
                           predictions=result)


if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    model = resnet50.ResNet50(include_top=True, weights='imagenet')
    app.run(host='0.0.0.0', port=PORT)