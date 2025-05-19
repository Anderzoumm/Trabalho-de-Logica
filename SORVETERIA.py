'''
A.	*CHECK* Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e sobrenome [EXIGÊNCIA DE CÓDIGO 1 de 8];
B.	*CHECK* Deve-se implementar o input do sabor (CP/AC) e o print “Sabor inválido. Tente novamente" se o usuário entra com valor diferente de CP e AC [EXIGÊNCIA DE CÓDIGO 2 de 8];
C.	*CHECK* Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];
D.	*CHECK* Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8];
E.	*CHECK* Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];
F.	*CHECK* Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];
G.	*CHECK* Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];
H.	*CHECK* Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
I.	*CHECK* Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
J.	*CHECK* Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; 
K.	*CHECK* Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
L.	*CHECK* Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];  

'''
#Funções e variaveis ultilizadas
menu = (
    "Bem-vindo(a) ao Expresso Anderson Queiroga!!\n"
    + "-"*18 + "Cardápio" + "-"*18 + '\n'
    + "-"*44 + "\n"
    + '---| Tamanho | Cupuaçu (CP) | Açaí (AC) |---\n'
    + "---|    P    |   R$  9.00   | R$ 11.00  |---\n"
    + "---|    M    |   R$ 14.00   | R$ 16.00  |---\n"
    + "---|    G    |   R$ 18.00   | R$ 20.00  |---\n"
    + "-" * 44
)
def escsabor (): #Essa função nao recebe parametros pois ela mesma ja executa o INPUT, ela tem a função de registrar o sabor desejado
        
        while True:
            sabor = input("Entre com o sabor desejado(CP/AC): ").upper()
            if sabor == "AC":
                nsabor = "Açai"
                print(f"Sabor selecionado: {nsabor}")    
                break
            elif sabor == "CP":
                nsabor = "Cupuaçu"
                print(f"Sabor selecionado: {nsabor}")    
                break
            else:
                 # Mensagem exibida quando a entrada é inválida
                 print("Sabor inválido. Tente novamente.")
        return nsabor
def esctamanho (): #Essa função nao recebe parametros pois ela mesma ja executa o INPUT, ela tem a função de registrar o tamanho desejado
        
        while True:
            tam = input("Entre com o tamanho desejado(P,M,G): ").upper() 
            if tam == "P" or tam == "M" or tam == "G":
                print(f"Sabor selecionado: {tam}")    
                break
            else:
                 # Mensagem exibida quando a entrada é inválida
                 print("Tamanho inválido. Tente novamente.")
        return tam

def preco(sabor, tamanho):# Função que retorna o preço com base no sabor e tamanho escolhidos, parametros obrigatorios
    if sabor == "Açai" and tamanho == "P":
         final = 11
    elif sabor == "Açai" and tamanho == "M":
         final = 16
    elif sabor == "Açai" and tamanho == "G":
         final = 20
    elif sabor == "Cupuaçu" and tamanho == "P":
         final = 9
    elif sabor == "Cupuaçu" and tamanho == "M":
         final = 14
    elif sabor == "Cupuaçu" and tamanho == "G":
         final = 18
    return final
carrinho = 0 # Variável que acumula o total das compras
print (menu) #mostra apenas 1 vez o menu.
while True:
    sabor = escsabor()
    tamanho = esctamanho()
    compra = preco(sabor, tamanho)
    print (f"Voçê pediu um {sabor} no tamanho {tamanho}: R${compra}")
    carrinho += compra
    # Verifica se o cliente deseja continuar comprando
    opc = input("Deseja pedir mais alguma coisa?(s/n)")
    if opc == "s":
         continue
    else:
         print (f"O total da sua compra deu R${carrinho}")
         break


