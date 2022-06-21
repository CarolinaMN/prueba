import random
AHORCADO = ['''
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
    =========''']

class Ahorcado:
    def buscarPalabraAleat(self, listaPalabras):
        palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
        return listaPalabras[palabraAleatoria]

    def tablero(self, AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
        print(AHORCADO[len(letraIncorrecta)])
        print ("")
        fin = " "
        print ('Letras incorrectas:', fin)
        for letra in letraIncorrecta:
            print (letra, fin)
        print ("")
        espacio = '_' * len(palabraSecreta)
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] in letraCorrecta:
                espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
        for letra in espacio:
            print (letra, fin)
        print ("")

    def elijeLetra(self, algunaLetra):
        while True:
            print ('Adivina una letra:')
            letra = input()
            letra = letra.lower()
            if len(letra) != 1:
                print ('Introduce una letra a la ve.') 
            elif letra in algunaLetra:
                print ('Ya nombraste esa letra ¿Qué tal si pruebas con una diferente?')
            elif letra not in 'abcdefghijklmnopqrstuvwxyz':
                print ('Ingresa una letra.')
            else:
                return letra
    
    def iniciarjuego(self):
        print('Quieres jugar de nuevo? (Si o No)')
        return input().lower().startswith('s')



print ('A H O R C A D O')
palabras = 'lunes martes miercoles jueves viernes sabado domingo'.split()
letraIncorrecta = ""
letraCorrecta = ""

# clase
ahorcado = Ahorcado()
palabraSecreta = ahorcado.buscarPalabraAleat(palabras)
finJuego = False
while True:
    ahorcado.tablero(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
    letra = ahorcado.elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('¡Muy bien! La palabra secreta es "' + palabraSecreta)
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            ahorcado.tablero(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            finJuego = True

    if finJuego:
        if ahorcado.iniciarjuego():
            letraCorrecta = ""
            letraIncorrecta = ""
            finJuego = False
            palabraSecreta = ahorcado.buscarPalabraAleat(palabras)
        else:      
            break

ja = Ahorcado()