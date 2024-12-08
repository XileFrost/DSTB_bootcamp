'''Importo la librería random para generar números aleatorios'''
import random

'''Creo el tablero del juego en tamaño 10X10 y relleno del carácter "_"'''
def crear_tablero(tamano):#Creo la función, tamano es el argumento.
    tablero = [] #Creo una lista llamada "tablero" donde almaceno las filas del tablero de juego.
    ltrs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #Creo una lista con las letras que quiero que se lean en la primera columna.
    primera_fila = [" "] + [str(i+1) for i in range(tamano)] #Lista de comprensión que genera una lista de números de 1 al tamaño, y convierto cada número a cadena de texto para que cada columna sea representada como un número en formato de texto.
    tablero.append(primera_fila) #Agrego la primera fila al tablero.
    for i in range(tamano): #Creo las filas del tablero, este bucle recorre los números del 0 hasta tamano - 1.
        fila = [ltrs[i]]+["_"] * tamano #Cada fila es la unión de la letra de la fila con la lista de celdas vacías con "_".
        tablero.append(fila) #Agrego al tablero las filas resultantes de cada iteración.
    return tablero

'''Creo una función para imprimir el tablero sin visualización de los barcos'''
def imprimir_tablero(tablero, mostrar_barcos=False): #Mostrar barcos es un parámetro opcional y por defecto es False, lo que no visibiliza los barcos, viendo en su lugar "_".
    for fila in tablero: #Bucle para recorrer cada fila del tablero.
        fila_imprimir = [] #Creo una liasta vacía para almacenar las celdas de la fila que veré impresas con el "_".
        for celda in fila: #Bucle para recorrer cada celda de la fila.
            if celda == "O" and not mostrar_barcos:
                fila_imprimir.append("_") #Agrego "_" a fila_imprimir en lugar de mostrar el barco.
            else:
                fila_imprimir.append(str(celda)) #Si la celda no contiene un barco y mostrar_barcos es True
        print(" ".join(fila_imprimir)) #Se agrega la celda tal como está a fila_imprimir

'''Creo la función colocar_barco para colocar cada barco en el tablero'''
def colocar_barco(barco,tablero):
    for coordenada in barco:
        x,y = coordenada #Defino coordenada, x para las filas, y para las columnas.
        tablero[x+1][y+1]= "O" # La coordenada es la posición en el tablero y se representa como O. Sumo 1 para respetar la fila de letras y la columna de números, no quiero que se sobreescriban.
    return tablero  

'''Creo la función para disparar a una casilla en el tablero'''
#Explicar lo del True y el False.
def disparar(casilla,tablero):
    x, y = casilla #Defino casilla dentro de la función.
    if tablero[x+1][y+1] == "O": #Sumo +1 para que no se sobreescriban las letras y números de la primera fila y columna.
        print("Tocado")
        tablero[x+1][y+1] = "X" #Si toco un barco la casilla se convierte en una X.
        return True #El disparo ha tenido éxito. 
    else:
        print("Agua")
        tablero[x+1][y+1] = "A" #Si no toco un barco la casilla se convierte en una A.
        return False #El disparo no ha tenido éxito.

'''Creo la función crear_barco(eslora) para generar los barcos de forma aleatoria'''
def crear_barco(eslora): #La función toma el argumento eslora para la longitud del barco.
    barco=[] #Creo una lista nueva que almacenará los coordenadas de las casillas
    casilla_0 = (random.randint(0,9), random.randint(0,9)) #Primera casilla en la que se coloca el barco.
    orientacion = random.choice(["Vertical", "Horizontal"]) #Aleatoriamente el barco si sitúa en vertical o en horizontal.

    barco.append(casilla_0) #Agrego la primera casilla. 
    casilla = casilla_0 #Asigno la primera casilla a la variable casilla para generar las siguientes casillas del barco.
    while len(barco) < eslora: #El bucle while se ejecuta hasta que la longitud del barco sea igual a la eslora deseada.
        if orientacion == "Vertical" and casilla[0]+1 <= 9: #Si la fila es válida dentro del rango 0 a 9 (para que no se salga del tablero) se puede agregar una casilla más.
            casilla = (casilla[0]+1, casilla[1]) #La nueva casilla se coloca en la fila siguiente manteniendo la misma columna.
            barco.append(casilla) # Agrega la nueva casilla a la lista barco.
        elif orientacion == "Horizontal" and casilla[1]+1 <= 9: #Si la siguiente columna es válida dentro del rango 0 a 9 (para que no se salga del tablero) se puede agregar una casilla más.
            casilla = (casilla[0], casilla[1]+1) #La nueva casilla se coloca en la siguiente columna de la misma fila. 
            barco.append(casilla) # Agrega la nueva casilla a la lista barco.
        else:
            break #El bucle while acaba porque el barco ya tiene la longitud deseada.
    return barco #Nos devuelve las coordenadas del barco generado.

