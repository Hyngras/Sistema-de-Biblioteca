from datetime import datetime
from livro import Livro

class Usuario:
    def __init__(self, nome, email, telefone, filiacao, nascimento, categoria):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.filiacao = filiacao
        self.nascimento = nascimento
        self.categoria = categoria
        self.livros_emprestados = []  # Lista de livros emprestados
        # multas acessado pela lista mesmo

        if self.categoria == "Aluno de graduacao":
            self.dias_emprestimos = 7
            self.quantidade_livros_max = 5
        elif self.categoria == "Aluno de pós-graduacao":
            self.dias_emprestimos = 15
            self.quantidade_livros_max = 9
        elif self.categoria == "Professor":
            self.dias_emprestimos = 60
            self.quantidade_livros_max = 15
        
        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"{self.nome},{self.email},{self.telefone},{self.filiacao},{self.nascimento},{self.categoria}\n")
        print(f'\nUsuário(a) {self.nome} foi cadastrado com sucesso.\n')


    def consultar(self):
        # Lógica para consultar informações de um usuário
        print(f'Informações do usuário {self.nome}:')
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Filiação: {self.filiacao}")
        print(f"Nascimento: {self.nascimento}")
        print(f"Categoria: {self.categoria} \n")

    def adicionar_emprestimo(self, emprestimo):
        self.livros_emprestados.append(emprestimo)
        print("\nlivro adicionado na lista do usuario \n")
        
        #self.quantidade_livros += 1
    
    def exibir_lista_do_usuario(self):
        print("\nRegistro de empréstimos do usuário:")
        for emprestimo in self.livros_emprestados:
            livro = Livro.procurar_livro_por_id(emprestimo.exemplar.id_item)
            data_inicio = emprestimo.data_inicio.strftime("%d/%m/%Y")
            data_devolucao = emprestimo.data_devolucao.strftime("%d/%m/%Y") if emprestimo.data_devolucao else "Ainda não devolvido"
            print(f"Livro: {livro} | Data de retirada: {data_inicio} | Data de devolução: {data_devolucao}")

    def exibir_lista_multas_do_usuario(self):
        print("\nRegistro de multas do usuário:")
        for emprestimo in self.livros_emprestados:
            livro = Livro.procurar_livro_por_id(emprestimo.exemplar.id_item)
            valor_multa = emprestimo.valor_multa
            situacao_multa = emprestimo.situacao_multa
            if situacao_multa == "Paga":
                print(f"Multas pagas para o livro {livro}: R${valor_multa:.2f}")
            elif situacao_multa == "Pendente":
                print(f"Multas pendentes para o livro {livro}: R${valor_multa:.2f}")  

    def entrar_na_fila(self, fila_espera, id_livro):
        fila_espera.entrar(id_livro, self.id)

    def renovar_livro(self, nova_data_fim, emprestimo):
        #Renova um livro emprestado, se possível.
        emprestimo.renovar(self, nova_data_fim)

    def tem_livro_em_atraso(self):
        data_atual = datetime.now()
        for emprestimo in self.livros_emprestados:
            if emprestimo.data_fim and emprestimo.data_fim < data_atual and emprestimo.data_devolucao == None:
                return True
        return False

    def pesquisar_livro(self):
        # Lógica para pesquisar livros no sistema (?)
        pass
