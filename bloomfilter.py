import hashlib as hl
import numpy as np
import random as r

class BloomFilter: # n es tamano y k es para hashes
    def __init__(self,n,k):
        self.n = n
        self.k = k
        self.bloomArr = np.array([0 for i in range(n)], dtype='bool')
        self.cont = 0
        

    def hashes(self,cadena,k,n):
        numBitsHash = int(np.ceil(np.log2(n)))
        caracHash = int(np.ceil(numBitsHash/4)) # bits
        numMD5 = int(np.ceil((caracHash * k) / 32)) #
        res = []
        dHasheado = hl.md5(cadena.encode('utf-8')).hexdigest()
        for i in range(numMD5-1):
            dHasheado += hl.md5(dHasheado.encode('utf-8')).hexdigest()
        for i in range(0,k*caracHash,caracHash):
            res += [int(dHasheado[i:i+caracHash],16)%n]
        return res
    
    def inserta(self,dato):
        listHash = self.hashes(dato, self.k, self.n)
        for i in listHash:
            self.bloomArr[i] = True
        self.cont += 1

    def busca(self,dato):
        posiciones = self.hashes(dato, self.k,self.n)
        res = True
        for i in posiciones:
            res = res and self.bloomArr[i]
        return res
