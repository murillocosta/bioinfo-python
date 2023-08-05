arquivo_usuario = input('Qual arquivo deseja abrir?')


arquivo = open('../../intermediario/exercicios/' + arquivo_usuario)
linhas = arquivo.readlines()

for linha in linhas:
    print(linha.strip())
