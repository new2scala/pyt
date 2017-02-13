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

normal_2sided_bounds(0.95, mu_0, sigma_0)