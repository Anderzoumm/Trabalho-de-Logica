'''
Elabore um programa em Python que: 
A.	Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 8];
B.	Deve-se implementar uma lista vazia com o nome de lista_livro e a variável id_global com valor inicial igual a 0 [EXIGÊNCIA DE CÓDIGO 2 de 8];
C.	Deve-se implementar uma função chamada cadastrar_livro(id) em que: [EXIGÊNCIA DE CÓDIGO 3 de 8];
a.	Pergunta nome, autor, editora do livro;
b.	Armazena o id (este é fornecido via parâmetro da função), nome, autor, editora dentro de um dicionário;
c.	Copiar o dicionário para dentro da lista_livro;
D.	Deve-se implementar uma função chamada consultar_livro() em que: [EXIGÊNCIA DE CÓDIGO 4 de 8];
a.	Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu):
i.	Se Consultar Todos, apresentar todos os livros com todos os seus dados cadastrados;
ii.	Se Consultar por Id, apresentar o livro específico com todos os seus dados cadastrados;
iii.	Se Consultar por Autor, apresentar o(s) livro(s) do autor com todos os seus dados cadastrados;
iv.	Se Retornar ao menu, deve-se retornar ao menu principal;
v.	Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta D.a.
vi.	Enquanto o usuário não escolher a opção 4, o menu consultar livros deve se repetir.
E.	Deve-se implementar uma função chamada remover_livro() em que: [EXIGÊNCIA DE CÓDIGO 5 de 8];
a.	Deve-se pergunta pelo id do livro a ser removido;
b.	Remover o livro da lista_livro;
c.	Se o id fornecido não for de um livro da lista, printar “Id inválido” e repetir a pergunta E.a.
F.	Deve-se implementar uma estrutura de menu no código principal (main), ou seja, não pode estar dentro de função, em que: [EXIGÊNCIA DE CÓDIGO 6 de 8];
a.	Deve-se pergunta qual opção deseja (1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa):
i.	Se Cadastrar Livro, acrescentar em um id_ global e chamar a função cadastrar_livro(id_ global);
ii.	Se Consultar Livro, chamar função consultar_livro();
iii.	Se Remover Livro, chamar função remover_livro();
iv.	Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
v.	Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta F.a.
vi.	Enquanto o usuário não escolher a opção 4, o menu deve se repetir.
G.	Deve-se implementar uma lista de dicionários (uma lista contento dicionários dentro) [EXIGÊNCIA DE CÓDIGO 7 de 8];
H.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
I.	Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6];
J.	Deve-se apresentar na saída de console um cadastro de 3 livros (sendo 2 deles no mesmo autor) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6];
K.	Deve-se apresentar na saída de console uma consulta de todos os livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6];
L.	Deve-se apresentar na saída de console uma consulta por código (id) de um dos livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6];
M.	Deve-se apresentar na saída de console uma consulta por autor em que 2 livros sejam do mesmo autor [EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6];
N.	Deve-se apresentar na saída de console uma remoção de um dos livros seguida de uma consulta de todos os livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];
'''
#FUNÇÕES E VARIAVEIS ULTILIZADAS
def cadastrar_livro(id):
    """
    Função feita para cadastrar um livro novo, seu parametro é obrigatorio para definir o id do livro novo
    """
    print("\n--- Cadastrar Novo Livro ---")
    nome_livro = input("Digite o nome do livro: ") #Recebe o nome do livro
    autor_livro = input("Digite o nome do autor: ") #Recebe o autor do livro
    editora_livro = input("Digite a editora do livro: ") #Recebe a editora do livro

    livro = {
        'id': id,
        'nome': nome_livro,
        'autor': autor_livro,
        'editora': editora_livro
    } 
    lista_livro.append(livro)
    #Aqui ele vai criar um dicionario e adicionar a lista de livros


    print(f"Livro com ID {id} cadastrado com sucesso!")

