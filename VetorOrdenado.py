# 1. Implementar em linguagem Python o pseudocódigo do algoritmo “Vetor Ordenado” visto
# na Aula 03. Faça também:
# a. Demonstrar a inserção de cada um dos caracteres que compõem seu primeiro nome;
# b. Demonstrar a impressão do vetor criado;
# c. Demonstrar a pesquisa por pelo menos três caracteres existentes no vetor;
# d. Demonstrar a exclusão de caracteres do início, meio e final do vetor;
# e. Demonstrar a impressão do vetor após as remoções.

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = [''] * capacidade

    def imprimir(self):
        if self.ultima_posicao == -1:
            print("Vetor atualmente vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(f"Posição : {i} | Valor: {self.valores[i]}")

    def inserir(self, valor):
        # Verificar se o vetor está cheio
        if self.ultima_posicao == self.capacidade - 1:
            print("Vetor cheio")
            return

        # Encontrar a posição onde o novo valor deve ser inserido
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                posicao = i
                break
        else:
            posicao = self.ultima_posicao + 1

        # Mover os elementos para abrir espaço para o novo valor
        for x in range(self.ultima_posicao, posicao - 1, -1):
            self.valores[x + 1] = self.valores[x]

        # Inserir o novo valor na posição correta
        self.valores[posicao] = valor

        # Atualizar a última posição
        self.ultima_posicao += 1
   
    def pesquisa_linear(self,valor):
        for i in range(self.ultima_posicao + 1):
            if (self.valores[i] == valor):
                return i
        return -1
    
    def pesquisa_binaria(self,valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao
        while True:
            posicao_atual = ( limite_inferior + limite_superior) // 2
            # Se o valor for encontrado
            if (self.valores[posicao_atual] == valor):
                return posicao_atual
           
            # Valor não encontrado
            if limite_inferior > limite_superior:
                return -1
            
            # Divide os limites
            else:
                # limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1

                    #Limite superior
                else:
                    limite_superior = posicao_atual - 1
        
    def excluir(self,valor):
        posicao = self.pesquisa_binaria(valor)
        if (posicao == -1):
            return -1
        else:
            for i in range(posicao,self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1





# criando o Objeto vetor ordenado
vetor = VetorOrdenado(9)

# teste de inserção
vetor.inserir(3)
vetor.inserir(1)
vetor.inserir(5)
vetor.inserir(4)
vetor.inserir(2)
vetor.inserir(9)
vetor.inserir(14)
vetor.inserir(20)
vetor.inserir(10)

# teste capacidade máxima
vetor.inserir(54)

# teste de impressão
vetor.imprimir()

# Teste pesquisa linear
print(vetor.pesquisa_linear(4))
print(vetor.pesquisa_linear(7))
print(vetor.pesquisa_linear(10))

# teste pesquisa binaria
print("bin",vetor.pesquisa_binaria(4))
print("bin",vetor.pesquisa_binaria(9))
print("bin",vetor.pesquisa_binaria(21))

# teste excluir valores
vetor.excluir(1)
vetor.excluir(5)
vetor.excluir(4)
vetor.imprimir()




# 2. Considere um vetor ordenado com capacidade igual a 7 elementos contendo em seu interior
# a sequência “2, 3, 5, 7”. Responda:

# a. Após a inserção da sequência, qual o valor do atributo “ultima_posiçao”?
  # o valor da ultima posição será 3

# b. Se inserirmos o elemento cujo valor é igual a 4, quantas iterações serão necessárias
# para realocar os demais elementos do vetor?
 # serão necessárias 2 iterações

# c. Qual o novo valor do atributo “ultima_posiçao”?
 #  o valor da ultima posição será 4

# d. Com base no algoritmo de pesquisa linear, quantas iterações serão necessárias para
# encontrar o índice do vetor que contém o valor 7?
 # 4 iterações

# e. Com base no algoritmo de pesquisa binária, quantas iterações serão necessárias para
# encontrar o índice do vetor que contém o valor 7?
 # 3 iterações
