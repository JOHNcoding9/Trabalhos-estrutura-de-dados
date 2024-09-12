# 7. Implementar em linguagem Python o pseudocódigo do algoritmo “Pilha” visto na
# Aula 05. Faça também:
# a. Teste o método “pilhaVazia()” através do método “desempilhar()”;
# b. Demonstrar o empilhamento de cada um dos caracteres que compõem seu
# primeiro nome;
# c. Teste o método “pilhaCheia()” através do método “empilhar(valor)”;
# d. Após executar as operações anteriores, demonstrar qual elemento está no
# topo da Pilha;
# e. Execute o método “desempilhar()” por três vezes e verifique qual elemento
# está no topo da Pilha;

class Pilha:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = [""] * capacidade

    def pilha_cheia(self):
        return self.topo == self.capacidade - 1
    
    def pilha_vazia(self):
        return self.topo == -1
    
    def empilhar(self,valor):
        if self.pilha_cheia():
            print("Erro ! pilha já está cheia")
        else:
            self.topo += 1
        self.valores[self.topo] = valor
    
    def topo_pilha(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1
        
    def desempilhar(self):
        if self.pilha_vazia():
            print("Pilha atulamente vazia")
        else:
            self.valores[self.topo] = "" 
            self.topo -= 1

# criando objeto pilha
objeto_pilha = Pilha(10)

# teste empilhar
objeto_pilha.empilhar("J")
objeto_pilha.empilhar("o")
objeto_pilha.empilhar("ã")
objeto_pilha.empilhar("o")
objeto_pilha.empilhar("V")
objeto_pilha.empilhar("i")
objeto_pilha.empilhar("t")
objeto_pilha.empilhar("o")
objeto_pilha.empilhar("r")
print(objeto_pilha.valores)
# teste topo pilha
print(objeto_pilha.topo_pilha())

# teste desempilhar
objeto_pilha.desempilhar()
objeto_pilha.desempilhar()
objeto_pilha.desempilhar()
print(objeto_pilha.valores)

# 8. Suponha que você insira a sequência “S, A, T, C” em uma Pilha. Então você
# desempilha três elementos. Qual o valor do atributo topo da Pilha? 
 # O valor do topo será "S"

# 9. Qual o principal problema envolvido no algoritmo que implementa a Pilha?
 # só possível acessar o primeiro elemento inserido após remover todos os valores prescendentes a ele

# 10. Qual critério é utilizado para saber se uma Pilha está vazia? 
 # return self.topo == -1 ( Verifica se a afirmação de que o topo é igual a -1, é True ou False)

# 11. Qual critério é utilizado para saber se uma Pilha está cheia? 
 #  return self.topo == self.capacidade - 1 (Verifica se a afirmação de que a posição do topo alançou o ultimo slot de capacidade, é True ou False)