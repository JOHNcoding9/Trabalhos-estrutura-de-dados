class No:
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None
    
    def mostrarNo(self):
        print(f"Valor: { self.valor}")
        print(f"Proximo Valor: { self.proximo}")
        print(f"anterior: { self.anterior}")

class encadeamento_duplo:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def lista_vazia(self):
        return self.primeiro == None
    
    def inserir_inicio(self,valor):
        novo = valor
        if self.lista_vazia():
            self.ultimo = novo
        
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro

    def insere_final(self,valor):
        novo = valor
        if self.lista_vazia():
            self.primeiro = novo
        
        else:
            self.ultimo.proximo = novo
        self.utlimo = novo

    def excluir_inicio(self):
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        primeiro = primeiro.proximo