'''Creo la función barcos(lista_barcos) para generar barcos de diferente longitud para el usuario y la computadora'''
def barcos(lista_barcos=None): #Creo la función a partir de lista_barcos que tiene un valor por defecto de None, así las listas son independientes y no se comparten entre sí. 
    if lista_barcos is None: #Si no se ha pasado ningún valor a lista_barcos significa que el argumento no fue proporcionado y se crea una nueva lista vacía. 
        lista_barcos = [] #Con None consigo que cada vez que se llame a la función la lista sea independiente y no se use la misma lista entre diferentes llamadas.
    barcos=(2,2,2,3,3,4) #Creo una tupla con la longitud de esloras que han de tener los barcos que quiero crear.
    for barco in barcos: #Recorro cada valor de la tupla barcos para ir generando los barcos. 
        lista_barcos.append(crear_barco(barco)) #Añado a lista_barcos las coordenadas del barco creado aleatoriamente mediante la función crear_barco(barco).
    return lista_barcos #Obtengo una lista con las coordenadas de todos los barcos generados.

'''Creo una función para verificar si todos los barcos han sido hundidos'''
def barcos_hundidos(barcos,tablero): #Función a partir de dos argumentos, barcos (tupla con coordenadas) y tablero.
    for barco in barcos: #Bucle para recorrer cada barco en la lista barcos.
        for coordenada in barco: #Bucle para recorrer la coordenada de cada barco.
            x,y = coordenada
            if tablero[x+1][y+1]!="X": #Si cualquier coordenada de barco en el tablero no tiene un valor de X quedan barcos por hundir.
                return False
    return True #Si el bucle encuentra todas las coordenadas de barco marcadas con X todos los barcos han sido hundidos.

'''Creo una función para disparar aleatoriamente en el tablero'''
def disparar_aleatoriamente(tablero):
    while True: #Bucle indefinido que se ejecuta hasta que encuentra la casilla donde disparar.
        x,y = random.randint(0,9), random.randint(0,9) #Por cada disparo genero dos números enteros aleatorios entre 0 y 9.
        if tablero[x+1][y+1] not in ("A","X"): #Condición que verifica si la casilla ha sido o no disparada previamente. 
            return x,y #Coordenada (fila,columna) de la casilla que la computadora elige para disparar. 

'''Creo una función para verificar la validez de las coordenadas introducidas'''
def validar_entrada(fila,columna):
    if fila not in "ABCDEFGHIJ": #Si la fila no es una letra entre A y J.
        print("Carácter no válido. Introduce una fila entre A y J.")
    if columna < 1 or columna > 10: #Si la columna no es un número entre 1 y 10.
        print("Carácter no válido. Introduce una columna entre 1 y 10.")
        return False
    return True #Los valores introducidos están en el rango y son válidos para disparar.

'''Creo una función para ejecutar el juego'''
def jugar(): 
    #Creo los tableros para usuario y computadora.
    tablero_usuario = crear_tablero(10)
    tablero_pc = crear_tablero(10)
    #Creo los barcos para usuario y computadora. 
    barcos_usuario = barcos()
    barcos_pc = barcos()
    #Colocar los respectivos barcos en los tableros.
    for barco in barcos_usuario: 
        colocar_barco(barco,tablero_usuario)
    for barco in barcos_pc:
        colocar_barco(barco,tablero_pc)
    '''Creo un sistema de turnos'''
    turno_usuario = True #Indico el turno del usuario.
    while True: #Bucle que se ejecuta de manera indefinida hasta que el juego termina porque uno de los dos jugadores ha hundido la flota del otro jugador.
        if turno_usuario:
            print("\nTurno del usuario")
            imprimir_tablero(tablero_usuario) #Muestra el tablero del usuario.
            print("\nTablero de la computadora con disparos previos:")
            imprimir_tablero(tablero_pc, mostrar_barcos=False) #Muestra el tablero de la computadora sin los barcos.
            while True: #Segundo bucle indefinido para que el usuario elija coordenada de disparo.
                fila = input("Elige una fila (A-J):").upper() #Introduzco la fila con una letra de A a J.
                try: #Código a ejecutar.
                    columna = int(input("Elige una columna (1-10):")) #Introduzco la columna con un número de 1 a 10.
                    if validar_entrada(fila,columna): #Comprueba la validez de la coordenada.
                        fila_idx = ord(fila) - ord('A') #Convierte la letra de fila a un índice numérico de 0 a 9.
                        break #Si la entrada es válida salgo del bucle.
                except ValueError: #Creo una excepción para errores de valor.
                    print("Carácter no válido. Introduce una fila entre A y J y una columna entre 1 y 10.")
            resultado = disparar((fila_idx, columna - 1), tablero_pc) #Dispara a la casilla elegida (ajustamos la columna para el índice)
            if resultado:
                if barcos_hundidos(barcos_pc,tablero_pc): 
                    print("¡Enhorabuena! Has hundido la flota de la computadora")
                    break
            turno_usuario = False #Cambia el turno a la computadora.
        else:
            print("\nTurno de la computadora")
            x,y = disparar_aleatoriamente(tablero_usuario) #Función que genera disparos aleatorios de la computadora.
            print(f"La computadora dispara a ({chr(x+ord('A'))},{y+1}") #Imprime la coordenada en formato (fila,columna). La primera parte convierte el índice númerico de la fila en una letra y la segunda convierte el índice de la columna en un número de 1 al 10.
            resultado = disparar((x,y),tablero_usuario) #La computadora dispara en el tablero del usuario.
            if resultado:
                if barcos_hundidos(barcos_usuario,tablero_usuario):
                    print("¡Has perdido! La computadora ha hundido tu flota")
                    break 
            turno_usuario = True #Cambia el turno al jugador. 
            
'''Inicio el juego'''
jugar()     