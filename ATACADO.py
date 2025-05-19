'''
•	Se valor for menor que 2500 o desconto será de 0%;
•	Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
•	Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
•	Se valor for igual ou maior que 10000 o desconto será de 11%;


Elabore um programa em Python que:
A.	*CHECK*  Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e sobrenome [EXIGÊNCIA DE CÓDIGO 1 de 6];
B.	*CHECK* Deve-se implementar o input do valor unitário e da quantidade do produto [EXIGÊNCIA DE CÓDIGO 2 de 6];
C.	*CHECK* Deve-se implementar o desconto conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];
D.	*CHECK* Deve-se implementar o valor total sem desconto e o valor total com desconto [EXIGÊNCIA DE CÓDIGO 4 de 6];
E.	*CHECK* Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];  
F.	*CHECK* Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
G.	*CHECK* Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];
H.	*CHECK* Deve-se apresentar na saída de console um pedido recebendo desconto (valor total sem desconto maior ou igual a 2500) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];  


'''
#Funções e Variaveis ultilizadas.
menu = ("_"*38 + '\n|Bem-vindo ao atacado Ander Queiroga!|\n' + "‾"*38) #menu do nosso programa
print (menu)

def desconto (quantidade): #Para maior praticidade e facil uso do programa, criei uma função que me da o desconto de acordo com a quantidade que o usuario deseja comprar do produto
    if quantidade >= 2500 and quantidade < 6000:
         desconto = 0.04
    elif quantidade >= 6000 and quantidade < 1000:
         desconto = 0.07
    elif quantidade >= 1000:
         desconto = 0.11
    return desconto

#Programa principal!

valor = float(input("Digite o valor do produto: ")) #insere o valor do produto
quantidade = int(input("Digite a quantidade: "))    #insere a quantidade do produto
total = quantidade * valor #valor do total sem desconto
if quantidade < 2500:   #Caso a quantiade seja menor que 2500, nao havera desconto
     comdesconto = total
else:                   #se nao, sera aplicado um desconto de acordo com a quantidade
     comdesconto = total - (total*desconto(quantidade))
print (f'Valor SEM desconto R${total}')
print (f'Valor COM desconto R${comdesconto}')           #42, 43 e 44 mostram as informações para o usuario no terminal, valor com e sem desconto E o quanto o usario esta economizando
print (f"Voce esta esconomizando R${total*desconto(quantidade)}")