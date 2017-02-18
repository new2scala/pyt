
import numpy as np

data = np.array([[2.7810836  , 2.550537003, 0],
                 [1.465489372, 2.362125076, 0],
                 [3.396561688, 4.400293529, 0],
                 [1.38807019 , 1.850220317, 0],
                 [3.06407232 , 3.005305973, 0],
                 [7.627531214, 2.759262235, 1],
                 [5.332441248, 2.088626775, 1],
                 [6.922596716, 1.77106367 , 1],
                 [8.675418651, -0.2420686549, 1],
                 [7.673756466, 3.508563011, 1]])

import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def pred(dr, coeff):
    x = np.dot(dr[:-1], coeff[:-1])
    return sigmoid(x)

def pred_err(dr, coeff):
    p = pred(dr, coeff)
    return p - dr[-1]

def squared_error(data, coeff):
    errs = [pred_err(data[i], coeff) for i in range(data.shape[0])]
    e = np.dot(errs, errs)
    return np.sum(e)

def precision(data, coeff):
    data_count = data.shape[0]
    preds = [1 if pred(data[i], coeff) > 0.5 else 0 for i in range(data_count)]
    correct = [1 if preds[i] == data[i,-1] else 0 for i in range(data_count)]
    return np.sum(correct) / data_count

#print(sigmoid(data[0]))
init_coeff = np.array([0.0, 0.0, 0.0])
print(pred(data[0,], init_coeff))

print(squared_error(data, init_coeff))

learning_rate = 0.3

'''
coeff update function
b = b + learning_rate * (y – pred) * prediction * (1 – pred) * x
'''

def coeff_upd(coeff, learning_rate, pred, expected, x):
    return [coeff[i] + learning_rate*(expected-pred) * pred * (1-pred) * x[i] for i, _ in enumerate(x)]

def coeff_upd_on_data(data, coeff, learning_rate):
    p = pred(coeff, data)
    return coeff_upd(coeff, learning_rate, p, data[-1], np.append(data[:-1], [1.0]))

coeff1 = coeff_upd_on_data(data[0,], init_coeff, learning_rate)
print(coeff1)

batch_size = 2
import random

random.seed(124)

# shuffer data and split into batches
def shuffle_and_split(data, batch_size):
    start_index = random.randint(0, data.shape[0]-1)
    shuffled = np.vstack([data[start_index:,:], data[:start_index,:]])
    #shuffled = np.random.shuffle(data)
    batch_count = data.shape[0]//batch_size
    return [shuffled[i*batch_size:(i+1)*batch_size] for i in range(batch_count)]

#test_shuffle = shuffle_and_split(data, batch_size)
#print(len(test_shuffle))
def coeff_sgd(data, coeff, epoch, batch_size, learning_rate):
    for i in range(epoch):
        shuffled = shuffle_and_split(data, batch_size)
        for b in shuffled:
            coeff1 = [coeff_upd_on_data(b[i], coeff, learning_rate) for i in range(batch_size)]
            #print(coeff1)
            coeff = np.mean(coeff1, axis=0)
            err = squared_error(data, coeff)
            prec = precision(data, coeff)
            print("Epoch: %d, error: %f, precision: %f" % (i, err, prec))
    return coeff


def coeff_sgd1(data, coeff, epoch, batch_size, learning_rate):
    for i in range(epoch):
        #shuffled = shuffle_and_split(data, batch_size)
        for b in data:
            coeff1 = coeff_upd_on_data(b, coeff, learning_rate)
            #print(coeff1)
            coeff = coeff1 #np.mean(coeff1, axis=0)
            err = squared_error(data, coeff)
            prec = precision(data, coeff)
            print("Epoch: %d, error: %f, precision: %f" % (i, err, prec))
    return coeff

result_coeff = coeff_sgd(data, init_coeff, 100, 5, 0.3)
print(result_coeff)