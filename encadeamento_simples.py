class No:  
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)


class ListaEncadeada:  
    def __init__(self):
        self.primeiro = None

    def inserir_inicio(self, valor):
        novo = No(valor)  # Cria um novo objeto de classe No
        novo.proximo = self.primeiro # O novo nó aponta para o atual primeiro nó da lista
        self.primeiro = novo # O novo nó se torna o primeiro nó da lista

    def mostrar_lista(self):
        if self.primeiro is None:
            print("Lista encadeada nula!")
            return
        atual = self.primeiro
        while atual is not None:
            atual.mostrar_no()  # Mostra o valor do nó atual
            atual = atual.proximo

    def excluir_inicio(self):
        if self.primeiro is None:
            print("Erro de lista vazia!")
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo  
        return temp.valor  # Retorna o valor do nó excluído

    def pesquisar_lista(self, valor):
        if self.primeiro is None:
            print("Erro de lista vazia!")
            return None
        atual = self.primeiro
        while atual is not None:
            if atual.valor == valor:  # Verifica se o valor do nó atual é o procurado
                return atual
            atual = atual.proximo
        return None  # Retorna None se não encontrar o valor

    def excluir_qualquer_valor(self, valor):
        if self.primeiro is None:
            print("Erro de lista vazia!")
            return None
        atual = self.primeiro
        anterior = None
        while atual is not None:
            if atual.valor == valor:  # Se o valor é encontrado
                if anterior is None:  # Se for o primeiro nó
                    self.primeiro = atual.proximo
                else:
                    anterior.proximo = atual.proximo  # Remove o nó
                return atual.valor  # Retorna o valor do nó excluído
            anterior = atual
            atual = atual.proximo
        return None  # Retorna None se o valor não for encontrado

# Exemplo de uso
lista = ListaEncadeada()
lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_inicio(30)

print("Elementos da lista:")
lista.mostrar_lista()

print("\nExcluindo o primeiro elemento:")
lista.excluir_inicio()
lista.mostrar_lista()

print("\nPesquisando o valor 20:")
resultado = lista.pesquisar_lista(20)
if resultado:
    print(f"Valor encontrado: {resultado.valor}")
else:
    print("Valor não encontrado.")

print("\nExcluindo o valor 10:")
lista.excluir_qualquer_valor(10)
lista.mostrar_lista()
