from GGH import *

# генерація ключів для двох абонентів
Alice = GGH(10)
Alice.CryptGenKey()
Bob   = GGH(10)
Bob.CryptGenKey()

# виділення публічних ключів абонентів
pub_Alice = Alice.CryptGetUserKey()
pub_Bob   = Bob.CryptGetUserKey()

# Боб шифрує повідомлення для Аліси:
m = np.random.randint(-100, 100, pub_Alice.dim)
c = pub_Alice.CryptEncrypt(m)

#Аліса розшифровує повідомлення від Боба:
M = Alice.CryptDecrypt(c)

#перевірка коректності:
if np.all(M == m):
    print('received')

# Аліса шифрує повідомлення для Боба:
m = np.random.randint(-100, 100, pub_Bob.dim)
c = pub_Bob.CryptEncrypt(m)

#Аліса розшифровує повідомлення від Боба:
M = Bob.CryptDecrypt(c)

#перевірка коректності:
if np.all(M == m):
    print('received')
