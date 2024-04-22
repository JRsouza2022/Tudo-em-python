import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_da_senha = int(input("Digite o tamanho da senha desejada: "))
nova_senha = gerar_senha(tamanho_da_senha)
print("Sua senha gerada é:", nova_senha)
