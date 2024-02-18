import csv
import classes as cs

def carregarGrafo():
    # Criar uma instância da classe Vertices
    grafo = cs.Vertices()
    
    # Abrir o arquivo CSV contendo os dados das estações e caminhos
    with open('database/arquivoestacoes.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            origem, destino, distancia = linha[0], linha[1], linha[2]
            
            # Adicionar estações ao grafo, se ainda não estiverem presentes
            if origem not in grafo.estacoes:
                grafo.estacoes.append(origem)
            if destino not in grafo.estacoes:
                grafo.estacoes.append(destino)
            
            # Adicionar caminhos ao grafo
            grafo.caminhos.append([origem, destino, float(distancia)])
    return grafo

def gerarGrafoRota(grafo, rota):
    # Dividir a rota em estações
    estacoes_rota = rota.split(' > ')
    
    # Criar um novo grafo
    grafo_rota = cs.Vertices()
    
    # Adicionar vértices da rota ao grafo
    for estacao in estacoes_rota:
        grafo_rota.estacoes.append(estacao)
    
    # Adicionar arestas da rota ao grafo
    for i in range(len(estacoes_rota) - 1):
        estacao_origem = estacoes_rota[i]
        estacao_destino = estacoes_rota[i + 1]
        for origem, destino, distancia in grafo.caminhos:
            if (origem == estacao_origem and destino == estacao_destino) or (origem == estacao_destino and destino == estacao_origem):
                grafo_rota.caminhos.append([origem, destino, float(distancia)])
    
    return grafo_rota
