import sys
sys.path.insert(0, 'src')

import tkinter as tk
from tkinter import messagebox, scrolledtext
import time
import preencher as pc
import bellmanford as bf
import visualizador as vs

def calcularMenorCaminho(root):
    estacaoOrigem = entryOrigem.get().strip()
    estacaoDestino = entryDestino.get().strip()
    
    if not estacaoOrigem or not estacaoDestino:
        tk.messagebox.showerror("Erro", "Por favor, insira as estações de origem e destino.")
        return
    
    try:
        if estacaoOrigem not in grafo.estacoes or estacaoDestino not in grafo.estacoes:
            raise ValueError("Estação não encontrada.")
        
        resultado = bf.bellmanFord(estacaoOrigem, grafo, estacaoDestino)

        labelResultado = tk.Label(root, text="Resultado:")
        labelResultado.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        textoResultado = tk.scrolledtext.ScrolledText(root, width=95, height=17)
        textoResultado.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        buttonVisualizarGrafo = tk.Button(root, text="Visualizar Grafo do percurso", command=lambda: exibirVisualizadorGrafos(resultado))
        buttonVisualizarGrafo.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        
        textoResultado.delete(1.0, tk.END)
        textoResultado.insert(tk.END, resultado)
    
    except ValueError as e:
        tk.messagebox.showerror("Erro", str(e))

def exibirVisualizadorGrafos(rota):
    if rota:
        grafoRota = pc.gerarGrafoRota(grafo, rota)
        vs.visualizarGrafo(grafoRota, "Grafo representando as estações de metrô de Munique que devem ser escolhidas para o menor tempo")
    else:
        vs.visualizarGrafo(grafo, "Grafo representando as linhas de metrô de Munique")

def exibirTelaInicial():
    rootInicial = tk.Tk()
    rootInicial.title("Guia de Navegação do Metrô de Munique")
    
    # Dimensões da tela
    larguraTela = 800
    alturaTela = 650
    
    # Criar um canvas para desenhar a imagem
    canvas = tk.Canvas(rootInicial, width=larguraTela, height=alturaTela)
    canvas.pack()
    
    # Carregar a imagem
    imagem = tk.PhotoImage(file="assets/munchen.png")
    
    # Redimensionar a imagem para preencher todo o canvas
    imagemRedimensionada = imagem.subsample(1)
    
    # Desenhar a imagem no canvas
    canvas.create_image(larguraTela // 2, alturaTela // 2, image=imagemRedimensionada)
    
    # Atualizar a tela
    rootInicial.update()
    
    # Esperar 3 segundos
    time.sleep(1.5)
    
    # Destruir a tela inicial
    rootInicial.destroy()
    
    # Exibir a tela principal
    exibirTelaPrincipal()

def exibirTelaPrincipal():
    global grafo
    grafo = pc.carregarGrafo()

    root = tk.Tk()
    root.title("Menor Caminho entre as Estações do Metrô de Munique")
    root.geometry("800x650")

    labelTitulo = tk.Label(root, text="Guia de Navegação do Metrô de Munique", font=("Arial", 24))
    labelTitulo.grid(row=0, column=0, columnspan=2, padx=50, pady=5)

    labelSubtitulo = tk.Label(root, text="Este guia tem como propósito ajudá-lo a chegar aos seus destinos de forma mais rápida utilizando o metrô de Munique. Solicitaremos a sua estação de origem e a estação de destino desejada, e em seguida mostraremos a rota recomendada juntamente com a distância a ser percorrida.", wraplength=700)
    labelSubtitulo.grid(row=1, column=0, columnspan=2, padx=50, pady=5)

    root.resizable(width=False, height=False)

    labelOrigem = tk.Label(root, text="Estação de Origem:")
    labelOrigem.grid(row=2, column=0, padx=0, pady=5)
    global entryOrigem
    entryOrigem = tk.Entry(root)
    entryOrigem.grid(row=2, column=1, padx=0, pady=5)

    labelDestino = tk.Label(root, text="Estação de Destino:")
    labelDestino.grid(row=3, column=0, padx=0, pady=5)
    global entryDestino
    entryDestino = tk.Entry(root)
    entryDestino.grid(row=3, column=1, padx=0, pady=5)

    buttonVisualizarGrafoCompleto = tk.Button(root, text="Visualizar Grafo das Estações", command=lambda: exibirVisualizadorGrafos(""))
    buttonVisualizarGrafoCompleto.grid(row=4, column=0, padx=10, pady=10)
    
    buttonCalcular = tk.Button(root, text="Calcular Menor Caminho", command=lambda: calcularMenorCaminho(root))
    buttonCalcular.grid(row=4, column=1, padx=10, pady=10)

    root.mainloop()

exibirTelaInicial()
