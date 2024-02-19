class FilaDeEspera:
    def __init__(self):
        self.fila = []

    def entrar(self, id_livro, id_usuario):
        # Verifica se o usuário já está na fila
        for entrada in self.fila:
            if entrada['id_usuario'] == id_usuario:
                print("Você já está na fila de espera. \n")
                return

        # Adiciona o usuário à fila de espera
        self.fila.append({'id_livro': id_livro, 'id_usuario': id_usuario})
        print("Você entrou na fila de espera com sucesso. \n")

    def sair(self, id_usuario):
        # Remove o usuário da fila de espera, se estiver presente
        for entrada in self.fila:
            if entrada['id_usuario'] == id_usuario:
                self.fila.remove(entrada)
                print("Você saiu da fila de espera. \n")
                return
        print("Você não está na fila de espera. \n")

    def verificar_livro(self, id_livro):
        for i in range(len(self.fila)):
            if id_livro == self.fila[i]['id_livro']:
                return True
        return False
    
    '''def verificar_usuario(self, id_livro, id_usuario):
        for i in range(len(self.fila)):
            if id_livro == self.fila[i]['id_livro']:
                return True
        return False'''

    def listar_fila(self):
        print("Fila de espera:")
        for i, entrada in enumerate(self.fila, start=1):
            print(f"{i}. Livro: {entrada['id_livro']}, Usuário: {(entrada['id_usuario'].nome)}\n") #aq ta o nome mas pode escolher outro atributo de usuario ou + de um
