from view import View

def main():
    '''
    #testes
    livro1 = Livro("Python Programming", "978-0-13-446379-3", "Editora A", 2020, ["John Doe"], 1)
    livro2 = Livro("Python for Beginners", "978-1-987654-32-1", "Editora A", 2020, ["John Smith"], 2)
    #livro3 = "Introducao a Biologia Molecular,978-0321811851,Pearson,2012,[Maurice R. Strum,John Doe],3
    exemplares_livro1 = [Exemplar(1, 1), Exemplar(2, 1)]
    exemplares_livro2 = [Exemplar(1, 2), Exemplar(2, 2), Exemplar(3,2)]
    livro1.cadastrar(exemplares_livro1)
    livro2.cadastrar(exemplares_livro2)
    livro1.consultar()
    livro2.consultar()


    # Exemplo de usuario
    usuario1 = Usuario("Joao Silva", "joao@example.com", "123456789", "Departamento X", "01/01/1990", "Aluno de graduacao")
    funcionario = Funcionario()
    funcionario.cadastrar_usuario(usuario1)
    usuario1.consultar()

    # Criando uma instância de Gerente
    gerente = Gerente()

    # Para usar o método cadastrar_usuario:
    usuario = Usuario(nome="ciclano", email="ciclano@example.com", telefone="987654321", filiacao="Departamento Y", nascimento="1999-01-01", categoria="Aluno de graduacao")
    arquivo_usuarios = "usuarios.txt"
    gerente.cadastrar_usuario(usuario, arquivo_usuarios)

    
    # Exemplo de cadastro de revista
    revista = "Journal of Biomedical Engineering,1234-5678,John Smith,ACM,2023,Volume 10,R0001"
    gerente.cadastrar_revista(revista)

    # Exemplo de cadastro de tese
    tese = "Development of Neural Prosthetics,Emily Johnson,Neuroscience,Dr. Robert Brown,Dr. Sarah White,2020"
    gerente.cadastrar_tese(tese)

    # Chamando o método emprestar livro
    #emprestimo = Emprestimo
    #exemplar = Exemplar(id_exemplar=1, id_item=1)
    exemplar = exemplares_livro1[0]
    emprestimo = Emprestimo(exemplar, usuario1, data_inicio=datetime.datetime.now())
    exemplar.emprestar()
    usuario1.adicionar_emprestimo(emprestimo)
    print(vars(emprestimo))
    
    #print(usuario1.livros_emprestados)    

    livro1.consultar()
    lista_espera = FilaDeEspera()
    lista_espera.entrar(1, usuario1)

    renovar = emprestimo.renovar(lista_espera)

    data_devolucao = datetime.datetime.now()
    emprestimo.devolver(data_devolucao)
    exemplar.devolver()

    #livro1.consultar()
    

    #lista_espera.listar_fila()
    #print(Livro.procurar_livro_por_id(1))
    #emprestimo.listar_livros_emprestados()

    print(Emprestimo.listar_50_mais_emprestados())

    print(f"{Emprestimo.quantidade_livros_emprestados_mes()} emprestimo no mês")
    # Para a contagem de empréstimos por semana
    contagem_semana = Emprestimo.quantidade_livros_emprestados_semana()
    for semana, quantidade in contagem_semana.items():
        print(f"Na semana {semana}, ocorreram {quantidade} empréstimos.")

    # Para a contagem de empréstimos por dia
    contagem_dia = Emprestimo.quantidade_livros_emprestados_dia()
    for dia, quantidade in contagem_dia.items():
        print(f"No dia {dia}, ocorreram {quantidade} empréstimos.")

    quantidade_dias_atraso = Emprestimo.quantidade_dias_atraso_por_livro()
    for livro, dias_atraso in quantidade_dias_atraso.items():
        print(f"{livro}: {dias_atraso} dias em atraso")

    #print(dir(usuario1.livros_emprestados))
    usuario1.exibir_lista_do_usuario()'''




if __name__ == "__main__":
    View.tela_entrada()