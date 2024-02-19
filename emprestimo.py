import datetime
from datetime import timedelta
from exemplar import Exemplar
from usuario import Usuario
from fila_espera import FilaDeEspera
from livro import Livro


class Emprestimo:

    livros_emprestados={}
    emprestimos = []

    def __init__(self, exemplar, usuario, data_inicio, data_fim=None, data_devolucao=None, valor_multa=0, situacao_multa=None):
        # Lógica para emprestar o livro ao usuário
        #print(f"dados user: ",vars(usuario))
        #print(f"dados exemplar: ",vars(exemplar))
        if exemplar.esta_disponivel():
            #exemplar.disponivel = False
            #print("rodou o exemplar.esta_disponivel() \n")

            if isinstance(usuario, Usuario):
                data_fim = data_inicio + timedelta(days=usuario.dias_emprestimos)
                if len(usuario.livros_emprestados) < usuario.quantidade_livros_max :
                    #print(usuario.livros_emprestados)                    
                    if usuario.tem_livro_em_atraso():
                        print("Você possui pelo menos um livro em atraso. Não é possível emprestar o livro.")
                    else:
                        self.exemplar = exemplar
                        self.usuario = usuario
                        self.categoria_user = usuario.categoria
                        self.data_inicio = data_inicio
                        self.data_fim = data_fim
                        self.data_devolucao = data_devolucao
                        self.valor_multa = valor_multa
                        self.situacao_multa = situacao_multa

                        # Atualiza o registro de livros emprestados
                        if self not in self.livros_emprestados:
                            self.livros_emprestados[self] = 1
                        else:
                            self.livros_emprestados[self] += 1

                        # Adiciona o livro na lista de emprestados por data
                        self.emprestimos.append(self)
                        
                        print("Livro emprestado com sucesso. \n")
                        
                else:
                    print("Você atingiu o número máximo de livros. Não é possível emprestar o livro. \n")                
        else:
            print("Este exemplar não está disponível para empréstimo. \n")


    def calcular_multa(self, data_atual):
        if self.data_devolucao is None:
            return 0

        dias_atraso = (data_atual - self.data_fim).days
        if dias_atraso > 0:
            multa_base = 2.50
            multa_por_dia = multa_base * (2 ** (dias_atraso // 30))  # Dobrar a multa a cada 30 dias de atraso
            return multa_por_dia * dias_atraso
        else:
            return 0

    def pagar_multa(self):
        self.valor_multa = 0
        self.situacao_multa = "Paga"
        print("Multa paga com sucesso. \n")

    def renovar(self, lista_espera):
        """Renova um empréstimo, se possível."""    
        nova_data_fim = self.data_fim + timedelta(days=self.usuario.dias_emprestimos)
        if nova_data_fim > self.data_fim:
            if not self.usuario.tem_livro_em_atraso():
                if not lista_espera.verificar_livro(self.exemplar.id_item) or lista_espera.fila==[]:
                    self.data_fim = nova_data_fim
                    print("Empréstimo renovado com sucesso. \n")
                else:
                    print("Há pessoas na lista de espera para este livro. Não é possível renovar o empréstimo. \n")
            else:
                print("Não é possível renovar o empréstimo devido a livros em atraso. \n")
        else:
            print("A nova data de devolução deve ser posterior à data atual. \n")

    def devolver(self, data_devolucao):
        self.data_devolucao = data_devolucao
        if self.data_devolucao > self.data_fim:
            multa = self.calcular_multa(data_devolucao)
            if multa > 0:
                self.valor_multa = multa
                self.situacao_multa = "pendente"
                self.usuario.multas[self.id_exemplar] = multa
                print(f"Item devolvido com sucesso. Multa aplicada: R${multa:.2f}\n")
            else:
                print("Item devolvido com sucesso. \n")
        else:
            print("Item devolvido com sucesso. \n")

    @staticmethod
    def listar_livros_emprestados():
        for emprestimo in Emprestimo.emprestimos:
            titulo_livro = Livro.procurar_livro_por_id(emprestimo.exemplar.id_item)
            if titulo_livro:
                print(f"Usuário: {emprestimo.usuario.nome}")
                print(f"Título: {titulo_livro}")
                print(f"Id do item emprestado: {emprestimo.exemplar.id_item}.{emprestimo.exemplar.id_exemplar}")
                print(f"Data de início do empréstimo: {emprestimo.data_inicio}")
                print(f"Data de fim do empréstimo: {emprestimo.data_fim}")
                if emprestimo.data_devolucao:
                    print(f"Data de devolução: {emprestimo.data_devolucao} \n")
                else:
                    print("Item ainda não devolvido. \n")
        print("\n")
    
    '''def mostrar_livro_emprestado(self):
        print(f"Usuário: {self.usuario.nome}")
        #id=self.exemplar.id_item
        print(f"Id do item emprestado: {self.exemplar.id_item}.{self.exemplar.id_exemplar}")
        #print(Livro.procurar_livro_por_id(self,id))        
        print(f"Data de início do empréstimo: {self.data_inicio}")
        print(f"Data de fim do empréstimo: {self.data_fim}")
        if self.data_devolucao:
            print(f"Data de devolução: {self.data_devolucao} \n")
        else:
            print("Item ainda não devolvido. \n")'''

    @classmethod
    def listar_50_mais_emprestados(cls):
        # Classifica os livros emprestados com base no número de empréstimos
        livros_sorted = sorted(cls.livros_emprestados.items(), key=lambda x: x[1], reverse=True)
        # Retorna os IDs dos 50 livros mais emprestados
        ids_50_mais_emprestados = [livro[0] for livro in livros_sorted[:50]]
        
        # Retorna os títulos dos 50 livros mais emprestados
        titulos_50_mais_emprestados = []
        for emprestimo in ids_50_mais_emprestados:
            titulo = Livro.procurar_livro_por_id(emprestimo.exemplar.id_item)
            if titulo:
                titulos_50_mais_emprestados.append(titulo)
        
        return titulos_50_mais_emprestados
    
    @staticmethod
    def quantidade_livros_emprestados_mes():
        # Obtém o mês atual
        mes_atual = datetime.datetime.now().month
        
        # Contador de empréstimos no mês atual
        contador_emprestimos_mes = 0
        for emprestimo in Emprestimo.emprestimos:
            # Verifica se o empréstimo ocorreu no mês atual
            if emprestimo.data_inicio.month == mes_atual:
                contador_emprestimos_mes += 1
        return contador_emprestimos_mes

    @staticmethod
    def quantidade_livros_emprestados_semana():
        # Obtém a data atual
        data_atual = datetime.datetime.now()
        # Obtém o número da semana atual
        semana_atual = data_atual.isocalendar()[1]

        # Dicionário para manter contagem de empréstimos por semana
        emprestimos_por_semana = {}
        for emprestimo in Emprestimo.emprestimos:
            semana_emprestimo = emprestimo.data_inicio.isocalendar()[1]
            if semana_emprestimo not in emprestimos_por_semana:
                emprestimos_por_semana[semana_emprestimo] = 1
            else:
                emprestimos_por_semana[semana_emprestimo] += 1
        return emprestimos_por_semana

    @staticmethod
    def quantidade_livros_emprestados_dia():
        # Dicionário para manter contagem de empréstimos por dia da semana
        emprestimos_por_dia = {}
        for emprestimo in Emprestimo.emprestimos:
            dia_semana = emprestimo.data_inicio.strftime("%A")
            if dia_semana not in emprestimos_por_dia:
                emprestimos_por_dia[dia_semana] = 1
            else:
                emprestimos_por_dia[dia_semana] += 1
        return emprestimos_por_dia
    
    @staticmethod
    def quantidade_dias_atraso_por_livro():
        # Dicionário para manter a contagem de dias em atraso por livro
        dias_atraso_por_livro = {}

        # Obtém a data atual
        data_atual = datetime.datetime.now()

        for emprestimo in Emprestimo.emprestimos:
            if emprestimo.data_devolucao and emprestimo.data_devolucao > emprestimo.data_fim:
                dias_atraso = (emprestimo.data_devolucao - emprestimo.data_fim).days
                id_item_emprestado = emprestimo.exemplar.id_item
                titulo_livro = Livro.procurar_livro_por_id(id_item_emprestado)
                if titulo_livro:
                    if titulo_livro not in dias_atraso_por_livro:
                        dias_atraso_por_livro[titulo_livro] = dias_atraso
                    else:
                        dias_atraso_por_livro[titulo_livro] += dias_atraso
        if dias_atraso_por_livro=={}:
            print("Não há livros em atraso \n")                

        return dias_atraso_por_livro
