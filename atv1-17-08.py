class Autor:
    def __init__ (self,nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def mostrar_info(self):
        return f"Computador com {self.nome}, Data de Nascimento: {self.data_nascimento}"

charles_nome = Autor("Charles","30-07-2003")
print(charles_nome.mostrar_info())


class Livro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

    def mostra_info(self):
        return f"Livro '{self.titulo}' é do autor: {self.autor.mostrar_info()}"
    

autor_livro = Autor("Seila", "01-01-1990")
livro_nome = Livro("Harry Potter", autor_livro)
print(livro_nome.mostra_info())