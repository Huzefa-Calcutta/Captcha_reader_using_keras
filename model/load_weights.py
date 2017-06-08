from keras.models import Graph
from keras.layers.core import Dense, Flatten, Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D
import h5py

def load_weights(models, directory):
    file_name = os.path.join(directory,'model_1.hdf5')
    return models.load_weights(file_name)