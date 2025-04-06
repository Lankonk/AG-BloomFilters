import individuo as indv
import random as r
import string
import numpy as np

class Poblacion:
    def __init__(self, numHashes,pAceptable):
        self.Pob = []
        self.numHashes = numHashes
        self.pAceptable = pAceptable
        self.conj = set()
        self.cardinalidad = 0
        self.MejorIndividuo = None
    
    def comenzarAlgoritmo(self, numE, numGen):
        for i in range(numE):
            self.creadorCadenas()
        self.generaPrimPob(1000)
        self.calcYordenaAdecuacion()
        for i in range(numGen):
            self.cruza()
            self.Muta()
            self.Pob.sort(key=lambda indv: indv.getCromosoma())
            if self.Pob[0].getCromosoma() < self.MejorIndividuo.getCromosoma():
                self.MejorIndividuo = self.Pob[0]
        return "El size minimo es de "+ str(self.MejorIndividuo.getCromosoma()) + " con este porcentaje de falsos positivos "+ str(self.MejorIndividuo.getPorcentaje())

    def creadorCadenas(self):
        e = r.choice(string.ascii_letters)
        for k in range(r.randint(1,99)):
                e += r.choice(string.ascii_letters)
        self.conj.add(e)
        self.cardinalidad += 1
    
    def generaPrimPob(self, cantPob):
        for i in range(cantPob):
            indiv = indv.individuo(r.randint(1,(2**16)-1),self.numHashes, self.conj)
            indiv.generaIndividuo()
            indiv.calculaPorcentaje()
            self.Pob.append(indiv)
            if self.MejorIndividuo is None:
                self.MejorIndividuo = indiv
        
    
    def calcYordenaAdecuacion(self):
        if self.pAceptable != 0:
            self.pAceptable = float((self.pAceptable / 100) * self.cardinalidad)
        for org in self.Pob:
            if org.getPorcentaje() > self.pAceptable:
                self.Pob.remove(org)
        self.Pob.sort(key=lambda indv: indv.getCromosoma()) 
        if self.Pob[0].getCromosoma() < self.MejorIndividuo.getCromosoma():
            self.MejorIndividuo = self.Pob[0]
    
    def cruza(self):
        pobCruz = []
        pobCount = len(self.Pob)
        for i in range(pobCount//4):
            rIndice = r.randint(pobCount//2,pobCount-1)
            resta =(self.Pob[rIndice].getCromosoma() - self.Pob[i].getCromosoma()) //2
            if resta > 1:
                pobCruz.append(resta)
        del self.Pob[pobCount//2:]
        self.generaCruza(pobCruz)

    def Muta(self):
        rMut = r.randint(10,100)
        for i in range(rMut):
            ind = indv.individuo(r.randint(2,(2**16)-1),self.numHashes, self.conj)
            ind.generaIndividuo()
            ind.calculaPorcentaje()
            if ind.getPorcentaje() < self.pAceptable:
                self.Pob.append(ind)
    
    def generaCruza(self, pobList):
        for i in pobList:
            ind = indv.individuo(i,self.numHashes, self.conj)
            ind.generaIndividuo()
            ind.calculaPorcentaje()
            if ind.getPorcentaje() < self.pAceptable:
                self.Pob.append(ind)
