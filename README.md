# 1️⃣ Desafio Classificador de nível de Herói

## Propósito do Projeto

O projeto **Nível Herói XP** tem como objetivo classificar heróis em diferentes níveis com base em sua quantidade de experiência (XP). Cada herói recebe uma classificação que varia desde "Ferro" até "Radiante" de acordo com os critérios definidos. Este projeto é uma ótima maneira de entender conceitos fundamentais de programação, como variáveis, operadores, estruturas de decisão e testes unitários.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação usada para escrever a lógica do programa e os testes.
- **unittest**: Biblioteca de testes unitários integrada ao Python, utilizada para garantir que a função de classificação funciona corretamente.
- **Git**: Sistema de controle de versão para gerenciar o código-fonte do projeto.
- **GitHub**: Plataforma para hospedar o repositório do projeto e colaborar com outros desenvolvedores.

## Estrutura do Projeto

nivel-heroi-xp/  
├── README.md              # Documentação do projeto  
├── .gitignore             # Arquivo de exclusões do Git  
├── main.py                # Código principal  
├── test_main.py           # Testes automatizados  
├── data/                  # Pasta de dados  
│   └── banco_de_dados.json  # Base de dados  
├── assets/                # Recursos visuais  
│   └── imagens_exemplo.png  # Exemplo de imagem  
└── docs/                  # Documentação adicional  
    └── diagramas.md       # Diagramas explicativos  

## Como Executar o Programa

### Pré-requisitos

- **Python 3.x**: Certifique-se de ter o Python instalado. Você pode baixá-lo em [python.org](https://www.python.org/).
- **Git**: Certifique-se de ter o Git instalado. Você pode baixá-lo em [git-scm.com](https://git-scm.com/).

### Passos para Executar

1. **Clone o Repositório:**
   ```sh
   git clone https://github.com/profamar/nivel-heroi-xp.git
   cd nivel-heroi-xp
2.Instale as Dependências (se houver):
pip install -r requirements.txt

3.Execute o Script Principal:
python main.py

4.Execute os Testes Unitários:
python -m unittest test_main.py

## Utilização de Conceitos de Programação
Variáveis: Utilizadas para armazenar informações sobre o herói, como nome_heroi e xp_heroi.

Operadores: Empregados para comparar os valores de XP e determinar o nível do herói.

Estruturas de Decisão: Utilizamos if, elif e else para decidir o nível do herói com base na quantidade de XP.

Laços de Repetição: Embora este projeto específico não utilize laços de repetição, eles poderiam ser aplicados em futuros desenvolvimentos, como processamento de listas de heróis.

