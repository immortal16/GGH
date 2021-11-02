import numpy as np

from GGH import System

L1 = lambda x: np.linalg.norm(x, 1)
L2 = lambda x: np.linalg.norm(x, 2)
Linf = lambda x: np.max(np.absolute(x))
det = lambda x: np.linalg.det(x)

GGH = System(5, 5)

e = np.random.randint(-1, 1, GGH.dim)

while not GGH.UT_check_noise_accuracy(e):
    e = np.random.randint(-1, 1, GGH.dim)

m = np.random.randint(-100, 100, GGH.dim)
c = GGH.PKE_encrypt(m, e)
M = GGH.PKE_decrypt(c)

print(m)

print(M)

print(np.all(M.astype('int64') == m))