#!/usr/bin/python3 

# Definir uma lista 
lista = [2, 8, 9, 48, 8, 22, -12, 2]

# Adicionar 2 a cada elemento da lista usando list comprehension
lista_new = [i + 2 for i in lista if i > 5]

# Exibir as listas originais e modificada
print(f'{lista}')
print(f'{lista_new}')