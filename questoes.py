print ("Questão 1 - Escada de tamanho n")
n = int(input("Por favor, insira o valor de n:"))
def escada(n):
    for i in range(1, n+1):
        txt = "*" * i
        print(txt)
    return
escada(n)

print ("Questão 2 - Senha forte")
senha = input("Digite sua senha:")
tamanho = len(senha)
if tamanho < 6:
    print(6-tamanho)
else:
    print("Sua senha possui o tamanho mínimo para ser considerada segura")

print ("Questão 3 - Anagramas")
palavra = input("Digite a palavra:")
def anagramas(palavra):
    tamanho = len(palavra)
    dicionario = dict()
    for i in range(tamanho):
        substring = ''
        for j in range(i, tamanho):
            substring = ''.join(sorted(substring + palavra[j]))
            dicionario[substring] = dicionario.get(substring, 0)
            dicionario[substring] += 1
    qtd = 0
    for k, v in dicionario.items():
        qtd += (v*(v-1))//2
    return qtd
print(anagramas(palavra))
