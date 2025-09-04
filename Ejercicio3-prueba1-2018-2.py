arch=open('dispositivos.txt','r')
linea=arch.readline().strip()
c=0
ins=""
cortar=""
segundo=0
while linea!="":
    c=c+1
    rojo=0
    amarillo=0
    negro=0
    parte=linea.split(",")
    num=int(parte[0])
    if num==3:
        print("Dispositivo "+str(c)+" tiene 3 cables")
        c1=parte[1]
        c2=parte[2]
        c3=parte[3]
        if c1.upper()=="ROJO":
            rojo+=1
        if c2.upper()=="ROJO":
            rojo+=1
        if c3.upper()=="ROJO":
            rojo+=1
        if rojo==0:
            print("Cortar el segundo cable ("+c2+")")
            segundo+=1
        elif c3.upper()=="BLANCO":
            print("Cortar el tercer cable ("+c3+")")
        elif c2.upper()=="AZUL" and c1.upper()=="AZUL":
            print("Cortar el segundo cable (Azul)")
            segundo+=1
        else:
            print("Cortar el tercer cable ("+c3+")")
    elif num==4:
        print("Dispositivo "+str(c)+" tiene 4 cables")
        c1=parte[1]
        c2=parte[2]
        c3=parte[3]
        c4=parte[4]
        if c1.upper()=="ROJO":
            rojo+=1
        if c2.upper()=="ROJO":
            rojo+=1
        if c3.upper()=="ROJO":
            rojo+=1
        if c4.upper()=="ROJO":
            rojo+=1
        if rojo>1:
            print("Cortar el cuarto cable ("+c4+")")
        elif c4.upper()=="AMARILLO" and rojo==0:
            print("Cortar el primer cable ("+c1+")")
        elif rojo==1:
            print("Cortar el segundo cable ("+c2+")")
            segundo+=1
        elif c2.upper()=="AMARILLO" and c3.upper()=="AMARILLO":
            print("Cortar el cuarto cable ("+c4+")")
        else:
            print("Cortar el tercer cable ("+c3+")")
    elif num==5:
        print("Dispositivo "+str(c)+" tiene 5 cables")
        c1=parte[1]
        c2=parte[2]
        c3=parte[3]
        c4=parte[4]
        c5=parte[5]
        if c1.upper()=="AMARILLO":
            amarillo+=1
        elif c1.upper()=="NEGRO":
            negro+=1
        if c2.upper()=="AMARILLO":
            amarillo+=1
        elif c2.upper()=="NEGRO":
            negro+=1
        if c3.upper()=="AMARILLO":
            amarillo+=1
        elif c3.upper()=="NEGRO":
            negro+=1
        if c4.upper()=="AMARILLO":
            amarillo+=1
        elif c4.upper()=="NEGRO":
            negro+=1
        if c5.upper()=="AMARILLO":
            amarillo+=1
        elif c5.upper()=="NEGRO":
            negro+=1
        if c5.upper()=="NEGRO":
            print("Cortar el cuarto cable ("+c4+")")
        elif c3.upper()=="ROJO"and amarillo>1:
            print("Cortar el tercer cable ("+c3+")")
        elif negro==0:
            print("Cortar el segundo cable ("+c2+")")
            segundo+=1
        else:
            print("Cortar el primer cable ("+c1+")")
    linea=arch.readline().strip()
print("Se analizaron",c,"dispositivos")
print("El cabel 2 se corto ",segundo," veces, en "+str(segundo*100/c)+"% del total")

        