from exemplar import Exemplar
from item import Item

class Tese(Item):
    def __init__(self, titulo, programa, autor, orientador, coorientador, ano, id_tese): #método cadastrar
        super().__init__(titulo, ano, id_tese)
        self.programa = programa
        self.autor = autor
        self.orientador = orientador
        self.coorientador = coorientador

        with open("teses.txt", "a") as arquivo:
            arquivo.write(self + "\n")
        print("Tese cadastrada com sucesso.\n")

        

    def consultar(self):
        # Lógica para consultar informações de uma tese
        print(f'Informações da tese "{self.titulo}":')
        print(f"Título: {self.titulo}")
        print(f"Programa de Pós-Graduação: {self.programa}")
        print(f"Autor: {self.autor}")
        print(f"Orientador: {self.orientador}")
        print(f"Coorientador: {self.coorientador}")
        print(f"Ano: {self.ano}")
        print(f"ID: {self.id_item}")
