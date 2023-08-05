# seq1 = input("Digite a primeira sequencia: ")
# seq2 = input("Digite a segunda sequencia: ")


# print('Sequências iguais' if seq1 == seq2 else 'Sequências diferentes')

import re

seq1 = input("Digite a primeira sequencia: ")
seq2 = input("Digite a segunda sequencia: ")

busca = re.match(seq1, seq2)

if busca:
    print("Sequências iguais")
    print(busca.group())
else:
    print("Sequências diferentes")
