from exemplar import Exemplar
from item import Item

class Revista(Item):
    def __init__(self, titulo, issn, editoras, ano, autor, volume, id_revista):
        super().__init__(titulo, ano, id_revista)
        self.issn = issn
        self.editoras = editoras
        self.autor = autor
        self.volume = volume

    def cadastrar(self, nova_revista):
        with open("revistas.txt", "a") as arquivo:
            arquivo.write(nova_revista + "\n")
        print("Revista cadastrada com sucesso.\n")    

    def consultar(self):
        # Lógica para consultar informações de uma revista
        print(f'Informações da revista "{self.titulo}":')
        print(f"Título: {self.titulo}")
        print(f"ISSN: {self.issn}")
        print(f"Editoras: {', '.join(self.editoras)}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print(f"Volume: {self.volume}")
        print(f"ID: {self.id_item}")
