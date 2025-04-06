import Poblacion as pob

print("Escribe como numero entero el porcentaje de error")
porcentajeError = int(input())
print("Escribe el numero de datos que recibiran los bloomfilters")
nDatos = int(input())
print("Escribe el numero de generaciones")
nGen = int(input())

AG = pob.Poblacion(20,porcentajeError)
res = AG.comenzarAlgoritmo(nDatos,nGen)
print(res)


