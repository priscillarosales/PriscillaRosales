# -*- coding: utf-8 -*-
import numpy as np

matriz = np.zeros((5,6))
listaEtapas = ['1', '2', '3', '4', '5']
listaCasas = ['A', 'B', 'C', 'D', 'E', 'F']
precioCasas = [65000000, 80000000, 75000000, 95000000, 120000000, 135000000]
arch = open('casas.txt', "r")
linea = arch.readline().strip()
while linea != "":
    partes = linea.split(",")
    etapa = partes[0]
    casasA = int(partes[1])
    casasB = int(partes[2])
    casasC = int(partes[3])
    casasD = int(partes[4])
    casasE = int(partes[5])
    casasF = int(partes[6])
    posEtapa = listaEtapas.index(etapa)
    matriz[posEtapa][0] = casasA
    matriz[posEtapa][1] = casasB
    matriz[posEtapa][2] = casasC
    matriz[posEtapa][3] = casasD
    matriz[posEtapa][4] = casasE
    matriz[posEtapa][5] = casasF
    
    linea = arch.readline().strip()
    
ingresoCasas = [0,0,0,0,0,0]
reservasRechazadas = 0
arch2 = open('reservas.txt', "r")
linea2 = arch2.readline().strip()
while linea2 != "":
    partes2 = linea2.split(",")
    valorPie = int(partes2[0])
    tipoCasa = partes2[1]
    etapaCasa = partes2[2]
    if (etapaCasa == "3" or etapaCasa == "5") and (tipoCasa == "E" or tipoCasa == "F"):
        reservasRechazadas +=1
    else:
        posCasa = listaCasas.index(tipoCasa)
        posEtapa = listaEtapas.index(etapaCasa)
        stockCasa = matriz[posEtapa][posCasa]
        if stockCasa > 0:
            precio = precioCasas[posCasa]
            ingresoPie = precio * (valorPie/100.0)
            ingresoCasas[posCasa] += ingresoPie
            matriz[posEtapa][posCasa]-=1
        else:
            reservasRechazadas +=1
    linea2 = arch2.readline().strip()

print("1) El (los) tipo de casa que menos ingreso generó es (son):")

menorIngreso = 99999999999999999
for valor in ingresoCasas:
    if valor < menorIngreso:
        menorIngreso = valor
for i in range(6):
    if ingresoCasas[i] == menorIngreso:
        print(listaCasas[i])
print("con un monto de $",menorIngreso)

print("2) Las casas que quedan disponible son: ")
for i in range(5):
    print("Etapa",listaEtapas[i])
    for j in range(6):
        stockCasa = matriz[i][j]
        if stockCasa > 0:
            print("Tipo",listaCasas[j],stockCasa,"casas")

print("3) La cantidad de reservas rechazadas es",reservasRechazadas)








