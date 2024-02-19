#if gerente menu1 #if funcionario menu2
#depois criar visualizações mais bonitinhas para as requeridas

from controller import Controller

class View:

    @staticmethod
    def tela_entrada():
        print("===== Tela Inicial =====")
        print("Você é Gerente (1) ou Funcionário (2)?")
        funcao = input()
        if funcao == "Gerente" or "1":
            View.mostrar_menu_gerente()
        elif funcao == "Funcionário" or "2":
            View.mostrar_menu_funcionario()
        else: print("Voce não digitou algo valido")

    @staticmethod
    def solicitar_dados_cadastro_livro():
        titulo = input("Título do livro: ")
        isbn = input("ISBN: ")
        editora = input("Editora: ")
        ano = input("Ano de publicação: ")
        autores = input("Autores (separados por vírgula): ").split(",")
        id_livro = input("Identificador único do livro: ")
        num_exemplares = int(input("Número de exemplares: "))
        return titulo, isbn, editora, ano, autores, id_livro, num_exemplares
    
    @staticmethod
    def cadastrar_livro():
        dados_livro = View.solicitar_dados_cadastro_livro()
        Controller.cadastrar_livro(*dados_livro)

    @staticmethod
    def solicitar_dados_cadastro_revista():
        titulo = input("Título da revista: ")
        issn = input("ISSN: ")
        editoras = input("Editoras (separadas por vírgula): ").split(",")
        ano = input("Ano de publicação: ")
        autor = input("Autor: ")
        volume = input("Volume: ")
        id_revista = input("Identificador único da revista: ")
        num_exemplares = int(input("Número de exemplares: "))
        return titulo, issn, editoras, ano, autor, volume, id_revista, num_exemplares
    
    @staticmethod
    def cadastrar_revista():
        dados_revista = View.solicitar_dados_cadastro_revista()
        Controller.cadastrar_revista(*dados_revista)

    @staticmethod
    def solicitar_dados_cadastro_tese():
        titulo = input("Título da tese: ")
        programa = input("Programa de pós-graduação: ")
        autor = input("Autor: ")
        orientador = input("Orientador: ")
        coorientador = input("Coorientador: ")
        ano = input("Ano de publicação: ")
        id_tese = input("Identificador único da tese: ")
        return titulo, programa, autor, orientador, coorientador, ano, id_tese
    
    @staticmethod
    def cadastrar_tese():
        dados_tese = View.solicitar_dados_cadastro_tese()
        Controller.cadastrar_tese(*dados_tese)

    @staticmethod
    def solicitar_dados_cadastro_usuario():
        nome = input("Nome do usuário: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        filiacao = input("Filiação (departamento ou curso): ")
        nascimento = input("Data de nascimento: ")
        categoria = input("Categoria (Aluno de graduação, Aluno de pós-graduação, Professor, Funcionário): ")
        return nome, email, telefone, filiacao, nascimento, categoria
    
    @staticmethod
    def cadastrar_usuario():
        dados_usuario = View.solicitar_dados_cadastro_usuario()
        Controller.cadastrar_usuario(*dados_usuario)
    
    @staticmethod
    def realizar_emprestimo():
        id_exemplar = input("ID do exemplar: ")
        id_usuario = input("ID do usuário: ")
        Controller.realizar_emprestimo(id_exemplar, id_usuario)

    @staticmethod
    def renovar_emprestimo():
        id_emprestimo = input("ID do empréstimo: ")
        Controller.renovar_emprestimo(id_emprestimo)

    @staticmethod
    def registrar_devolucao():
        id_emprestimo = input("ID do empréstimo: ")
        data_devolucao = input("Data de devolução (formato YYYY-MM-DD): ")
        Controller.registrar_devolucao(id_emprestimo, data_devolucao)

    @staticmethod
    def adicionar_usuario_lista_espera():
        id_item = input("ID do item: ")
        id_usuario = input("ID do usuário: ")
        Controller.adicionar_usuario_a_fila_espera(id_item, id_usuario)

    @staticmethod
    def mostrar_opcoes_menu1():
        print("\n===== Menu =====")
        print("1. Cadastrar usuário")
        print("2. Realizar empréstimo")
        print("3. Renovar empréstimo")
        print("4. Registrar devolução")        
        print("5. Adicionar usuário à lista de espera")
        print("6. Exibir lista de espera")
        print("7. Exibir relação de livros emprestados")        
        print("8. Listar os 50 mais emprestados")
        print("9. Quantidade de livros emprestados no mês")
        print("10. Quantidade de livros emprestados por semana")
        print("11. Quantidade de livros emprestados por dia")
        print("12. Quantidade de dias em atraso por livro")
        print("13. Cadastrar livro")
        print("14. Cadastrar revista")
        print("15. Cadastrar tese")
        print("0. Sair\n")

    @staticmethod
    def mostrar_opcoes_menu2():
        print("\n===== Menu =====")
        print("1. Cadastrar usuário")
        print("2. Realizar empréstimo")
        print("3. Renovar empréstimo")
        print("4. Registrar devolução")        
        print("5. Adicionar usuário à lista de espera")
        print("6. Exibir lista de espera")
        print("7. Exibir relação de livros emprestados")        
        print("8. Listar os 50 mais emprestados")
        print("9. Quantidade de livros emprestados no mês")
        print("10. Quantidade de livros emprestados por semana")
        print("11. Quantidade de livros emprestados por dia")
        print("12. Quantidade de dias em atraso por livro")
        print("0. Sair\n")        

    @staticmethod
    def solicitar_opcao_menu():
        return input("Digite a opção desejada: \n")




    @staticmethod
    def listar_50_mais_emprestados():
        mais_emprestados = Controller.listar_50_mais_emprestados()
        print("\n===== 50 mais emprestados =====")
        for item in mais_emprestados:
            print(item)

    @staticmethod
    def quantidade_livros_emprestados_mes():
        quantidade = Controller.quantidade_livros_emprestados_mes()
        print(f"\nQuantidade de livros emprestados no mês: {quantidade}\n")

    @staticmethod
    def quantidade_livros_emprestados_semana():
        quantidade = Controller.quantidade_livros_emprestados_semana()
        print(f"\nQuantidade de livros emprestados por semana: {quantidade}\n")

    @staticmethod
    def quantidade_livros_emprestados_dia():
        quantidade = Controller.quantidade_livros_emprestados_dia()
        print(f"\nQuantidade de livros emprestados por dia: {quantidade}\n")

    @staticmethod
    def quantidade_dias_atraso_por_livro():
        atraso_por_livro = Controller.quantidade_dias_atraso_por_livro()
        print("\n===== Quantidade de dias de atraso por livro =====")
        for livro, dias in atraso_por_livro.items():
            print(f"Livro {livro}: {dias} dias de atraso")

    @staticmethod
    def exibir_relacao_livros_emprestados(relacao):
        print("\n===== Relação de livros emprestados =====")
        for emprestimo in relacao:
            print(f"Item: {emprestimo.exemplar.id_item} - Data de empréstimo: {emprestimo.data_inicio} - Data de devolução: {emprestimo.data_fim if emprestimo.data_fim else 'Não devolvido'}")

    @staticmethod
    def exibir_lista_espera(lista):
        print("\n===== Lista de espera =====")
        for item, usuarios in lista.items():
            print(f"Item: {item} - Usuários na lista de espera: {', '.join(usuarios)}")


    @staticmethod
    def mostrar_menu_funcionario():
        while True:
            View.mostrar_opcoes_menu2()
            opcao = View.solicitar_opcao_menu()
            if opcao == "1":
                View.cadastrar_usuario()
            elif opcao == "2":
                View.realizar_emprestimo()
            elif opcao == "3":
                View.renovar_emprestimo()
            elif opcao == "4":
                View.registrar_devolucao()
            elif opcao == "5":
                View.adicionar_usuario_lista_espera()  
            elif opcao == "6":
                View.exibir_lista_espera(Controller.obter_lista_espera())  # Passar a lista de espera como argumento
            elif opcao == "7":
                View.exibir_relacao_livros_emprestados(Controller.obter_relacao_livros_emprestados())  # Passar a relação de livros emprestados como argumento
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

    @staticmethod
    def mostrar_menu_gerente():
        while True:
            View.mostrar_opcoes_menu1()
            opcao = View.solicitar_opcao_menu()
            if opcao == "1":
                View.cadastrar_usuario()
            elif opcao == "2":
                View.realizar_emprestimo()
            elif opcao == "3":
                View.renovar_emprestimo()
            elif opcao == "4":
                View.registrar_devolucao()
            elif opcao == "5":
                View.adicionar_usuario_lista_espera() 
            elif opcao == "6":
                View.exibir_lista_espera(Controller.obter_lista_espera())  # Passar a lista de espera como argumento
            elif opcao == "7":
                View.exibir_relacao_livros_emprestados(Controller.obter_relacao_livros_emprestados())  
            elif opcao == "8":
                View.listar_50_mais_emprestados() 
            elif opcao == "9":
                View.quantidade_livros_emprestados_mes() 
            elif opcao == "10":
                View.quantidade_livros_emprestados_semana() 
            elif opcao == "11":
                View.quantidade_livros_emprestados_dia()
            elif opcao == "12":
                View.quantidade_dias_atraso_por_livro() 
            elif opcao == "13":
                View.cadastrar_livro()
            elif opcao == "14":
                View.cadastrar_revista()
            elif opcao == "15":
                View.cadastrar_tese()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")