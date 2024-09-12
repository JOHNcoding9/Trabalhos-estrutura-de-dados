# 1. Implementar em linguagem Python o pseudocódigo do algoritmo “Fila” visto na Aula 05
# com capacidade igual a quantidade de caracteres que compõem seu primeiro nome. Faça
# também:
# a. Teste o método “filaVazia()” através do método “desenfileirar()”;
# b. Demonstrar o enfileiramento de cada um dos caracteres que compõem seu
# primeiro nome;
# c. Teste o método “filaCheia()” através do método “enfileirar(valor)”;
# d. Após executar as operações anteriores, demonstrar qual elemento é o primeiro
# da fila;
# e. Execute o método “desenfileirar()” por três vezes e verifique qual elemento é o
# primeiro da fila.


class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = -1
        self.elementos = 0
        self.valores = [""] * capacidade

    def fila_cheia(self):
        return self.elementos == self.capacidade
    
    def enfileirar(self,valor):
        if self.fila_cheia():
            print("Erro ! A fila já está cheia !")
        if self.fim == self.capacidade - 1: # No caso de uma fila circular
            self.fim = -1
        self.fim = self.fim + 1
        self.valores[self.fim] = valor
        self.elementos += 1
    
    def  fila_vazia(self):
        return self.elementos == 0
    
    def desenfileirar(self):
        if self.fila_vazia():
           return print("Erro! a fila já está vazia")
        proximo_da_fila = self.valores[self.inicio]
        self.valores[self.inicio] = "" 
        self.inicio += 1
        if self.inicio == self.capacidade : # No caso da fila circular
            self.inicio = 0
        self.elementos -= 1
        return proximo_da_fila
    
    def inicio_fila(self):
        if self.fila_vazia():
            return -1
        return self.valores[self.inicio]

# criação de objeto Fila
objeto_fila = Fila(10)

# teste enfileirar
objeto_fila.enfileirar("J")
objeto_fila.enfileirar("o")
objeto_fila.enfileirar('ã')
objeto_fila.enfileirar("o")
objeto_fila.enfileirar("V")
objeto_fila.enfileirar("i")
objeto_fila.enfileirar("t")
objeto_fila.enfileirar("o")
objeto_fila.enfileirar("r")

print(objeto_fila.valores)
# teste desenfileirar
objeto_fila.desenfileirar()
objeto_fila.desenfileirar()
objeto_fila.desenfileirar()

# teste inicio fila
print(objeto_fila.inicio_fila())
print(objeto_fila.valores)
 

# 2. O problema de inserir (enfileirar) elementos em uma Fila envolve? Explique o que
# “precisa ser feito” para inserir um elemento e quais cuidados devem ser protegidos no
# algoritmo.
  # Ao inserir um novo item na fila, deve-se verificar se a fila não está cheia. Após isso, verificar se  a posição final chegou no ultimo slot de capacidade ( se esse for o caso, deve-se resetar o valor final para -1). Se esse não for o caso, acrescenta-se + 1 para a posição final, e se atribui o valor digitado pelo usuario àquela nova posição final. Por fim , se atualiza a quantidade  de elementos para + 1 elemento
 
# 3. O problema de retirar (desenfileirar) elementos em uma fila envolve? Explique o que
# “precisa ser feito” para retirar um elemento e quais cuidados devem ser protegidos no
# algoritmo.
 # Ao retirar um item da fila, deve-se verificar se a mesma não está vazia. Após isso, define-se o primeiro valor inserido na fila como o proximo a ser excluído. Após sua exclusão, a próxima posição prescendente será o novo proximo valor a ser excluído . No caso da fila circular, o valor da posição a ser excluída deve ser resetada para 0 quando esta atingir a capacidade máxima da fila.

# 4. Qual critério é utilizado para saber se uma Fila está vazia?
 # return self.elementos == 0 ( Essa linha de código retorna se a afirmação de, a quantidade e elementos ser igual a zero, é True ou False)

# 5. Qual critério é utilizado para saber se uma Fila está cheia? 
 # return self.elementos == self.capacidade ( Essa linha de código retorna se a afirmação de que, a quantidade elementos é igual a capacidade máxima, é True ou False)


# a. Insira a sequência T,C na Fila e demonstre esse procedimento através do
# preenchimento da tabela abaixo: ["","","S","A"]
# . Qual o valor do atributo “final” após a inserção da sequência descrita no item a)?
 # o valor do atributo final seria a posição 1

# c. Se você fosse “desenfileirar” um elemento da Fila, qual seria esse elemento?
 # o elemento excluído seria "S"