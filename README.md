# Sistema-de-Biblioteca
Trabalho Técnicas Computacionais - POO
2024.02.19

### Descrição
Vocês terão que desenvolver um sistema de gerenciamento de bibliotecas que gerencia livros, revistas e teses. Segue a lista de requisitos mínimos do sistema:
  - Cada livro tem: título, ISBN, editora, ano de publicação, autores, identificador único do exemplar;
  - Cada revista tem: título, ISSN, autor, editoras, ano, volume e identificador único do exemplar;
  - Cada tese tem: título, autor, programa de pós-graduação, orientador, co-orientador, ano de publicação;
  - A biblioteca tem as categorias de usuários:
      - Aluno de graduação - pode retirar até 5 livros simultaneamente por uma semana cada;
      - Aluno de pós-graduação - pode retirar até 9 livros simultaneamente por quinze dias cada;
      - Professor - pode retirar até 15 livros simultaneamente por 60 dias;
      - Funcionário - pode realizar o empréstimo, a devolução e cadastrar novos usuários;
      - Gerente - pode fazer tudo que o funcionário faz e também cadastrar novos livros, revistas e teses;
  - Cada usuário deve ter: nome, email, telefone, filiação (departamento ou curso), data de nascimento, um registro de todos os livros que já emprestou com as datas de retirada e devolução, um registro de todas as multas que pagou ou que está em débito;
  - Há uma lista de espera para os livros mais concorridos onde os usuários podem entrar na lista quando os exemplares estiverem todos emprestados;
  - Cada usuário pode renovar os livros que emprestou dentro do prazo, a menos que esteja com, pelo menos, um livro em atraso ou que não haja pessoas na lista de espera para aquele item;
  - Há uma multa de R$2.50 por dia de atraso por livro. A cada 30 dias de atraso, a multa dobra de valor por dia;
  - O Sistema tem que mostrar as seguintes visualizações:
      - Relação dos livros que estão emprestados por data de empréstimo
      - Relação dos 50 livros mais emprestados
      - Relação das listas de espera
      - Quantidade de livros emprestados no mês
      - Quantidade de livros emprestados por semana e por dia
      - Quantidade de dias em atraso por livro
  - O sistema deve implementar a arquitetura MVC [Model View Controller]

## Execute o Main para rodar o código

