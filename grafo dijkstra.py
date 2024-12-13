import heapq  # Para usar uma fila de prioridade
# A fila de prioridade permite selecionar rapidamente o vértice com a menor distância acumulada




# Alunos:   João Vitor de Oliveira Lima
#           Rafael Pereira Machado


class Grafo:
    def __init__(self):
        self.adjacentes = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacentes:
            self.adjacentes[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2, peso):
        if vertice1 not in self.adjacentes or vertice2 not in self.adjacentes:
            print("Erro! Adicione um vértice antes de criar uma aresta!")
        self.adjacentes[vertice1].append((vertice2, peso))
        self.adjacentes[vertice2].append((vertice1, peso))  # Aresta bidirecional

    def exibir(self):
        print("Grafo:")
        for vertice, arestas in self.adjacentes.items():
            print(f"{vertice} --> {arestas}")

    def Dijkstra(self, origem):

        distancias = {vertice: float('inf') for vertice in self.adjacentes}
        antecessores = {vertice: None for vertice in self.adjacentes}
        distancias[origem] = 0
        fila_prioridade = [(0, origem)]

        while fila_prioridade:
            distancia_atual, vertice_atual = heapq.heappop(fila_prioridade) # Remove e retorna o menor elemento da heap 

            if distancia_atual > distancias[vertice_atual]: # ignora o processamento de vértices que já foram atualizados com distâncias menores.

                continue

            for vizinho, peso in self.adjacentes[vertice_atual]:
                distancia = distancia_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    antecessores[vizinho] = vertice_atual
                    heapq.heappush(fila_prioridade, (distancia, vizinho)) # Insere o elemento na heap e reorganiza para manter a propriedade de heap.

        return distancias, antecessores

    def reconstruir_caminho(self, antecessores, destino):
        caminho = []
        atual = destino
        while atual is not None:
            caminho.append(atual)
            atual = antecessores[atual]
        caminho.reverse()
        return caminho


# Teste do grafo
grafo = Grafo()
cidades = [
    "Criciúma", "Içara", "Cocal do Sul", "Nova Veneza", "Meleiro",
    "Araranguá", "Balneário Rincão", "Turvo", "Balneário Camboriú"
]

for cidade in cidades:
    grafo.adicionar_vertice(cidade)

arestas = [
    ("Criciúma", "Içara", 4), ("Criciúma", "Turvo", 8),
    ("Içara", "Cocal do Sul", 8), ("Içara", "Turvo", 11),
    ("Cocal do Sul", "Nova Veneza", 7), ("Cocal do Sul", "Balneário Camboriú", 2),
    ("Cocal do Sul", "Araranguá", 4), ("Nova Veneza", "Meleiro", 9),
    ("Nova Veneza", "Araranguá", 14), ("Meleiro", "Araranguá", 10),
    ("Araranguá", "Balneário Rincão", 2), ("Balneário Rincão", "Turvo", 1),
    ("Turvo", "Balneário Camboriú", 7), ("Balneário Camboriú", "Balneário Rincão", 6)
]

for aresta in arestas:
    grafo.adicionar_aresta(*aresta)

grafo.exibir()

# Calculando distâncias
print("=" * 50)
distancias, antecessores = grafo.Dijkstra("Criciúma")
print("Distâncias mínimas a partir  de Criciúma:")

for cidade, distancia in distancias.items():
    print(f"{cidade}: {distancia} km")

print("=" * 50)
print(f"caminhos a partir de Criciúma:")

for cidade, distancia in distancias.items():
    caminho = grafo.reconstruir_caminho(antecessores, cidade)
    print(f"- Caminho até {cidade}: {' -> '.join(caminho)}")

    
# Alunos:   João Vitor de Oliveira Lima
#           Rafael Pereira Machado

print("=" * 50)
caminho = grafo.reconstruir_caminho(antecessores, "Balneário Camboriú")
print(f"Caminho de Criciúma para Balneário Camboriú: {caminho}")
print(f"Distância total percorrida: {distancias['Balneário Camboriú']} km")
