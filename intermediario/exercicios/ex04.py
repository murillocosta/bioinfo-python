escolha = 0


def abrirArquivo():
    nome = input("Digite o nome do arquivo que deseja abrir: ")
    arquivo = open(nome)
    return arquivo


def lerArquivo(arquivo):
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())


while escolha != 3:
    escolha = int(input(
        "[1] para abrir arquivo\n[2] para ler arquivo\n[3] para fechar o programa\n escolha um número: "))

    if escolha == 1:
        arquivo = abrirArquivo()
    elif escolha == 2:
        lerArquivo(arquivo)
