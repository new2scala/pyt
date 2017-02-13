
import math
import random

b = 'boy'
g = 'girl'
def rand_kid():
    return random.choice([b, g])

both_girls = 0
older_girl = 0
either_girl = 0

#random.seed(0)

for _ in range(10000):
    younger = rand_kid()
    older = rand_kid()

    if older == g:
        older_girl += 1
    if older == g and younger == g:
        both_girls += 1
    if older == g or younger == g:
        either_girl += 1

print('P(Both|Older) = %f' % (both_girls/older_girl))
print('P(Both|Older) = %f' % (both_girls/either_girl))

'''
Bayes theorem
  P(E|F) = P(E,F)/P(F) = P(F|E)P(E) / P(F) = P(F|E)P(E) / (P(F|E)P(E) + P(F|^E)P(^E))
  P(D) = 1/10000 -- 1 out of 10000 people has the disease
  P(T) = 99/100  -- test accuracy for the disease is .99
  Now if someone is tested positive, the prob of his having the disease P(D|T) is:
  P(D|T) = P(T|D)P(D) / (P(T|D)P(D) + P(T|^D)P(^D))
'''

prob_d = 0.0001
prob_xd = 0.9999
prob_t_xd = 0.01
prob_t_d = 0.99

prob_d_t = prob_t_d*prob_d / (prob_t_d*prob_d + prob_t_xd*prob_xd)
print(prob_d_t)

#page 91
def normal_pdf(x, mu=0, sigma=1):
    sqrt_2pi = math.sqrt(2*math.pi)
    ex = math.exp(-(x-mu)**2 / 2 / sigma**2)
    return ex / (sqrt_2pi*sigma)

def trans(x, func, *args, **kwargs):
    return func(x, *args, **kwargs)

import matplotlib.pyplot as plt
def plot(v, func):
    l01, = plt.plot(v, [trans(x, func) for x in xs], '-', label='mu=0,sigma=1')
    l02, = plt.plot(v, [trans(x, func, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
    l005, = plt.plot(v, [trans(x, func, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
    l_11, = plt.plot(v, [trans(x, func, mu=-1, sigma=1) for x in xs], '-.', label='mu=-1,sigma=1')
    plt.legend(handles=[l01, l02, l005, l_11])
    plt.show()

xs = [x/10 for x in range(-50, 50)]
#plot(xs, normal_pdf)

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf( (x-mu) / math.sqrt(2) / sigma)) / 2
#plot(xs, normal_cdf)
'''
xs = [x/10 for x in range(-50, 50)]

import matplotlib.pyplot as plt
l01, = plt.plot(xs, [normal_cdf(x) for x in xs], '-', label='mu=0,sigma=1')
l02, = plt.plot(xs, [normal_cdf(x,sigma=2) for x in xs], '--', label='mu=0,sigma=2')
l005, = plt.plot(xs, [normal_cdf(x,sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
l_11, = plt.plot(xs, [normal_cdf(x,mu=-1,sigma=1) for x in xs], '-.', label='mu=-1,sigma=1')
plt.legend(handles=[l01, l02, l005, l_11])
plt.show()
'''

def inv_normal_cdf(p, mu=0, sigma=1, tolerance=1e-6):
    low_x, low_p = -16, 0
    high_x, high_p = 16, 0

    while high_x-low_x > tolerance:
        mid_x = (high_x+low_x)/2
        mid_p = normal_cdf(mid_x)
        if (mid_p < p):
            low_x = mid_x
        elif (mid_p > p):
            high_x = mid_x
        else:
            break
    return mid_x

print(inv_normal_cdf(0.8))
# page 96

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

from collections import Counter
def make_hist(p, n, num_points):
    # random generated data
    d = [ binomial(n, p) for _ in range(num_points) ]
    histogram = Counter(d)
    xs = [x-0.4 for x in histogram.keys()]
    ys = [y/num_points for y in histogram.values()]
    plt.bar(xs, ys, 0.8, color='0.75')

    # theoretical value
    mu = p*n
    sigma = math.sqrt(n*p*(1-p))
    xs = range(min(d), max(d)+1)
    plt.plot(xs, [normal_pdf(x, mu=mu, sigma=sigma) for x in xs])
    plt.show()

make_hist(0.75, 100, 10000)
