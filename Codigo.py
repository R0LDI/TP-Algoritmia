#Librerias
from random import randint as rn

#Funciones

#Creacion de variables

def ingresar_opcion_menu():
    '''Ingreso de opcion del menu'''
    try:
        opcion = '0'
        while not opcion.isalpha() or len(opcion) > 1 and opcion != '':
            opcion = input('''Opciones:
1- Iniciar juego
2- Editar palabras y pistas
3 - Salir
: ''')
            return opcion
    except KeyboardInterrupt:
        return print('Salida de emergencia')

def opcion():
    try:
        '''Usuario ingresa opcion'''
        opcion1 = input(' Ingrese letra: ').strip().upper()
        validar = validar_opcion(opcion1)
        if validar:
            return opcion1
        else:
            print('Opcion invalida - Ingrese solo un caracter alfabeticos')
            return opcion()
    except KeyboardInterrupt:
        return print('Salida de emergencia')

def crear_ahorcado(palabra):
    ahorcado = list() #Palabra dividida por letras
    for n in palabra:
        if n == ' ':
            ahorcado.append('   ') #Convierte los espacios simples en espacios triples para que coincida con linea 52
        else:
            ahorcado.append(n)
    return ahorcado

def tipito(intentos):
    ahorcado = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
    O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
    O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
    O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
    O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
    O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
    O   |
     /|\  |
     / \  |
          |
    =========''', '''
 Winner
 
   \ O /   
      | 
     / \   
===========  ''', '''
     
    O /   
     /|     Adios!
     / \   ''']
    if intentos == 6:
        return ahorcado[0]
    elif intentos == 5:
        return ahorcado[1]
    elif intentos == 4:
        return ahorcado[2]
    elif intentos == 3:
        return ahorcado[3]
    elif intentos == 2:
        return ahorcado[4]
    elif intentos == 1:
        return ahorcado[5]
    elif intentos == 0:
        return ahorcado[6]
    elif intentos == 'win':
        return ahorcado[7]
    elif intentos == 'chau':
        return ahorcado[8]

def creditos():
    return f'''
Programadores:
Bono Dipacce
Lucas Roldan
Nicolas Constantini
Lautaro Figueroa
:)'''

#Acciones y modificaciones
        
def validar_opcion(opcion):
    '''Valida la opcion del usuario ante posibles errores'''
    if len(opcion) != 1:
        return False
    if opcion.isalpha():
            return True

def seleccionar_palabra():
    '''Selecciona desde el archivo de texto "palabras.txt" una palabra a adivinar'''
    try:
        with open('palabras.txt', 'rt', encoding='UTF-8') as palabras:
            palabritas = []
            linea = 1 #Asi entra al while
            while linea != '':
                linea = palabras.readline().strip().upper()
                palabritas.append(linea)
            palabritas.pop()
            indice= rn(0, len(palabritas)-1)
    except:
        pass
    return str(palabritas[indice]), indice

def transformar_en_guiones(palabra):
    '''Transforma la palabra a adivinar en guiones y espacios'''
    guiones1 = [] #Palabra en guiones
    for n in palabra:
        if n == ' ':
            guiones1.append('   ')
        else:
            guiones1.append('-')
    return guiones1

def seleccionar_pista(indice):
    '''Selecciona la pista del archivo "pistas.txt" correspondiente a la palabra a adivinar'''
    try:
        with open('pistas.txt', 'rt', encoding='UTF-8') as pistas:
            pista = []
            linea = 1 #Asi entra al while
            while linea != (''):
                linea = pistas.readline().strip().upper()
                pista.append(linea)
            pista.pop() #Elimina el ultimo espacio
            return pista[indice]
    except:
        pass        
        
def jugar_de_nuevo():
    try:
        '''Opcion para seguir jugando o no cuando se gana o pierde el juego'''
        opcion = input('Jugar de nuevo? S/N: ').lower()
        while opcion != 's' and opcion != 'n':
            opcion = input('Seleccione opcion - Jugar de nuevo? S/N: \n')
        if opcion == 's':
            return juego()
        else:
            return menu()
    except KeyboardInterrupt:
        return print('Salida de emergencia')

def editar():
    '''Agrega palabras y pistas a los txt donde se buscan las palabras a adivinar y las pistas'''
    try:
        with(
            open('palabras.txt', 'a', encoding='UTF-8')) as palabras, (
            open('pistas.txt', 'a', encoding='UTF-8')) as pistas:
                while True:
                    nueva_palabra = input('Ingrese palabra a agregar (enter para salir): ')
                    if nueva_palabra == '':
                        return menu()
                    nueva_pista = input('Ingrese nueva pista: ')
                    if (nueva_pista.isalpha() and len(nueva_pista )> 1) and nueva_palabra.isalpha():
                        palabras.write('\n' + nueva_palabra)
                        pistas.write('\n' + nueva_pista)
                    else:
                        print('Ambos campos deben estar completos')
    except KeyboardInterrupt:
        return print('Salida de emergencia')
        
def imprimir_guiones(guiones):
    '''Imprime la lista de guiones con la palabra a adivinar'''
    for i in guiones:
        print(i, end=' ')
    return ''

def acierto(guiones, opcion, ahorcado):
    '''Accion cuando el usuario acierta'''
    if opcion in ahorcado: #Palabra acertada
        if guiones.count(opcion) > 1:
            return print('Ya pusiste la letra')
        else:
            for i in range(len(ahorcado)):
                if ahorcado[i] == opcion:
                    guiones[i] = opcion
    return ''

def no_se_encuentra(opcion, intentos):
    '''Accion cuando el usuario se equivoca'''
    print(tipito(intentos))
    return  print(f'{opcion} no se encuentra - Intentos restantes: {intentos}')

def fin_de_juego(palabra, intentos):
    '''Accion cuando se gana o pierde el juego'''
    if intentos == 0:
        print(f'Perdiste - Palabra correcta: {palabra}')
        return jugar_de_nuevo()
    else:
        print(tipito('win'))
        print(f'Ganaste - palabra correcta: {palabra}')
        return jugar_de_nuevo()

#Llamamiento y ejecucion de funciones - Menu

def juego():
    '''Programa principal'''
    intentos = 6
    try:
        indice = seleccionar_palabra()
        palabra = indice[0].upper()
        pista = seleccionar_pista(indice[1]).upper()
        ahorcado = crear_ahorcado(palabra)
        guiones = transformar_en_guiones(palabra)
        while True:
            print(tipito(intentos))
            print(pista)
            imprimir_guiones(guiones)
            opcion1 = opcion()
            if opcion1 not in ahorcado:
                intentos -= 1
                no_se_encuentra(opcion1, intentos)
            acierto(guiones, opcion1, ahorcado)
            if guiones == ahorcado or intentos == 0:
                fin_de_juego(palabra, intentos)
                return ''
    except KeyboardInterrupt:
        print(f'Palabra correcta: {palabra}')
        print('Salida de emergencia')
        
def menu():
    '''Menu principal'''
    try:
        print('Bienvenido al ahorcado.py ')
        opcion = ingresar_opcion_menu()
        if opcion == '1':
            return juego()
        elif opcion == '2':
            return editar()
        if opcion == '3':
            return print(creditos())
        else:
            return print('Opcion invalida'), menu()
    except:
        pass






