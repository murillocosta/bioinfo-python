# coding: utf-8

# file = open("file.txt")
# texto = file.read()
# print(texto)

new_file = open("file02.txt", "w", encoding="utf-8")
new_file.write("Bioinformática com Python")

new_file = open('file02.txt', encoding='utf-8')

text02 = new_file.readlines()
print(text02)

new_file.close()
