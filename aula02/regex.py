import re

regex = '[^ ]*[r|R][^ |\.]*'

texto = 'o rato roeu a roupa do rei de roma'

busca = re.findall(regex, texto)

if busca:
    print(busca)
