from time import time
from tensorflow.keras.models import load_model
import numpy as np
#from model import max_sent


labels = open('NLU\entities.txt', 'r', encoding='utf-8').read().split('\n')
model = load_model('NLU\model.5')
lbl2idx = {}
idx2lbl = {}

for k, label in enumerate(labels):
    lbl2idx[label] = k
    idx2lbl[k] = label
# classify any given text


def classify(text):
    x = np.zeros((1, 27, 256), dtype="float32")
    if(len(x) > 48):
        x = x[:48]
    for k, ch in enumerate(bytes(text.encode("utf-8"))):
        x[0, k, int(ch)] = 1.0
    out = model.predict(x)
    idx = out.argmax()

    #print("text: '{}' is classified as '{}'".format(text, idx2lbl[idx]))
    return idx2lbl[idx]


if __name__ == '__main__':
    while True:
        text = input("Enter some text:")
        print(classify(text))
