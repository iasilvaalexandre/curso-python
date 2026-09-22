# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if  'l' in letras:
        print('Parabens, você digitou a letra "l"')
        break   

    print(letras)