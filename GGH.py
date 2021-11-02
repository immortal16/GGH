import numpy as np


class System():

    def __init__(self, dim, bound):
        self.dim = dim
        self.bound = bound
        self.R = self.GEN_rand_basis()
        self.U = self.GEN_unimodular()
        self.B = self.U @ self.R

    def GEN_rand_basis(self):
        k = np.round(np.sqrt(self.dim) * self.bound)
        return (k * np.identity(self.dim)).astype('int64') + np.random.randint(-self.bound, self.bound,
                                                                               size=(self.dim, self.dim)).astype(
            'int64')

    def GEN_unimodular(self):
        l = np.tril(np.random.randint(-1, 1, size=(self.dim, self.dim))).astype('int64')
        u = np.triu(np.random.randint(-1, 1, size=(self.dim, self.dim))).astype('int64')

        for i in range(self.dim):
            l[i, i] = u[i, i] = 1

        return (l @ u).astype('int64')

    def UT_check_noise_accuracy(self, e):
        return True if np.sum(np.round(e @ np.linalg.inv(self.R))) == 0. else False

    '''
    def UT_Babai_rounding(self, w):
        L = np.round(np.linalg.solve(self.R, w))
        return L @ self.R
    '''

    def PKE_encrypt(self, m, e):
        return (m @ self.B).astype('int64') + e.astype('int64')

    def PKE_decrypt(self, c):
        return ((np.round(c @ np.linalg.inv(self.R))).astype('int64') @ np.linalg.inv(self.U).astype('int64')).astype(
            'int64')
