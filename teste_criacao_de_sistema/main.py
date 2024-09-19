import os
from models.programador import Programador

os.system("clear")
QUANT = 2
programadores = []

while True:
    cadastro_usuario = str(input("Deseja cadastrar um usuario: ")).upper()
    if cadastro_usuario == "S":
        os.system("clear")
        programador = Programador(
            nome = input("Digite seu nome: "),
            idade = input("Digite sua idade: "),
            telefone = input("Digite seu telefone: "),
            salario = input("Digite seu salario: "),
            id = input("Digite seu id: ")
            )
        os.system("clear")
        programadores.append(programador)
    else :
        break


os.system("clear")

for i,programador in enumerate(programadores):
    print(f"{i+1}° Programador:\n")
    print(programador)
    print()
