import math

def normal_approx_to_binomial(n, p):
    mu = p*n
    sigma = math.sqrt(p*(1-p)*n)
    return mu, sigma

from dsfs.ch6_prob import normal_cdf, inv_normal_cdf

def normal_prob_btw(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

def normal_lower_bound(prob, mu=0, sigma=1):
    return inv_normal_cdf(prob, mu, sigma)

def normal_2sided_bounds(prob, mu=0, sigma=1):
    tail_prob = (1-prob)/2
    lower = normal_lower_bound(tail_prob, mu, sigma)
    upper = normal_lower_bound(1-tail_prob, mu, sigma)
    return lower, upper

mu_0, sigma_0 = normal_approx_to_binomial(1000, 0.5)
print((mu_0, sigma_0))
mu_1, sigma_1 = normal_approx_to_binomial(1000, 0.55)
print((mu_1, sigma_1))

low, hi = normal_2sided_bounds(0.95, mu_0, sigma_0)
print(normal_2sided_bounds(0.95, mu_1, sigma_1))

t2_prob = normal_prob_btw(low, hi, mu_1, sigma_1)
print("t2 prob: %f" % t2_prob)

'''
to verify the prob of falling between low and hi is actually close to 95%
'''
import random
def flip_trial(num, low, hi):
    sum = 0
    for _ in range(num):
        sum += random.choice([0, 1])
    if (sum < low or sum > hi):
        return 0
    else:
        return 1

def verify_bound(total_trial, low, hi):
    inside = 0
    for _ in range(total_trial):
        inside += flip_trial(1000, low, hi)

    print("%d / %d" % (inside, total_trial))

#verify_bound(1000, low, hi)

def two_sided_p_value(x, mu=0, sigma=1):
    if x > mu:
        return 2*(1 - normal_cdf(x, mu, sigma))
    else:
        return 2*normal_cdf(x, mu, sigma)

def one_sided_p_value(x, mu=0, sigma=1):
    if x > mu:
        return (1 - normal_cdf(x, mu, sigma))
    else:
        return normal_cdf(x, mu, sigma)

print(two_sided_p_value(529.5, mu_0, sigma_0))
print(two_sided_p_value(531.5, mu_0, sigma_0))

print(one_sided_p_value(524.5, mu_0, sigma_0))
print(one_sided_p_value(526.5, mu_0, sigma_0))

