
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
