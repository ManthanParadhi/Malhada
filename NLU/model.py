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

max_sent = max([len(bytes(x.encode('utf-8'))) for x in inputs])
# create data set matrics with zero's
input_data = np.zeros((len(inputs), max_sent, 256), dtype="float32")

for i, inp in enumerate(inputs):
    for k, ch in enumerate(bytes(inp.encode("utf-8"))):
        input_data[i, k, int(ch)] = 1.0


labels = set(outputs)
fwrite = open('NLU\entities.txt', 'w', encoding='utf-8')
for label in labels:
    fwrite.write(label + '\n')
fwrite.close()

labels = open('NLU\entities.txt', 'r', encoding='utf-8').read().split('\n')

lbl2idx = {}
idx2lbl = {}

for k, label in enumerate(labels):
    lbl2idx[label] = k
    idx2lbl[k] = label

output_data = []
for output in outputs:
    output_data.append(lbl2idx[output])

output_data = to_categorical(output_data, len(labels))

model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(labels), activation='softmax'))

model.compile(optimizer="adam",
              loss="categorical_crossentropy", metrics=["acc"])

model.fit(input_data, output_data, epochs=2048)
model.save('NLU\model.5')

# classify any given text


def classify(text):
    x = np.zeros((1, max_sent, 256), dtype="float32")
    for k, ch in enumerate(bytes(text.encode("utf-8"))):
        x[0, k, int(ch)] = 1.0
    out = model.predict(x)
    idx = out.argmax()

    #print("text: '{}' is classified as '{}'".format(text, idx2lbl[idx]))
    return idx2lbl[idx]


'''if __name__ == '__main__':
    while True:
        text = input("Enter some text:")
        print(classify(text))
'''
