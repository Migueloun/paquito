import multiprocessing as mp

def producto_punto_parcial(a_q, b_q, y_q):
    # Extraer los arreglos de la fila
    a = a_q.get()
    b = b_q.get()

    y = 0.0

    for i in range(0, len(a)):
        y = y + a[i]*b[i]

    y_q.put(y)

if __name__ == "__main__":
    # Número de elementos
    n = 679477248
    #n = 12
    # Variables de entrada
    a = range(1, n+1)
    b = range(1, n+1)

    # Obtener número de núcleos
    nucleos = int(mp.cpu_count()/2)

    # Resultado
    dotp = 0.0

    # Queue de productos parciales (Cola de escritura)
    productos = mp.Queue()

    # Segmentación de la carga
    if(n%nucleos != 0):
        print("Segmentación incorrecta")
        exit(-1)
    else:
        segmento = int(n/nucleos)

    for i in range(1, nucleos+1):

        # Definiendo colas de lectura
        a_q = mp.Queue()
        b_q = mp.Queue()

        # Llenando las colas de lectura
        a_q.put(a[(i-1)*segmento:i*segmento])
        b_q.put(b[(i-1)*segmento:i*segmento])

        # Mandar llamar a los procesos
        p = mp.Process(target=producto_punto_parcial, args=(a_q,b_q, productos))
        p.start()
    p.join()
    
    for i in range(productos.qsize()):
        dotp += productos.get()
    print(dotp)
            

