# 1 Implementar em linguagem Python o pseudocódigo do algoritmo “Vetor Não
# Ordenado” visto na Aula 03. Faça também:
# a. Demonstrar a inserção de cada um dos caracteres que compõem seu primeiro
# nome;
# b. Demonstrar a impressão do vetor criado;
# c. Demonstrar a pesquisa por pelo menos três caracteres existentes no vetor;
# d. Demonstrar a exclusão de caracteres do início, meio e final do vetor;
# e. Demonstrar a impressão do vetor após as remoções.
class VetorNaoOrndenado:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.posicao = -1
        self.valores = [''] * capacidade
    def inserir(self,valor):
        if self.posicao == self.capacidade - 1:
            print("Vetor atualmente cheio")
        else:
            self.posicao += 1
            self.valores[self.posicao] = valor
            print("vetor criado: ")
    def imprimir(self):
        if self.posicao == -1:
            print("vetor atualmente vazio")
        else:
            for i in range(self.posicao +  1):
                print("posição:",i,"->", self.valores[i])
    def pesquisar(self,valor):
        for e in range(self.posicao + 1) :
            if (valor == self.valores[e]) :
             return e
        return -1
    def excluir(self,valor):
        pesquisando = self.pesquisar(valor)
        if (pesquisando == -1):
            return -1
        else:
            for i in range(pesquisando,self.posicao ):
                self.valores[i] = self.valores[i + 1]
            self.valores[self.posicao] = ''
            self.posicao = self.posicao - 1




# teste inserir vetor
Vetor = VetorNaoOrndenado(9)
print(Vetor.valores)
Vetor.inserir("J")
Vetor.inserir("o")
Vetor.inserir("ã")
Vetor.inserir("o")
Vetor.inserir("V")
Vetor.inserir("i")
Vetor.inserir("t")
Vetor.inserir("o")
Vetor.inserir("r")
print(Vetor.valores)
# vetor cheio teste
Vetor.inserir("P")

# teste de impressão
Vetor.imprimir()

# teste pesquisar
a = Vetor.pesquisar("J")
b = Vetor.pesquisar("V")
d = Vetor.pesquisar("o")
c = Vetor.pesquisar("r")
print("a letra J esta na posiçaõ: ",a)
print("a letra V esta na posiçaõ: ",b)
print("a letra r esta na posiçaõ: ",c)
print("a letra o esta na posiçaõ: ",d)

# teste de excluir
Vetor.excluir('J')
Vetor.excluir('ã')
Vetor.excluir('V')

# impressão após a exclusão de valores
print("Após excluir J ã V ",Vetor.valores)




# 2. Considere um vetor não ordenado com capacidade igual a 7 elementos contendo
# em seu interior a sequência “C,A,S,A”. Responda:

# a. Qual o nome do atributo responsável pelo controle de inserções da sequência
# descrita no enunciado desta questão?
 # R: o atributo capacidade, ( o número de elementos) controla as inserções da sequência

# b. Após a inserção da sequência, qual o valor do atributo “ultima_posiçao”?
 # R: o valor do atributo ultima_posicao seria a posição 3

# c. Se excluirmos o elemento do vetor cujo valor do seu índice é 1, quantas
# iterações serão necessárias para realocar os demais elementos do vetor?
 # R: serão necessárias 2 iterações para realocar as letras da direita para a esquerda

# d. Se executar o método “imprimir()”, qual sequência de caracteres será mostrada
# após a operação realizada no ítem b)?
 # R: o terminal irá imprimir "CASA" após a operação do item b)
 # R: o terminal irá imrpimir "CSA" após a opreção do item d)

# e. Qual o novo valor do atributo “ultima_posiçao”?
 # R: o novo valor de ultima_posicao é = 2

# f. Com base no algoritmo de pesquisa, qual a condição utilizada para saber se ele
# encontrou o elemento solicitado?
 # R: o loop for irá transformar i em um valor da range a cada iteração
 #  se/quando o valor inserido pelo usuário for igual ao valor dentro da posição i da lista self.valores
 #  retorne o valor i
 #  senão, retorne -1

 # type: ignore
