import random
palavras = ['python', 'programacao', 'computador', 'desenvolvimento', 'algoritmo', 'openai', 'inteligencia', 'artificial']
def escolher_palavra(palavras):
    return random.choice(palavras)
def exibir_palavra_oculta(palavra, letras_reveladas):
    resultado = ''
    for letra in palavra:
        if letra in letras_reveladas:
            resultado += letra
        else:
            resultado += '_'
    return resultado
def jogar_forca():
    palavra = escolher_palavra(palavras)
    letras_reveladas = set()
    tentativas_maximas = 6
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra:")
    print(exibir_palavra_oculta(palavra, letras_reveladas))

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_reveladas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_reveladas.add(letra)
            print("Letra correta!")
        else:
            tentativas += 1
            print("Letra incorreta!")
            print(f"Tentativas restantes: {tentativas_maximas - tentativas}")

        print(exibir_palavra_oculta(palavra, letras_reveladas))

        if '_' not in exibir_palavra_oculta(palavra, letras_reveladas):
            print("Parabéns! Você ganhou!")
            break
        elif tentativas == tentativas_maximas:
            print("Você perdeu! A palavra era:", palavra)
            break
if __name__ == "__main__":
    jogar_forca()
