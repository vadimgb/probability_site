from sympy import Symbol, integrate
x = Symbol('x')
mu = integrate(x/(50-5), (x,5, 50))
print(f"mu={mu}={float(mu)}")
eX2 = integrate(x**2/(50-5), (x, 5, 50))
print(f"E(X^2) = {eX2}")
sigma2 = eX2-mu**2
print(f"sigma^2 = E(X^2) - E(X)^2 = {sigma2} = {float(sigma2)}") 
from scipy.stats import norm
print(1-norm.cdf(1.92))
