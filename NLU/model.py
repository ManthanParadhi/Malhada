import yaml
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical

data = yaml.safe_load(open('nlu\\train.yml').read())
inputs, outputs = [], []
for command in data['commands']:
    inputs.append(command['input'])
    outputs.append('{}\{}'.format(command['entity'], command['action']))

max_sent = max([len(x) for x in inputs])
# create data set matrics with zero's
input_data = np.zeros((len(inputs), max_sent, 256), dtype="float32")

for i, inp in enumerate(inputs):
    for k, ch in enumerate(bytes(inp.encode("utf-8"))):
        input_data[i, k, int(ch)] = 1.0
