def app():
        #Hago la excepcion y le pido al usuario el valor.
        try:
                num = int(input("Introduce el tamaño que quires para tu matriz:"))
    
        except:
                print("As ingresado un valor no válido")
                return "Valor no válido"
        
        #Importo random para poder generar números aleatorios para la matriz.
        import random
        
        #Generar la matriz cuadrada rellena con números aleatorios 
        # donde la variable num es el número que tu pones para asignarle el tamaño de la matriz.
        print("Matriz:")
        matr = [[random.randint(0,9) for fila in range(num)] for colum in range(num)]
        for a in matr:
                print(a)

        #Es la operacióin de la suma de las filas:
        print("La suma de los números de cada fila son:")
        for b in range(num):
                suma_filas = sum(matr[b])
                print(str(suma_filas))

        #Es la ooperacion de la suma de las columnas:
        print("La suma de los números de cada columna son:")
        suma_columnas = 0
        for c in range(num):
                
                suma_columnas = 0
                
                for f in range(num):
                        suma_columnas = suma_columnas + matr[f][c]

                if f == num-1:
                        print(str(suma_columnas))

app()