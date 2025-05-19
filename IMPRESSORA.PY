'''
A.	*CHECK* Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 7];
B.	*CHECK* Deve-se implementar a função escolha_servico() em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
a.	        Pergunta o servico desejado;
b.	        Retorna o valor servico com base na escolha do usuário;
c.	        Repete a pergunta do item B.a se digitar uma opção diferente de: dig/ico/ipb/fot;
C.	*CHECK* Deve-se implementar a função num_pagina() em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
a.	        Pergunta o número de páginas;
b.	        Retorna o número de páginas com desconto seguindo a regra do enunciado (desconto calculado em cima do número de páginas);
c.	        Repete a pergunta do item C.a se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico)
D.	*CHECK* Deve-se implementar a função servico_extra() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
a.	    Pergunta pelo serviço adicional;
b.	    Retornar o valor de apenas uma das opções de adicional 
c.	    Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0;
E.	*CHECK* Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função, conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5 de 7];
F.	*CHECK* Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7];
G.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de 7];
H.	Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
I.	Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de serviço [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
J.	Deve-se apresentar na saída de console um pedido no qual o usuário digitou ultrapassou no número de páginas [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
K.	*CHECK* Deve-se apresentar na saída de console um pedido com opção de serviço, número de páginas e serviço extra válidos [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];
'''
# Funções e variáveis utilizadas

def escolha_servico():
    """
    Permite ao usuário escolher o tipo de serviço desejado através da entrada de texto.
    O loop continua até que uma opção válida (DIG, ICO, IPB ou FOT) seja inserida.
    Retorna o valor correspondente ao serviço escolhido.
    """
    while True:
        opc = input("Entre com o tipo de serviço desejado" \
                      ">>> ").upper()  # Solicita a opção do serviço e converte para maiúsculas para comparação

        if opc == "DIG":
            valor = 1.10  # Define o valor para Digitalização
            break  # Sai do loop quando uma opção válida é escolhida
        elif opc == "ICO":
            valor = 1.00  # Define o valor para Impressão Colorida
            break  # Sai do loop quando uma opção válida é escolhida
        elif opc == "IPB":
            valor = 0.40  # Define o valor para Impressão Preto e Branco
            break  # Sai do loop quando uma opção válida é escolhida
        elif opc == "FOT":
            valor = 0.20  # Define o valor para Fotocópia
            break  # Sai do loop quando uma opção válida é escolhida
        else:
            print ("Opção invalida, tente novamente") # Informa o usuário sobre a opção inválida
    return valor  # Retorna o valor do serviço escolhido


def num_pagina():
    """
    Solicita ao usuário o número de páginas e calcula o valor total com base em descontos por quantidade.
    Possui tratamento de erros para garantir que a entrada seja um número inteiro.
    Impõe um limite máximo de páginas e solicita a entrada novamente se excedido.
    Retorna o valor total das páginas após a aplicação de um possível desconto.
    """
    while True:  # Loop principal para garantir uma entrada válida de número de páginas
        while True:  # Loop interno para tratamento de erros na entrada do número
            try:
                
                num = int(input("Digite o numero de paginas: ")) # Solicita o número de páginas
                if num >= 2000:
                    print ("Não aceitamos tantas páginas de uma vez.\n" \
                   +"Por favor, entre com o numero de páginas novamente.") # Informa sobre o limite de páginas
                elif num < 2000:
                    break  # Sai do loop interno se a entrada for um inteiro válido
            except ValueError:  # Captura erros se a entrada não for um inteiro
                print ("Houve um erro na digitação, tente novamente!")


        if num < 20:
            desc = 0  # Sem desconto para menos de 20 páginas
        elif num >= 20 and num < 200:
            desc = 0.15  # 15% de desconto para 20 a 199 páginas
        elif num >= 200 and num < 2000:
            desc = 0.20  # 20% de desconto para 200 a 1999 páginas
        # A linha abaixo parece ter um erro de lógica, pois a condição já foi tratada no if anterior (num >= 2000)
        # elif num >= 2000 and num < 20000:
        #     desc = 0.25
        else: # Adicionando um caso para números maiores ou iguais a 2000 (já que a condição anterior tinha um erro)
            desc = 0.25 # 25% de desconto para 2000 ou mais páginas

        pagvalor = num - (num * desc) # Calcula o valor total com o desconto aplicado
        return pagvalor # Retorna o valor total das páginas


def servico_extra():
    """
    Apresenta um menu de serviços adicionais (encadernação) e permite ao usuário escolher.
    Possui tratamento de erros para garantir que a entrada seja um número inteiro válido.
    Retorna o valor do serviço adicional escolhido (0 se nenhum for desejado).
    """
    menu = ("Serviços adicionais\n"
            +"1 - Encardenação Simples - R$ 15.00\n"
            +"2 - Encardenação Capa Dura - R$ 40.00\n"
            +"0 - Não desejo mais nada.\n\n"
            +"Deseja adicionar algum serviço?") # Menu de opções de serviços extras
    print (menu)

    while True: # Loop principal para garantir uma entrada válida de opção de serviço extra
        while True: # Loop interno para tratamento de erros na entrada da opção
            try:
                opc = int(input(">>>")) # Solicita a opção do serviço extra
                break # Sai do loop interno se a entrada for um inteiro válido
            except ValueError: # Captura erros se a entrada não for um inteiro
                print ("Opção invalidade, tente novamente.")

        if opc == 1:
            adc = 15 # Define o valor para Encardenação Simples
            break # Sai do loop quando uma opção válida é escolhida
        elif opc == 2:
            adc = 40 # Define o valor para Encardenação Capa Dura
            break # Sai do loop quando uma opção válida é escolhida
        elif opc == 0:
            adc = 0 # Define o valor para "Não desejo mais nada"
            break # Sai do loop quando uma opção válida é escolhida
        else:
            print ("Opção inválida, tente novamente.") # Informa o usuário sobre a opção inválida
    return adc # Retorna o valor do serviço adicional escolhido 



menu = ("Bem vindo a Copiadoa do Anderson Queiroga!\n\n"
        
        +"Nossos serviços\n"
        +"DIG - Digitalização\n"
        +"ICO - Impressão Colorida\n"
        +"IPB - Impressão Preto e Branco\n"
        +"FOT - Fotocópia"        
        )

#Programa Principal
while True :
    print (menu)
    serv=escolha_servico()
    pags = num_pagina()
    extra = servico_extra()
    total = (serv * pags) + extra
    print (f"TOTAL: {total} (Serviço: {serv} * Paginas: {pags} + extra: {extra})")
    break