#!/usr/bin/env python3

import random
import os
import sys
import numpy as np

TEST = False
learnig_rate = 0.3
n = 40
train_count = 50
k = 50


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


# layers = [785, n, 1]ss
weights = [np.random.randn(784, n)/np.sqrt(784), np.random.randn(n, 10)/np.sqrt(n)]
# biases = [np.random.randn(n), np.random.randn()]


def feedforward(v):
    out = sigmoid(np.dot(v, weights[0]))
    out1 = sigmoid(np.dot(out, weights[1]))
    return (out, out1)


def backpropagation(batch, exp, eta):
    out, out1 = feedforward(batch)
    delta = 2*(out1-exp)*out1*(1-out1)  # 70x1
    weights[1] -= np.dot(out.transpose(), delta)*eta/k
    # biases[1] -= sum(delta)*eta/k
    delta = np.dot(delta, weights[1].transpose())  # 70xn
    delta *= out*(1-out)
    weights[0] -= np.dot(np.transpose(batch), delta)*eta/k


def train(vectors, exp):
    global learnig_rate
    for r in range(0, train_count):
        eta = learnig_rate
        # seed = random.randint(1, 1000000)
        # random.seed(seed)
        # random.shuffle(vectors)
        # random.seed(seed)
        # random.shuffle(exp)
        indices = np.arange(vectors.shape[0])
        np.random.shuffle(indices)
        # vectors = vectors[indices]
        # exp = exp[indices]
        vectors_shuffled = [vectors[i] for i in indices]
        exp_shuffled = [exp[i] for i in indices]
        batches = [vectors_shuffled[j:j+k] for j in range(0, len(vectors), k)]
        batches_exp = [exp_shuffled[j:j+k] for j in range(0, len(exp), k)]
        for v, e in zip(batches, batches_exp):
            backpropagation(v, e, eta)
            # eta *= 0.99
        # z = list(zip(vectors, exp))
        # random.shuffle(z)
        # vectors, exp = zip(*z)
        # batches = [vectors[j:j+k] for j in range(0, len(vectors), k)]
        # batches_exp = [exp[j:j+k] for j in range(0, len(exp), k)]
        # for v, e in zip(batches, batches_exp):
        #     backpropagation(v, e, eta)
        #     eta *= 0.99

def parse(filename):
    vectors = []
    expect = []
    f = open(filename, 'r')
    for line in f:
        w = []
        for i in line.split(','):
            w.append(float(i))
        exp = int(w[0])
        w = w[1:]
        expv = [0]*10
        expv[exp] = 1
        vectors.append(w)
        expect.append(expv)
    f.close()
    mean = np.mean(vectors)
    # std = np.sum(np.sqrt(np.mean(abs(vectors - mean)**2)))
    for v in vectors:
        for i in range(0, len(v)):
            v[i] -= mean
            v[i] /= 78.56748998339798
    # vectors = (vectors-mean)/np.std(vectors)
    return (vectors, expect)
    



spamtrain = sys.argv[1]
test = sys.argv[2]


vectors, expect = parse(spamtrain)
train(np.array(vectors), np.array(expect))

acc = 0
vectors, expect = parse(test)

size = 0
for v, exp in zip(vectors, expect):
    if TEST:
        # print(feedforward(v)[1], exp)
        size += 1
        if (np.argmax(feedforward(v)[1]) == np.argmax(exp)):
            acc += 1
    else:
        print(np.argmax(feedforward(v)[1]))
# print()

if TEST:
    print(acc, "/", size, acc/size)
    # print(weights[0])
    # print(weights[1])
    # print(biases)