def consultar_livro():
    '''
    Função criada para consultar os livros ja adicionados, parametros nao sao obrigatorios aqui
    
    
    '''
    while True:
        menu_consulta = ("\n--- Consultar Livros ---\n"
                +"1. Consultar Todos\n"
                +"2. Consultar por Id\n"
                +"3. Consultar por Autor\n"
                +"4. Retornar ao menu")
        print (menu_consulta)

        opcao = input("Digite a opção desejada: ")

        if opcao == '1': #Consulta livro por ID
            if not lista_livro: #Se nao existir um livro cadastrados ainda ele retorna isso
                print("Nenhum livro cadastrado.")
            else:               #se existir ao menos 1 livro cadastrado, ele entra em um loop for para printar todos os livros
                print("\n--- Todos os Livros ---")
                for livro in lista_livro: #para cada livro na lista de livros printar os dicionarios
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print("-" * 20)

        elif opcao == '2':
            try: #tenta realizar uma busca pelo id fornecido
                id_busca = int(input("Digite o ID do livro que deseja consultar: "))
                encontrado = False #faz a verificação de que foi encontrado um livro com esse id
                for livro in lista_livro:
                    if livro['id'] == id_busca:
                        print("\n--- Livro Encontrado ---")
                        print(f"ID: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}")
                        print("-" * 20)
                        encontrado = True
                        break
                if not encontrado: #se o livro nao foi encontrado como o id fornecido
                    print("Nenhum livro encontrado com o ID fornecido.")
            except: #caso de algum erro, pode ser ValueError ou outros
                print("ID inválido. Por favor tente novamente")

        elif opcao == '3':
            #consulta os livros de acordo com o dicionario que tenha o nome do autor mencionado
            autor_busca = input("Digite o nome do autor que deseja consultar: ")
            livros_autor = []
            for livro in lista_livro:
                if livro['autor'].lower() == autor_busca.lower():#para facilitar o programa a encontrar o autor
                    livros_autor.append(livro)

            if not livros_autor: #caso nao tenha nenhum livro com esse autor
                print(f"Nenhum livro encontrado do autor '{autor_busca}'.")
            else:
                print(f"\n--- Livros do Autor '{autor_busca}' ---")
                for livro in livros_autor:
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print("-" * 20)

        elif opcao == '4': #sair do menu de consulta
            break


        else:
            print("Opção inválida. Por favor, digite um número de 1 a 4.")

def remover_livro():
    '''
    Função criada para remover algum livro APENAS POR ID
    
    '''
    print("\n--- Remover Livro ---")
    while True:
        try:
            id_remover = int(input("Digite o ID do livro que deseja remover: "))
            encontrado_indice = -1
            for indice, livro in enumerate(lista_livro):
                if livro['id'] == id_remover:
                    encontrado_indice = indice
                    break
                #cria uma variavel para escolher o livro com id informado
            if encontrado_indice != -1:
               
                livro_removido = lista_livro.pop(encontrado_indice)
                print(f"Livro com ID {livro_removido['id']} ('{livro_removido['nome']}') removido com sucesso!")
                break
                #remove o item com o id informado
            else: #caso nao ache o ID
                print("Id inválido. Nenhum livro encontrado com o ID fornecido. Tente novamente.")
        except:# caso de algum erro
            print("ID inválido. Por favor, tente novamente..")




lista_livro = []
id_global = 0
menu = ('   Bem vindo a livravia do Andeson Queiroga   \n'
        +'----------------------------------------------\n'
        +'--------------- MENU PRINCIPAL ---------------\n'
        +'Escolha a opção desejada\n'
        +'1 - Cadastrar livro\n'
        +'2 - Consultar Livro(s)\n'
        +'3 - Remover Livro\n'
        +'4 - Sair\n'
        )

#PROGRAMA PRINCIPAL     
while True:
        print (menu)
        opc = int(input("Digite uma opção acima: "))
        if opc == 1:
            id_global += 1
            cadastrar_livro(id_global)
        elif opc == 2:
            consultar_livro()
        elif opc == 3:
            remover_livro()
        elif opc == 4:
                print("Encerrando programa...")
                break
        