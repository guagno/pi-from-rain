import numpy as np

N = 10_000 # how many random numbers?
rng = np.random.default_rng() # default random number generator
r2 = rng.random(N)**2 + rng.random(N)**2
pirain = 4*np.count_nonzero(r2 <= 1)/N
print(f"With {N} rain drops...")
print(f"pi = {pirain:7.5f}   (relative error: {abs(np.pi-pirain)/np.pi:7.5f})")
