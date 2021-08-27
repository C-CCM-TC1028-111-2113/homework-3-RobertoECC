def bis(a):
    bisiesto = (a%4)
    return(bisiesto)

def main():
    #escribe tu código abajo de esta línea
    pass

año = int(input(""))
if bis(año)==0:
    print("True")
else: print("False")

if __name__=='__main__':
    main()
