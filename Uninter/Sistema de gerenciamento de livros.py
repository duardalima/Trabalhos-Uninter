print("Bem-vindo ao Sistema de Gerenciamento de Livros da Maria!") 

lista_livro = [] 
id_global = 0 

def cadastrar_livro(id): 
    nome = input("Digite o nome do livro: ") 
    autor = input("Digite o autor do livro: ") 
    editora = input("Digite a editora do livro: ") 
    livro = { 
        "id": id, 
        "nome": nome, 
        "autor": autor, 
        "editora": editora 
    } 
    lista_livro.append(livro) 
    print("Livro cadastrado com sucesso!") 

def consultar_livro(): 
    while True: 
        print("\n1. Consultar Todos") 
        print("2. Consultar por Id") 
        print("3. Consultar por Autor") 
        print("4. Retornar ao menu") 
        opcao = input("Escolha a opção desejada: ") 

        if opcao == '1': 
            if not lista_livro: 
                print("Nenhum livro cadastrado.") 
            else: 
                for livro in lista_livro: 
                    print(livro) 
        elif opcao == '2': 
            id_consulta = int(input("Digite o Id do livro: ")) 
            encontrado = False 
            for livro in lista_livro: 
                if livro["id"] == id_consulta: 
                    print(livro) 
                    encontrado = True 
                    break 
            if not encontrado: 
                print("Id não encontrado.") 
        elif opcao == '3': 
            autor_consulta = input("Digite o autor do livro: ") 
            encontrados = [livro for livro in lista_livro if livro["autor"].lower() == autor_consulta.lower()] 
            if encontrados: 
                for livro in encontrados: 
                    print(livro) 
            else: 
                print("Nenhum livro encontrado para o autor informado.") 
        elif opcao == '4': 
            break 
        else: 
            print("Opção inválida. Tente novamente.") 

def remover_livro(): 
    while True: 
        try: 
            id_remover = int(input("Digite o Id do livro a ser removido: ")) 
            for livro in lista_livro: 
                if livro["id"] == id_remover: 
                    lista_livro.remove(livro) 
                    print("Livro removido com sucesso!") 
                    return 
            print("Id inválido. Tente novamente.") 
        except ValueError: 
            print("Entrada inválida. Por favor, digite um número válido.") 
 
if __name__ == "__main__": 
    while True: 
        print("\n1. Cadastrar Livro") 
        print("2. Consultar Livro") 
        print("3. Remover Livro") 
        print("4. Encerrar Programa") 
        
        opcao = input("Escolha a opção desejada: ") 

        if opcao == '1': 
            id_global += 1 
            cadastrar_livro(id_global)     
        elif opcao == '2': 
            consultar_livro()        
        elif opcao == '3': 
            remover_livro() 
        elif opcao == '4': 
            print("Programa encerrado.") 
            break 
        else: 
            print("Opção inválida. Tente novamente.") 
 print("Bem-vindo ao Sistema de Gerenciamento de Livros da Maria!") 
lista_livro = [] 
id_global = 0 

def cadastrar_livro(id): 
    nome = input("Digite o nome do livro: ") 
    autor = input("Digite o autor do livro: ") 
    editora = input("Digite a editora do livro: ") 
    livro = { 
        "id": id, 
        "nome": nome, 
        "autor": autor, 
        "editora": editora 
    }
    lista_livro.append(livro) 
    print("Livro cadastrado com sucesso!")
def consultar_livro(): 
    while True: 
        print("\n1. Consultar Todos") 
        print("2. Consultar por Id") 
        print("3. Consultar por Autor") 
        print("4. Retornar ao menu") 
  
        opcao = input("Escolha a opção desejada: ") 

        if opcao == '1': 
            if not lista_livro: 
                print("Nenhum livro cadastrado.") 
            else: 
                for livro in lista_livro: 
                    print(livro) 
        elif opcao == '2': 
            id_consulta = int(input("Digite o Id do livro: ")) 
            encontrado = False 
            for livro in lista_livro: 
                if livro["id"] == id_consulta: 
                    print(livro) 
                    encontrado = True 
                    break 
            if not encontrado: 
                print("Id não encontrado.") 
        elif opcao == '3': 
            autor_consulta = input("Digite o autor do livro: ") 
            encontrados = [livro for livro in lista_livro if livro["autor"].lower() == autor_consulta.lower()] 
            if encontrados: 
                for livro in encontrados: 
                    print(livro) 
            else: 
                print("Nenhum livro encontrado para o autor informado.") 
        elif opcao == '4': 
            break 
        else: 
            print("Opção inválida. Tente novamente.")        
def remover_livro(): 
    while True: 
        try: 
            id_remover = int(input("Digite o Id do livro a ser removido: ")) 
            for livro in lista_livro: 
                if livro["id"] == id_remover: 
                    lista_livro.remove(livro) 
                    print("Livro removido com sucesso!") 
                    return 
            print("Id inválido. Tente novamente.") 
        except ValueError: 
            print("Entrada inválida. Por favor, digite um número válido.") 
if __name__ == "__main__": 
    while True: 
        print("\n1. Cadastrar Livro") 
        print("2. Consultar Livro") 
        print("3. Remover Livro") 
        print("4. Encerrar Programa") 
       
        opcao = input("Escolha a opção desejada: ") 
        
        if opcao == '1': 
            id_global += 1 
            cadastrar_livro(id_global) 
        elif opcao == '2': 
            consultar_livro() 
        elif opcao == '3': 
            remover_livro() 
        elif opcao == '4': 
            print("Programa encerrado.") 
            break    
        else: 
            print("Opção inválida. Tente novamente.")
