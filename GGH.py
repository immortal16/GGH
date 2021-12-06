import numpy as np


class GGH:

    def __init__(self, dim):

        self.dim = dim

        self.R = None
        self.B = None
        self.U = None

        self.delta = None

    
    def __del__(self):

        return None


    def CryptGenKey(self):

        k = np.round(np.sqrt(self.dim) * 4)

        l = np.tril(np.random.randint(-1, 1, size = (self.dim, self.dim)))
        u = np.triu(np.random.randint(-1, 1, size = (self.dim, self.dim)))

        for i in range(self.dim):
            l[i, i] = u[i, i] = np.random.choice([1, -1])

        self.U = l @ u

        while True:
            self.R = k * np.identity(self.dim) + np.random.randint(-4, 4, size = (self.dim, self.dim))
            self.inv_R = self.inv(self.R)

            norms = []
            for i in range(self.dim):
                norms.append(self.L1(self.inv_R[i, :]))

            self.delta = int(np.floor(max(norms)))

            if self.delta >= 1 and self.HadamardRatio() > 0.8:
                break
        
        self.B = self.U @ self.R

    
    def CryptGetUserKey(self):

        pub = GGH(self.dim)

        pub.B = self.B
        pub.delta = self.delta

        return pub


    def CryptDestroyKey(self):

        return self.__del__()

    
    def CryptEncrypt(self, m):

        e = np.random.choice([-self.delta, self.delta], size = self.dim)
        return m @ self.B + e


    def CryptDecrypt(self, c):

        return np.round(c @ self.inv_R) @ self.inv(self.U)

    
    def HadamardRatio(self):

        ratio = np.abs(self.det(self.R))

        for i in range(self.dim):
            ratio /= self.L2(self.R[:, i])

        return pow(ratio, 1 / self.dim)


    L1 = staticmethod(lambda x: np.linalg.norm(x, 1))

    L2 = staticmethod(lambda x: np.linalg.norm(x, 2))

    inv = staticmethod(lambda x: np.linalg.inv(x))

    det = staticmethod(lambda x: np.linalg.det(x))
