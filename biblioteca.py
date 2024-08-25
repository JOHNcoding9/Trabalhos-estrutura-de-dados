# criar um sistema simples de gerenciamento de livros em uma biblioteca.
# implementar três classes principais: Livro, Usuario, e
# Biblioteca. A classe Livro representa os livros da biblioteca, a classe Usuario representa
# as pessoas que pegam emprestado os livros, e a classe Biblioteca gerencia o processo
# de empréstimo de livros.

# criando as classes
class Livro:
    def __init__(self,autor,titulo,disponivel = True):
        self.autor = autor
        self.titulo = titulo
        self.disponivel = disponivel
    def __repr__(self):
     # Representação personalizada do livro para não devolver no terminal algo como :<__main__.Livro object at 0x0000023A75944B50>
     status = "Disponível" if self.disponivel else "Não disponível"
     return f'"{self.titulo}" por {self.autor} - {status}'
    def exibir_detalhes(self):
        if self.disponivel:
            print("Livro disponível")
        else:
            print("Livro não disponivel no momento")
        print(f"Autor: {self.autor}")
        print(f"Título: {self.titulo}")

class Usuario:
    def __init__(self,nome):
        self.nome = nome
        self.emprestado = []
    def emprestar_livro(self,livro):
        if livro in biblioteca.livros and livro.disponivel:
         livro.disponivel = False
         self.emprestado.append(livro)
         print(f"livro pego com sucesso: {livro.titulo}")
        else:
            print("livro não disponível para emprestar")
    def devolver_livro(self,livro):
        if livro in self.emprestado and not livro.disponivel:
         livro.disponivel = True
         self.emprestado.remove(livro)
         print(f"livro devolvido com sucesso: {livro.titulo}")

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
    def adicionar_livro(self,livro):
        self.livros.append(livro)
        print(f"Livro {livro.titulo} adicionado a biblioteca")
    def exibir_livro_disponível(self):
        print(f"Lista antes dos empréstimos")
        print(self.livros)
        print("="*30)
        livros_disponiveis = [livro for livro in self.livros if livro.disponivel]
        print(f"Lista depois de todos os dos empréstimos")
        print(livros_disponiveis)



# criando os objetos
livro_1 = Livro("George Orwell","1984",disponivel =True)
livro_2 = Livro("J.R.R. Tolkien","O Senhor dos Anéis",disponivel = True)
livro_3 = Livro("Jane Austen","Orgulho e Preconceito",disponivel = False)
livro_4 = Livro("Harper Lee","Matar a Mockingbird",disponivel = False)
livro_5 = Livro("F. Scott Fitzgerald","O Grande Gatsby",disponivel = True)
livro_6 = Livro("J.D. Salinger","O Apanhador no Campo de Centeio",disponivel = True)
livro_7 = Livro("Markus Zusak","A Menina que Roubava Livros",disponivel = True)
livro_8 = Livro("Yuval Noah Harari","Sapiens: Uma Breve História da Humanidade",disponivel = True)
livro_9 = Livro("Dan Brown","O Código Da Vinci",disponivel = False)
livro_10 = Livro("Patrick Rothfuss","O Nome do Vento",disponivel = True)
livro_11 = Livro("Franz Kafka","O Processo",disponivel = True)

# criando o objeto biblioteca 
biblioteca = Biblioteca("Biblioteca do Sul")
# adicionar livros para a biblioteca
biblioteca.adicionar_livro(livro_1)
biblioteca.adicionar_livro(livro_2)
biblioteca.adicionar_livro(livro_3)
biblioteca.adicionar_livro(livro_4)
biblioteca.adicionar_livro(livro_5)
biblioteca.adicionar_livro(livro_6)
biblioteca.adicionar_livro(livro_7)
biblioteca.adicionar_livro(livro_8)
biblioteca.adicionar_livro(livro_9)
biblioteca.adicionar_livro(livro_10)
biblioteca.adicionar_livro(livro_11)

# criando usuário
usuario = Usuario("João")
usuario_2 = Usuario("Isa")

#teste detalhes
livro_1.exibir_detalhes()
livro_4.exibir_detalhes()
# teste emprestar
usuario.emprestar_livro(livro_5)
usuario.emprestar_livro(livro_2)
usuario.devolver_livro(livro_5)
#teste exibir
biblioteca.exibir_livro_disponível()
#teste usuario 2
usuario_2.emprestar_livro(livro_5)
usuario_2.emprestar_livro(livro_3)
usuario_2.emprestar_livro(livro_6)
usuario_2.devolver_livro(livro_6)
# teste exibir
biblioteca.exibir_livro_disponível()