import argparse
import numpy as np

from azureml.core import Run


parser = argparse.ArgumentParser()
parser.add_argument('--training_data')
parser.add_argument('--max_epochs', type=int, default=0.2)
parser.add_argument('--learning_rate', type=float, default=0.1)
parser.add_argument('--subsample', type=float)
args = parser.parse_args()
training_data = args.training_data
max_epochs = args.max_epochs
learning_rate = args.learning_rate
subsample = args.subsample
print('training_data: ', training_data)
print('max_epochs: ', max_epochs)
print('learning_rate: ', learning_rate)
print('subsample: ', subsample)

# start an Azure ML run
run = Run.get_context()
# Log metric
run.log('accuracy', np.float(learning_rate * max_epochs))
run.log('accuracy', np.float(learning_rate * max_epochs / 2))
run.log('accuracy', np.float(learning_rate * max_epochs / 3))
run.log('precision', np.float(learning_rate * max_epochs))
run.log('precision', np.float(learning_rate * max_epochs / 2))
run.log('precision', np.float(learning_rate * max_epochs / 3))

with open('outputs/saved_model.txt', 'w') as fout:
    fout.write(str(np.float(learning_rate * max_epochs / 3)))
