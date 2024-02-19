from exemplar import Exemplar
from livro import Livro
from revista import Revista
from tese import Tese
from usuario import Usuario
from emprestimo import Emprestimo
from fila_espera import FilaDeEspera
import datetime


class Controller:
    @staticmethod
    def cadastrar_livro(titulo, isbn, editora, ano, autores, id_livro, num_exemplares):
        livro = Livro(titulo, isbn, editora, ano, autores, id_livro)
        exemplares = [Exemplar(i, id_livro) for i in range(1, num_exemplares + 1)]
        livro.cadastrar(exemplares)
    
    @staticmethod
    def cadastrar_revista(titulo, issn, editoras, ano, autor, volume, id_revista, num_exemplares):
        revista = Revista(titulo, issn, editoras, ano, autor, volume, id_revista)
        exemplares = [Exemplar(i, id_revista) for i in range(1, num_exemplares + 1)]
        revista.cadastrar(exemplares)

    @staticmethod
    def cadastrar_tese(titulo, programa, autor, orientador, coorientador, ano, id_tese):
        tese = Tese(titulo, programa, autor, orientador, coorientador, ano, id_tese)


    @staticmethod
    def cadastrar_usuario(nome, email, telefone, filiacao, nascimento, categoria):
        usuario = Usuario(nome, email, telefone, filiacao, nascimento, categoria)
        #usuario.cadastrar(usuario)

    @staticmethod
    def realizar_emprestimo(exemplar, usuario):
        emprestimo = Emprestimo(exemplar, usuario, data_inicio=datetime.datetime.now())
        exemplar.emprestar()
        usuario.adicionar_emprestimo(emprestimo)
        return emprestimo

    @staticmethod
    def adicionar_usuario_a_fila_espera(id_item, usuario):
        lista_espera = FilaDeEspera()
        lista_espera.entrar(id_item, usuario)

    @staticmethod
    def renovar_emprestimo(emprestimo, lista_espera):
        return emprestimo.renovar(lista_espera)

    @staticmethod
    def registrar_devolucao(emprestimo, data_devolucao):
        emprestimo.devolver(data_devolucao)
        exemplar = emprestimo.exemplar
        exemplar.devolver()

    @staticmethod
    def listar_50_mais_emprestados():
        return Emprestimo.listar_50_mais_emprestados()

    @staticmethod
    def quantidade_livros_emprestados_mes():
        return Emprestimo.quantidade_livros_emprestados_mes()

    @staticmethod
    def quantidade_livros_emprestados_semana():
        return Emprestimo.quantidade_livros_emprestados_semana()

    @staticmethod
    def quantidade_livros_emprestados_dia():
        return Emprestimo.quantidade_livros_emprestados_dia()

    @staticmethod
    def quantidade_dias_atraso_por_livro():
        return Emprestimo.quantidade_dias_atraso_por_livro()

    @staticmethod
    def exibir_relacao_livros_emprestados():
        Emprestimo.listar_livros_emprestados()

    @staticmethod
    def exibir_lista_espera():
        FilaDeEspera.listar_fila()