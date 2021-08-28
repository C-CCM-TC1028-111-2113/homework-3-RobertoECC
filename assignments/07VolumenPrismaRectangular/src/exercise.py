def vol(b, a, p):
    volumen= a*b*p
    return(volumen)

def main():
    #escribe tu código abajo de esta línea
    pass

base = float(input("Dame la base: "))
area = float(input("Dame la altura: "))
prof = float(input("Dame la profundidad: "))

print ("EL volumen del prisma es: ", vol(base, area, prof))

if __name__=='__main__':
    main()
