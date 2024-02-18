# Guia de Navegação do Metrô de Munique

## Descrição do Projeto

Este projeto consiste em um sistema que auxilia os usuários na navegação pelo metrô de Munique, fornecendo informações sobre o trajeto mais rápido entre duas estações desejadas. O sistema utiliza o algoritmo de Bellman-Ford para encontrar o caminho mais curto entre as estações, além de permitir a visualização do mapa das estações e caminhos disponíveis.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do sistema.
- **Tkinter**: Biblioteca padrão do Python para criação de interfaces gráficas.
- **NetworkX**: Biblioteca para manipulação de estruturas de redes, utilizada para visualizar o grafo das estações e caminhos.
- **Matplotlib**: Biblioteca para criação de gráficos e visualização de dados, utilizada em conjunto com o NetworkX para exibir o mapa das estações.
- **CSV**: Formato de arquivo utilizado para armazenar os dados das estações e caminhos do metrô de Munique.

## Instalação

Para executar o projeto, siga os passos abaixo:

1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

2. Clone este repositório para o seu ambiente local:

```
git clone https://github.com/rafaelmourato/algoritimos.git
```

3. Navegue até o diretório do projeto:

```
cd algoritmos
```

4. Instale as dependências do projeto utilizando o pip (gerenciador de pacotes do Python):

```
pip install matplotlib networkx
```

### Verificação e instalação do tkinter (para Windows)

Para sistemas Windows, o tkinter geralmente é instalado junto com o Python. No entanto, se você estiver enfrentando problemas, siga estas etapas:

1. Verifique se o tkinter está disponível digitando o seguinte comando no prompt de comando:

```bash
python -m tkinter
```

2. Se o tkinter não estiver disponível, você pode instalar o Python novamente usando o instalador oficial do Python (disponível em [python.org](https://www.python.org/)). Durante a instalação, certifique-se de marcar a opção para instalar o tkinter.

### Verificação e instalação do tkinter (para macOS)

Para sistemas macOS, o tkinter também é incluído na maioria das distribuições do Python. No entanto, se você estiver tendo problemas, siga estas etapas:

1. Verifique se o tkinter está disponível digitando o seguinte comando no terminal:

```bash
python3 -m tkinter
```

2. Se o tkinter não estiver disponível, você pode instalar o Python novamente usando o Homebrew (um gerenciador de pacotes para macOS) e garantir que o tkinter seja instalado. Primeiro, instale o Homebrew se ainda não o tiver:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Em seguida, instale o Python com o suporte ao tkinter usando o Homebrew:

```bash
brew install python-tk
```

### Verificação e instalação do tkinter (para Linux)

Para sistemas Linux, o tkinter geralmente não é incluído por padrão e precisa ser instalado separadamente. Aqui está como fazer isso em diferentes distribuições Linux:

#### Ubuntu / Debian:

1. Abra um terminal e atualize o índice de pacotes:

```bash
sudo apt update
```

2. Instale o pacote do tkinter:

```bash
sudo apt install python3-tk
```

## Executando o Projeto

Após a instalação das dependências, execute o projeto com o seguinte comando:

```
python main.py
```

Isso abrirá a interface gráfica do sistema, onde você poderá inserir a estação de origem e destino desejada para encontrar o menor caminho no metrô de Munique. Como também, visualizar as estações do metrô de Munique e caminho mais curto em formato de grafo.

## Processo de Desenvolvimento

O desenvolvimento deste projeto seguiu os seguintes passos:

1. **Análise de Requisitos:** Compreensão dos requisitos do projeto, incluindo funcionalidades necessárias e tecnologias a serem utilizadas.

2. **Estruturação do Projeto:** Definição da estrutura de diretórios e arquivos do projeto, incluindo a separação por módulos (Classes, Funções, Bellman Ford, Visualizar, Main).

3. **Implementação dos Módulos:** Desenvolvimento das classes, funções e algoritmo de Bellman-Ford para manipulação dos dados e cálculo do menor caminho.

4. **Interface Gráfica:** Implementação da interface gráfica utilizando a biblioteca Tkinter, incluindo a entrada de dados pelo usuário e exibição dos resultados.

5. **Visualização do Grafo:** Desenvolvimento da visualização do grafo das estações e caminhos utilizando as bibliotecas NetworkX e Matplotlib.

6. **Testes e Depuração:** Realização de testes para garantir o funcionamento correto do sistema e correção de eventuais erros ou bugs.

7. **Documentação:** Elaboração da documentação do projeto, incluindo este arquivo README.md e comentários nos códigos para facilitar a compreensão e manutenção do sistema.

## Autores

- [Rafael Mourato](https://github.com/rafaelmourato)
- [Vinícius Lima](https://github.com/lima-vinicius)

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).