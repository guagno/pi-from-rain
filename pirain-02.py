import numpy as np

Nmeas = 1_000 # how many global measures?
Nbin = 1_000 # how many local measures in a bin?
rng = np.random.default_rng() # default random number generator
pirain = [] # create an empty list to store result for each imeas
for imeas in range(Nmeas):
  r2 = rng.random(Nbin)**2 + rng.random(Nbin)**2
  pirain.append(4*np.count_nonzero(r2 <= 1)/Nbin)

pirain = np.array(pirain)
print(f"With {Nmeas} rain seasons and {Nbin} rain drops per season...")
print(f"pi = {pirain.mean():7.5f} +/- {pirain.std()/np.sqrt(Nbin-1):7.5f}")
