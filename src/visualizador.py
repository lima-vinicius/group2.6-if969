import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

def visualizarGrafo(grafo, titulo):
    """
    Visualiza o grafo utilizando a biblioteca NetworkX.
    """
    G = nx.Graph()
    
    # Adiciona os vértices e arestas ao grafo
    for estacaoOrigem, estacaoDestino, distancia in grafo.caminhos:
        G.add_edge(estacaoOrigem, estacaoDestino, weight=distancia)
    
    # Posicionamento dos vértices
    pos = nx.spring_layout(G)
    
    # Cores das arestas
    coresArestas = ['black'] * len(grafo.estacoes)
    
    # Cria uma nova figura
    plt.figure(figsize=(10, 8))
    
    # Desenha os vértices
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    
    # Desenha as arestas
    nx.draw_networkx_edges(G, pos, edge_color=coresArestas)
    
    # Adiciona rótulos aos vértices
    nx.draw_networkx_labels(G, pos, font_size=10)
    
    # Adiciona rótulos às arestas
    rotulosArestas = {tuple(aresta[:2]): aresta[2] for aresta in grafo.caminhos}  # Convertendo para tupla
    nx.draw_networkx_edge_labels(G, pos, edge_labels=rotulosArestas)
    
    # Exibe o gráfico
    plt.title(titulo)
    plt.axis("off")
    plt.show()
