"""https://br.spoj.com/problems/PAPRIMAS/"""

import string, collections

palavra = input("Digite a palavra para sabermos se é primo ou não: ")

dicionario_minusculo = dict(zip(string.ascii_lowercase, range(1,27)))
dicionario_maiusculo = dict(zip(string.ascii_uppercase, range(27,53)))
ambos_dicionarios = collections.ChainMap(dicionario_minusculo, dicionario_maiusculo)

for letra in palavra:
    soma = 0
    numero_letra = ambos_dicionarios[letra]
    print(letra, numero_letra)
    soma += 
    
if soma_letra % 2 == 0:
    print("Palavra não prima")
else:
    print("Palavra Prima")
