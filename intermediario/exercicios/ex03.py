seq = input('Por favor, insira a sequência desejada: ')

arquivo = open('seq_user.fasta', 'w')

arquivo.write(">seq\n")
arquivo.write(seq)

arquivo.close()
