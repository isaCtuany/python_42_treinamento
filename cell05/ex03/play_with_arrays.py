#!/usr/bin/python3 

# Definir uma lista 
lista = [2, 8, 9, 48, 8, 22, -12, 2]

# Adicionar 2 a cada elemento da lista 
lista_new = [i + 2 for i in lista if i > 5]
lista_new2 = set(lista_new)

# Exibir as listas originais e modificada
print(f'Array original: {lista}')
print(f'Novo array: {lista_new2}')