import os, sys
import pandas as pd
import numpy as np
import json
import time
import flask
import numpy as np
import keras
from PIL import Image
from keras.models import Graph
from keras.layers.core import Dense, Flatten, Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import model.load_cnn as load_cnn
import model.load_weights as load_weights

from utils import prep_data

model_arc = load_cnn.save_model_arch()
model = keras.models.model_from_json(model_arc)


# Start Flask app
print('Starting Flask app')
app = flask.Flask(__name__)

# Provide image as an json input to the api to the  address http://localhost:5002/captcha_read
@app.route('/captcha_read', methods =['POST'])
def captcha_reco():
    pic = flask.request.files('imagefile', '')
    x = prep_data.get_data(pic)
    model_arc = m.load_cnn.save_model_arc()
    cnn_model = keras.models.model_from_json(model_arc)
    directory = sys.path.append(os.path.join(os.path.dirname(__file__), '..','model'))
    cnn_model_final = load_weights(cnn_model,directory)
    result = cnn_model_final.predict({'input': x})
    out = [np.argmax(result['out'][0]), np.argmax(result['out'][1]),
       np.argmax(result['out'][2]), np.argmax(result['out'][3]),
       np.argmax(result['out'][4])]
    r = [prep_data.asc_chr(i) for i in out]
    result_json = json.dump(dict(r), ensure_ascii= False)
    return flask.Response(result_json,mimetype='application/json')

if __name__ == '_main__':
    app.run(host="0.0.0.0", debug=True, port=5002, processes=True, use_reloader=True)
