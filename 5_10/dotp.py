if __name__ == "__main__":

    # Numero de elementos
    n = 679477248

    # Variables de entrada
    a = range(1,n+1)
    b = range(1,n+1)

    # Variable intermedia
    i = 0

    # Variable de salida
    y = 0.0

    for i in range(0, len(a)):
        y = y + a[i]*b[i]

    print(y)
