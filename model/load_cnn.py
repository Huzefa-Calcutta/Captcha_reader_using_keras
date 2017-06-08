from keras.models import Graph
from keras.layers.core import Dense, Flatten, Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D

def save_model_arch():
    graph = Graph()
    graph.add_input(name='input', input_shape=(3, 40, 40))
    graph.add_node(Convolution2D(32, 9, 9, activation='relu'), name='conv1', input='input')
    graph.add_node(Convolution2D(32, 9, 9, activation='relu'), name='conv2', input='conv1')
    graph.add_node(MaxPooling2D(pool_size=(2, 2)), name='pool', input='conv2')
    graph.add_node(Dropout(0.25), name='drop', input='pool')
    graph.add_node(Flatten(), name='flatten', input='drop')
    graph.add_node(Dense(640, activation='relu'), name='ip', input='flatten')
    graph.add_node(Dropout(0.5), name='drop_out', input='ip')
    graph.add_node(Dense(19, activation='softmax'), name='result', input='drop_out')

    graph.add_output(name='out', input='result')

    print '... compiling'
    graph.compile(
        optimizer='adadelta',
        loss={
            'out': 'categorical_crossentropy',
        }
    )

    graph_json = graph.to_json()
    return graph_json