class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def mostrar_no(self):
        print(self.valor)

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)
        if self.raiz is None:  # se a árvore estiver vazia
            self.raiz = novo
            return
        
        atual = self.raiz
        while True:
            pai = atual
            if valor < atual.valor:  # esquerda
                atual = atual.esquerda
                if atual is None:
                    pai.esquerda = novo
                    return
            else:  # direita
                atual = atual.direita
                if atual is None:
                    pai.direita = novo
                    return

    def pesquisar_valor(self, valor):
        atual = self.raiz
        while atual is not None:
            if atual.valor == valor:
                return atual
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None

    def pre_ordem(self, no):  # raiz, esquerda, direita
        if no is not None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    def em_ordem(self, no):  # esquerda, raiz, direita
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)

    def pos_ordem(self, no):  # esquerda, direita, raiz
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

    def excluir_no(self, valor):
        if self.raiz is None:
            print("Árvore binária vazia!")
            return
        
        # Encontrar nó
        atual = self.raiz
        pai = None
        e_esquerda = True
        
        while atual is not None and atual.valor != valor:
            pai = atual
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            else:
                e_esquerda = False
                atual = atual.direita
            
        if atual is None:
            return False  # O nó não foi encontrado

        # Caso 1: nó a ser excluído é uma folha
        if atual.esquerda is None and atual.direita is None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda:
                pai.esquerda = None
            else:
                pai.direita = None

        # Caso 2: nó a ser excluído tem apenas filho à esquerda
        elif atual.direita is None:
            if atual == self.raiz:
                self.raiz = atual.esquerda
            elif e_esquerda:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda

        # Caso 3: nó a ser excluído tem apenas filho à direita
        elif atual.esquerda is None:
            if atual == self.raiz:
                self.raiz = atual.direita
            elif e_esquerda:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita

        # Caso 4: nó a ser excluído tem dois filhos
        else:
            sucessor = self.get_sucessor(atual)
            if atual == self.raiz:
                self.raiz = sucessor
            elif e_esquerda:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor

            sucessor.esquerda = atual.esquerda

        return True
            
    def get_sucessor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita

        while atual is not None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        
        # Ajuste no ponteiro do pai do sucessor
        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
            
        return sucessor
    
    
# Criar uma instância da árvore binária
arvore = ArvoreBinaria()

# Inserir valores
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

# Exibir em ordem
print("Em ordem:")
arvore.em_ordem(arvore.raiz)

# Pesquisar um valor
valor_pesquisar = 40
no_encontrado = arvore.pesquisar_valor(valor_pesquisar)
print(f"\nPesquisar {valor_pesquisar}: {'Encontrado' if no_encontrado else 'Não encontrado'}")

# Excluir um nó (folha)
arvore.excluir_no(20)
print("\nApós excluir 20 (folha):")
arvore.em_ordem(arvore.raiz)

# Excluir um nó (com um filho)
arvore.excluir_no(30)
print("\nApós excluir 30 (com um filho):")
arvore.em_ordem(arvore.raiz)

# Excluir um nó (com dois filhos)
arvore.excluir_no(50)
print("\nApós excluir 50 (com dois filhos):")
arvore.em_ordem(arvore.raiz)
