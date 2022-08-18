#             # Aula 01
# x = int(5)
# z = "5"
# y = float(10)

# #
# print(x+x)
# print(y)
# print(type(z))

# #
# print("digte um valor:")
# a = input()
# print("o valor digitado foi: "+ a)

# num2 = input("digite o segundo valor:")
# print(num2)

# res = int(a)+int(num2)
# print(res)

#                 # Exercícios

# # Ex 01
# print("Calculadora")
# n1 = input("Valor: ")
# n2 = input("Valor: ")

# sum = int(n1)+int(n2)
# div = int(n1)/int(n2)
# mult = int(n1)*int(n2)
# sub = int(n1)-int(n2)

# print("A soma dos valores é: ", sum)
# print("A divisão dos valores é: ", div)
# print("A multiplicação dos valores é: " , mult)
# print("A subtração dos valores é: " , sub)

# # Ex02 
# nome = str(input("Nome: "))
# idade = int(input("idade: "))
# dt_nasc = str(input("data de nascimento: "))
# end = str(input("endereço: "))
# tel = int(input("telefone: "))

# # print("O tipo da variável: ",nome," é:", type(nome))

# print("O nome digitado foi: ",nome)
# print("A idade digitado foi: ",idade)
# print("O endereço digitado foi: ",end)
# print("O telefone digitado foi: ",tel)
# print("A data de nascimento digitada foi: ",dt_nasc)

# EX 03
# metro = float(input("Metros: "))
# print(metro ,"\rmetros em centímetros é: " ,metro*100)

#Ex 04
#
# nome = str(input("Nome: "))
# n1 = float(input("Nota 01: "))
# n2 = float(input("Nota 02: "))

# print("A média do aluno", nome, "é: ", (n1+n2)/2)

# Desafio ex 05
# n1 = int(input("Digite um número: "))

# if n1 > 0:
#   print("É um número positivo")

# elif n1<0:
#   print("É um numero negativo")

# else:
#   print("É um numero neutro")


# Ex salario ---------- IF
# nome = str(input("Nome: "))
# idade = str(input("Idade: "))
# cpf= str(input("CPF: "))
# salario_atual = float(input("Salário Atual: "))
# # print(salario_atual)

# novo_salario = 0

# if salario_atual< 500:
#   novo_salario = (15/100) * salario_atual
#   print(f"Novo salário reajustado: {novo_salario + salario_atual:.2f}")
  
# elif salario_atual >= 500 and salario_atual<= 1000:
#   novo_salario = (10/100) * salario_atual
#   print(f"Novo salário reajustado: {novo_salario + salario_atual:.2f}")
  
# elif salario_atual > 1000:
#   novo_salario = salario_atual* (5/100)
#   print(f"Novo salário reajustado: {novo_salario + salario_atual:.2f}")


#  ---------- FOR 

# print('Tabuada')
# num = int(input("Digite o número a ser calculado: "))

# for i in range(1,11):
#   print(num," * ",num, " = ", num* i)

# Exercicios FOR

# exercicio 01
# for i in range(5,101):
#   if i%7==0 and i%5!= 0:
#     print(i)

# exercicio 02
num = int(input("num: "))
x = 0
for i in range(1, num):
  num = i+num
  print(num)
  
  