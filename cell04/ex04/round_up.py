#!/usr/bin/python3 

import math

# Solicita um número ao usuário
numero = float(input("Digite um número: "))
    
try:
# # Tenta converter a entrada para float
#     num = float(numero)
        
# Arredonda o número para cima
    arredondar = math.ceil(numero)
        
# Exibe o número arredondado
    print(arredondar)
        
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número.")

