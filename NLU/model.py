import yaml
import numpy as np

data = yaml.safe_load(open('nlu\\train.yml').read())
inputs, outputs = [], []
for command in data['commands']:
    inputs.append(command['input'])
    outputs.append('{}\{}'.format(command['entity'], command['action']))

print(inputs)
print(outputs)
