class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}"

class Email(Documento):
    def __init__(self, titulo, conteudo, remetente, destinatario):
        super().__init__(titulo, conteudo)
        self.remetente = remetente
        self.destinatario = destinatario

    def exibir(self):
        doc_info = super().exibir()
        return f"{doc_info}, Remetente: {self.remetente}, Destinatário: {self.destinatario}"

class Relatorio(Documento):
    def __init__(self, titulo, conteudo, data):
        super().__init__(titulo, conteudo)
        self.data = data

    def exibir(self):
        doc_info = super().exibir()
        return f"{doc_info}, Data: {self.data}"

# Teste das classes
doc = Documento("Documento Genérico", "Este é um documento de teste.")
print(doc.exibir())

email = Email("Convite para a festa", "Olá! Você está convidado para a festa no sábado.", "remetente@gmail.com", "destinatario@gmail.com")
print(email.exibir())

relatorio = Relatorio("Relatório de Vendas", "As vendas deste mês aumentaram em 20%", "23/08/2023")
print(relatorio.exibir())
