class Exemplar:
    def __init__(self, id_exemplar, id_item):
        self.id_exemplar = id_exemplar
        self.id_item = id_item
        self.disponivel = True
        
    def esta_disponivel(self):
        """Verifica se o exemplar está disponível para empréstimo."""
        return self.disponivel

    def emprestar(self):
        """Marca o exemplar como emprestado."""
        if self.disponivel:
            self.disponivel = False
            print("Exemplar emprestado com sucesso. \n")
        else:
            print("Exemplar já emprestado. \n")

    def devolver(self):
        """Marca o exemplar como devolvido."""
        if not self.disponivel:
            self.disponivel = True
            print("Exemplar devolvido com sucesso. \n")
        else:
            print("Exemplar já está disponível. \n")