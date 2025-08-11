#Variaveis
nome =(input("Digite o seu nome"))
peso =float(input("Digite seu peso"))
altura =float(input("Digite sua altura"))
#Conta do IMC
Imc= peso/(altura*altura)
#mensagens

if Imc<24.9:
   print("Peso normal😁😁😁")

elif Imc<25:
   print("Sobre peso!")

else Imc<18.5:
   print("Baixo peso!!")
  
print(f"{nome},Seu IMC é {Imc:.4}")