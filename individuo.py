import bloomfilter as bF
import random as r
import string

class individuo:
    def __init__(self,tamBloom,numHashes, conjunto):
        self.bloonFilter = bF.BloomFilter(tamBloom,numHashes)
        self.falsosPos = 0
        self.porcentaje = 0.0
        self.cromosoma = tamBloom
        self.conjunto = set(conjunto)
    
    def generaIndividuo(self):
        for e in self.conjunto:
            self.bloonFilter.inserta(e)
    
    def calculaPorcentaje(self):
        if self.porcentaje == 0:
            for i in range(len(self.conjunto)):
                s = self.creadorCadenas()
                if self.bloonFilter.busca(s) and s not in self.conjunto:
                    self.falsosPos+= 1
            if self.falsosPos != 0:
                self.porcentaje = float((self.falsosPos / 100) * len(self.conjunto))
    
    def creadorCadenas(self):
        e = r.choice(string.ascii_letters)
        for k in range(r.randint(1,99)):
                e += r.choice(string.ascii_letters)
        return e
    
    def getPorcentaje(self):
         return self.porcentaje
    
    def getCromosoma(self):
         return self.cromosoma