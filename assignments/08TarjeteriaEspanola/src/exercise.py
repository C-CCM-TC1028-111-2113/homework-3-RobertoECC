def papel(p):
    tarjetas = p*12
    return (tarjetas)

def plumones(pm):
    tarjetas = pm*35
    return (tarjetas)

def main():
    
    #escribe tu código abajo de esta línea
    pass

pliegos = int(input("Dame la cantidad de pliegos de papel albanene: "))
plumn = int(input("Dame la cantidad de plumones: "))

if papel(pliegos) > plumones(plumn):
    print("El número máximo de tarjetas que se pueden hacer es: ", plumones(plumn))
elif papel(pliegos) < plumones(plumn):
    print("El número máximo de tarjetas que se pueden hacer es: ", papel(pliegos))

if __name__=='__main__':
    main()
