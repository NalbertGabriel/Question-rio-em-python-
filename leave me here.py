#Meu projeto em python

print ("hello World-Olá Mundo\n")

print ("Questionario Pessoal\n")


nome = input ("Qual é o seu nome? ")

print ("Olá seja bem vindo" , nome)



g = input ("Sua idade? ")

idade = int(g)

if idade >= 18:
    print ("Maior de Idade\n")
else:
    print ("Menor de Idade\n")

#tabuada Multiplicação de numeros

print ("Tabuada Vomos multiplicar!\n")

y = int(input("Tabuada Do número? "))
final = int(input("Até qual numero multiplicar? "))
x = 0   
while x <= final:
    print (y, ' x ', x, ' = ', y * x)
    x = x + 1 
       

print ("Escolha um comando abaixo\n")

print ("if , else e While\n")

y = input ("qual comando rever? ")

comando = (y)

if comando >= "if":
    print ("será o bloco de instrução a ser executados todas as vezes que a condição for verdadeira.\n")
if comando >= "else":
    print ("A palavra else do Inglês, significa SENÃO e com esta, definiremos o bloco de instrução a ser executado todas as vezes que a expressão definida for igual a falso.")
if comando >= "While":
    print (y , "É um laco de Repeticao")
else:
    print ("Você Nao digitou um comando !")
