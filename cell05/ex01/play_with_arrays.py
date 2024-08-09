#!/usr/bin/python3 

# Definir uma lista 
lista = [2, 8, 9, 48, 8, 22, -12, 2]

# Adicionar 2 a cada elemento da lista usando list comprehension
lista_new = [i + 2 for i in lista]

# Exibir as listas originais e modificada
print(f'Original array: {lista}')
print(f'New array: {lista_new}')