class Endereco:
    def __init__(self,rua, cidade):
        self.rua = rua
        self.cidade = cidade
    def mostrar_endereco(self):
        return f"{self.rua}.{self.cidade}"

class Pessoa:
    def __init__(self,nome,endereco):
        self.nome = nome
        self.endereco = endereco
    def mostrar_informacao(self):
        return f"{self.nome} mora em {self.endereco.mostrar_endereco()}"

endereco_maria = Endereco("Av. Principal","São Paulo")
maria = Pessoa("Maria",endereco_maria)

print(maria.mostrar_informacao()) 


class SistemaOperacional:
    def __init__(self, nome, versao):
        self.nome = nome
        self.versao = versao
        
    def mostrar_info(self):
        return f"Sistema: {self.nome} {self.versao}"

class Computador:
    def __init__(self, sistema):
        self.sistema = sistema
        
    def mostrar_info(self):
        return f"Computador com {self.sistema.mostrar_info()}"


windows = SistemaOperacional("Windows", "10")
linux = SistemaOperacional("Linux", "Ubuntu 20.04")
macos = SistemaOperacional("macOS", "Catalina")

computador_windows = Computador(windows)
computador_linux = Computador(linux)
computador_mac = Computador(macos)

print(computador_windows.mostrar_info())
print(computador_linux.mostrar_info())
print(computador_mac.mostrar_info())




    