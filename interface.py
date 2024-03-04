import tkinter as tk
from tkinter import simpledialog
from view import View
from controller import Controller

class InterfaceBiblioteca:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Para o Gerenciamento da Biblioteca")
        self.janela.configure(bg="light blue")  # Altera a cor de fundo da janela
        self.controller = Controller()  # Instanciando o controlador

        # Criar a primeira tela
        self.criar_primeira_tela()

    def criar_primeira_tela(self):
        self.label_titulo = tk.Label(self.janela, text="Bem-vindo ao Sistema da Biblioteca", font=("Helvetica", 30))
        self.label_titulo.pack(pady=40)

        self.botao_gerente = tk.Button(self.janela, text="Gerente", command=self.menu_gerente, font=("Helvetica", 20))
        self.botao_gerente.pack(pady=10)

        self.botao_funcionario = tk.Button(self.janela, text="Funcionário", command=self.menu_funcionario, font=("Helvetica", 20))
        self.botao_funcionario.pack(pady=10)
    
    def menu_gerente(self):
        self.limpar_tela()
        self.label_titulo.config(text="Menu do Gerente")
        opcoes = ["Cadastrar usuário", "Realizar empréstimo", "Renovar empréstimo",
                         "Registrar devolução", "Adicionar usuário à lista de espera", "Exibir lista de espera",
                         "Exibir relação de livros emprestados", "Listar os 50 mais emprestados",
                         "Quantidade de livros emprestados no mês", "Quantidade de livros emprestados por semana",
                         "Quantidade de livros emprestados por dia", "Quantidade de dias em atraso por livro",
                         "Cadastrar livro", "Cadastrar revista", "Cadastrar tese", "Sair"]

        for opcao in opcoes:
            botao = tk.Button(self.janela, text=opcao, command=lambda opcao=opcao: self.acao_gerente(opcao))
            botao.pack(pady=2)
            
    def menu_funcionario(self):
        self.limpar_tela()
        self.label_titulo.config(text="Menu do Funcionário")
        opcoes = ["Cadastrar usuário", "Realizar empréstimo", "Renovar empréstimo",
                         "Registrar devolução", "Adicionar usuário à lista de espera", "Exibir lista de espera",
                         "Quantidade de dias em atraso por livro", "Sair"]
        for opcao in opcoes:
            botao = tk.Button(self.janela, text=opcao, command=lambda opcao=opcao: self.acao_funcionario(opcao))
            botao.pack(pady=2)        
            
    def acao_gerente(self, opcao):
        if opcao == "Cadastrar usuário":
            self.cadastrar_usuario()
        elif opcao == "Realizar empréstimo":
            self.realizar_emprestimo()
        elif opcao == "Renovar empréstimo":
            self.renovar_emprestimo()
        elif opcao == "Registrar devolução":
            self.registrar_devolucao()
        elif opcao == "Adicionar usuário à lista de espera":
            self.adicionar_lista_espera()
        elif opcao == "Exibir lista de espera":
            self.exibir_lista_espera()
        elif opcao == "Exibir relação de livros emprestados":
            self.exibir_livros_emprestados()
        elif opcao == "Listar os 50 mais emprestados":
            self.listar_50_mais_emprestados()
        elif opcao == "Quantidade de livros emprestados no mês":
            self.quantidade_emprestados_mes()
        elif opcao == "Quantidade de livros emprestados por semana":
            self.quantidade_emprestados_semana()
        elif opcao == "Quantidade de livros emprestados por dia":
            self.quantidade_emprestados_dia()
        elif opcao == "Quantidade de dias em atraso por livro":
            self.quantidade_dias_atraso_livro()
        elif opcao == "Cadastrar livro":
            self.cadastrar_livro()
        elif opcao == "Cadastrar revista":
            self.cadastrar_revista()
        elif opcao == "Cadastrar tese":
            self.cadastrar_tese()
        elif opcao == "Sair":
            self.janela.quit()

    def acao_funcionario(self, opcao):
        if opcao == "Cadastrar usuário":
            self.cadastrar_usuario()
        elif opcao == "Realizar empréstimo":
            self.realizar_emprestimo()
        elif opcao == "Renovar empréstimo":
            self.renovar_emprestimo()
        elif opcao == "Registrar devolução":
            self.registrar_devolucao()
        elif opcao == "Adicionar usuário à lista de espera":
            self.adicionar_lista_espera()
        elif opcao == "Exibir lista de espera":
            self.exibir_lista_espera()
        elif opcao == "Exibir relação de livros emprestados":
            self.exibir_livros_emprestados()
        elif opcao == "Listar os 50 mais emprestados":
            self.listar_50_mais_emprestados()
        elif opcao == "Quantidade de dias em atraso por livro":
            self.quantidade_dias_atraso_livro()
        elif opcao == "Sair":
            self.janela.quit()

    def cadastrar_usuario(self):
        nome = simpledialog.askstring("Cadastrar Usuário", "Nome do usuário:")
        email = simpledialog.askstring("Cadastrar Usuário", "Email:")
        telefone = simpledialog.askstring("Cadastrar Usuário", "Telefone:")
        filiacao = simpledialog.askstring("Cadastrar Usuário", "Filiação (departamento ou curso):")
        data_nascimento = simpledialog.askstring("Cadastrar Usuário", "Data de nascimento:")
        categoria = simpledialog.askstring("Cadastrar Usuário", "Categoria (Aluno de graduação, Aluno de pós-graduação, Professor, Funcionário):")

        # Chamar o método da classe Controller para cadastrar o usuário
        self.controller.cadastrar_usuario(nome, email, telefone, filiacao, data_nascimento, categoria)

    def registrar_devolucao(self):
        id_emprestimo = simpledialog.askstring("Registrar Devolução", "ID do empréstimo:")
        data_devolucao = simpledialog.askstring("Registrar Devolução", "Data de devolução:")

    def registrar_devolucao(self):
        id_emprestimo = simpledialog.askstring("Registrar Devolução", "ID do empréstimo:")
        data_devolucao = simpledialog.askstring("Registrar Devolução", "Data de devolução:")

        # Chamar o método da classe Controller para registrar a devolução
        self.controller.registrar_devolucao(id_emprestimo, data_devolucao)

    def realizar_emprestimo(self):
        id_exemplar = simpledialog.askstring("Realizar Empréstimo", "ID do exemplar:")
        id_usuario = simpledialog.askstring("Realizar Empréstimo", "ID do usuário:")

        # Chamar o método da classe Controller para realizar o empréstimo
        self.controller.realizar_emprestimo(id_exemplar, id_usuario)

    def renovar_emprestimo(self):
        id_emprestimo = simpledialog.askstring("Renovar Empréstimo", "ID do empréstimo:")

        # Chamar o método da classe Controller para renovar o empréstimo
        self.controller.renovar_emprestimo(id_emprestimo)

    def exibir_lista_espera(self):
        # Chamar o método da classe Controller para exibir a lista de espera
        lista_espera = self.controller.obter_lista_espera()
        View.exibir_lista_espera(lista_espera)

    def exibir_livros_emprestados(self):
        # Chamar o método da classe Controller para exibir a relação de livros emprestados
        livros_emprestados = self.controller.obter_relacao_livros_emprestados()
        View.exibir_relacao_livros_emprestados(livros_emprestados)

    def listar_50_mais_emprestados(self):
        # Chamar o método da classe Controller para listar os 50 mais emprestados
        mais_emprestados = self.controller.listar_50_mais_emprestados()
        View.listar_50_mais_emprestados(mais_emprestados)

    def quantidade_emprestados_mes(self):
        # Chamar o método da classe Controller para calcular a quantidade de livros emprestados no mês
        quantidade = self.controller.quantidade_livros_emprestados_mes()
        View.quantidade_livros_emprestados_mes(quantidade)

    def quantidade_emprestados_semana(self):
        # Chamar o método da classe Controller para calcular a quantidade de livros emprestados por semana
        quantidade = self.controller.quantidade_livros_emprestados_semana()
        View.quantidade_livros_emprestados_semana(quantidade)

    def quantidade_emprestados_dia(self):
        # Chamar o método da classe Controller para calcular a quantidade de livros emprestados por dia
        quantidade = self.controller.quantidade_livros_emprestados_dia()
        View.quantidade_livros_emprestados_dia(quantidade)

    def quantidade_dias_atraso_livro(self):
        # Chamar o método da classe Controller para calcular a quantidade de dias de atraso por livro
        atraso_por_livro = self.controller.quantidade_dias_atraso_por_livro()
        View.quantidade_dias_atraso_por_livro(atraso_por_livro)

    def cadastrar_livro(self):
        # Chamar o método da classe View para cadastrar um livro
        View.cadastrar_livro()

    def cadastrar_revista(self):
        # Chamar o método da classe View para cadastrar uma revista
        View.cadastrar_revista()

    def cadastrar_tese(self):
        # Chamar o método da classe View para cadastrar uma tese
        View.cadastrar_tese()

    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            if widget != self.label_titulo:
                widget.destroy()


# Criar a janela principal
janela_principal = tk.Tk()

# Inicializar a interface da biblioteca
interface = InterfaceBiblioteca(janela_principal)

# Iniciar o loop principal da interface gráfica
janela_principal.mainloop()

# Chamar o método da classe Controller para registrar a devolução
       

