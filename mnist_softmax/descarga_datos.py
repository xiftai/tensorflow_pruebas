# Descarga los datasets MNIST de la ruta correspondiente
# y los instala en MNIST_DATA

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)