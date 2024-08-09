#!/usr/bin/python3 

#Digite sua idade
idade_hoje = int(input("Please tell me your age: "))
print(f"You are currently {idade_hoje} years old.")

for i in range(3):
    idade_hoje += 10
    print(f"In {(i + 1) * 10} years, you'll be {idade_hoje} years old.")


# #Soma de idades
# idade_10 = idade_hoje + 10
# idade_20 = idade_hoje + 20
# idade_30 = idade_hoje + 30

# #Resultado
# print(f"In 10 years, you'll be {idade_10} years old.")
# print(f"In 20 years, you'll be {idade_20} years old.")
# print(f"In 30 years, you'll be {idade_30} years old.")