<h1 align="center"> ReactGen </h1>

![LICENSE](https://img.shields.io/badge/LICENSE-GNU%20General%20Public%20License%20v3.0-blue)

## Introdução
Repositório criado para o projeto ReactGen, um algoritmo genético que seleciona uma molécula com alta chance de reagir com outra molécula dada.

<details>
    
__<summary>Algoritmos Genéticos :dna:</summary>__
    
Os algoritmos genéticos são uma família de algoritmos de busca inspirados nos princípios da evolução da natureza. Ao simular o processo de seleção natural e reprodução, eles são capazes de gerar soluções de alta qualidade para diversos problemas relacionados à busca, otimização e aprendizado. A sua analogia com a evolução natural permite que os algoritmos genéticos superem os desafios encontrados pelos algoritmos de busca e otimização convencionais, principalmente em problemas com uma grande quantidade de parâmetros e representações matemáticas complexas.
</details>

<details>
    
__<summary>O que nosso algoritmo genético faz?</summary>__

Nosso algoritmo genético é projetado para otimizar a combinação de grupos funcionais em uma molécula de referência. Aqui está uma visão geral do funcionamento do algoritmo em relação às moléculas:

**Inicialização:** A população inicial de indivíduos é criada com base em um tamanho fixo (TAM_POP) e um número máximo de grupos funcionais permitidos (MAX_GROUPS). Cada indivíduo representa uma combinação aleatória de grupos funcionais.

**Avaliação:** Cada indivíduo na população é avaliado em relação à sua adequação ou ajuste para a molécula de referência. Isso é feito por meio da função de fitness, que avalia a qualidade da combinação de grupos funcionais em relação à molécula.

**Seleção:** Os indivíduos mais adequados são selecionados para reprodução com base em seus valores de fitness.

**Reprodução:** Os indivíduos selecionados são combinados através do cruzamento (crossover) e da mutação para gerar descendentes. O operador de cruzamento é aplicado para trocar informações genéticas entre dois indivíduos, enquanto a mutação introduz pequenas alterações aleatórias nos indivíduos.

**Atualização da população:** Os descendentes gerados substituem os indivíduos menos adequados na população atual, mantendo o tamanho da população constante. Isso permite que as características mais favoráveis sejam transmitidas para as gerações subsequentes.

**Critério de parada:** O processo de seleção, reprodução e atualização é repetido por um número específico de gerações (NUM_GEN) ou até que algum critério de parada seja atendido.

O objetivo final desse algoritmo genético é encontrar a combinação de grupos funcionais que resulta na melhor adequação ou ajuste para a molécula de referência fornecida. A função de fitness é responsável por avaliar essa adequação, e o algoritmo busca aprimorar a população ao longo das gerações, selecionando os indivíduos mais aptos e aplicando operadores genéticos para explorar o espaço de soluções em busca de melhores resultados.
    
</details>

<details>
    
__<summary>Bibliotecas utilizadas</summary>__

- **random:** A biblioteca 'random' é utilizada para gerar números aleatórios
    
- **copy:** A biblioteca 'copy' fornece funções para copiar objetos
    
- **pubchempy:** A biblioteca 'pubchempy' é uma API que permite acessar o banco de dados do PubChem, uma plataforma de química que fornece informações sobre compostos químicos. No código, ela é utilizada para buscar informações sobre uma molécula de referência, como o SMILES (Simplified Molecular Input Line Entry System), que é uma representação textual da estrutura química
    
- **rdkit**: O 'RDKit' é uma biblioteca de química computacional amplamente utilizada. Ela oferece uma ampla gama de recursos para manipulação, visualização e análise de moléculas. No código, as seguintes subbibliotecas do RDKit são importadas:

    - Chem: A subbiblioteca 'Chem' fornece classes e funções para manipulação de moléculas. Ela é usada para criar objetos Mol a partir de SMILES e calcular fórmulas moleculares

    - Fragments: A subbiblioteca 'Fragments' contém funções relacionadas à fragmentação de moléculas
    
    - Draw: A subbiblioteca 'Draw' contém funções para visualização de moléculas

    - rdMolDescriptors: A subbiblioteca 'rdMolDescriptors' contém funções relacionadas à descrição molecular, como o cálculo da fórmula molecular
    
- **PIL (Python Imaging Library):** A biblioteca 'PIL' fornece funcionalidades para processamento de imagens
    
</details>
    
## Conteúdo

<details>
    
__<summary>Glossário :page_with_curl:</summary>__
    
    
- __*Indivíduos*:__ Em algoritmos genéticos, os indivíduos são soluções potenciais para um problema. Cada indivíduo é representado por um cromossomo, que contém genes que codificam características ou traços específicos.

- __*População*:__ Uma população é uma coleção de indivíduos que são avaliados e evoluídos ao longo do tempo. A população representa a geração atual de soluções potenciais.

- __*Gene*:__ Um gene é uma seção específica de um cromossomo que codifica um traço ou característica particular. Por exemplo, em um algoritmo genético para otimizar o design de uma asa de avião, um gene pode representar o ângulo no qual a asa está inclinada.

- __*Cromossomos*:__ Um cromossomo é uma sequência de genes que representa uma solução individual para o problema em questão. Em algoritmos genéticos codificados em binário, os cromossomos são geralmente representados como sequências de 0s e 1s.

- __*Geração*:__ Uma geração refere-se a uma iteração do algoritmo genético. Durante cada geração, a função de aptidão é aplicada para avaliar os indivíduos da população, e novos indivíduos são criados por meio de seleção, cruzamento e mutação.

- __*Função de objetivo*:__ A função de aptidão é usada para avaliar o quão bem cada indivíduo da população resolve o problema em questão. Ela atribui uma pontuação de aptidão a cada indivíduo com base em quão próximo sua solução está de ser ótima.

- __*Seleção*:__ A seleção é o processo pelo qual os indivíduos com pontuações de aptidão mais altas têm maior probabilidade de serem escolhidos para reprodução (ou seja, passar seus genes adiante) do que aqueles com pontuações de aptidão mais baixas.

- __*Cruzamento*:__ O cruzamento envolve a combinação de dois cromossomos parentais para criar um ou mais cromossomos filhos. Esse processo pode ajudar a criar novas combinações de genes que podem levar a melhores soluções.

- __*Mutação*:__ A mutação envolve a alteração aleatória de um ou mais genes no cromossomo de um indivíduo. Esse processo pode ajudar a introduzir novos traços na população que podem levar a melhores soluções.

</details>

As seguintes pastas compõem o repositório:
- [LICENSE](https://github.com/PedroSophiaaa/ReactGen/blob/main/LICENSE): Licença usada no repositório
- [README.md](https://github.com/PedroSophiaaa/ReactGen/blob/main/README.md): Guia para o repositório
- [grupos_funcionais.py](https://github.com/PedroSophiaaa/ReactGen/blob/main/grupos_funcionais.py): Ferramenta para detectar e selecionar os grupos funcionais presentes em uma molécula
- [funcoes.py](https://github.com/PedroSophiaaa/ReactGen/blob/main/funcoes.py): Funções do Algoritmo Genético
- [TrabalhoFinal.ipynb](https://github.com/PedroSophiaaa/ReactGen/blob/main/TrabalhoFinal.ipynb): Arquivo de execução do Algoritmo Genético

## Autores

<table>
  <tr>
    <td align="center"><a href="https://github.com/Marihbn"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/107010586?v=4" width="100px;" alt=""/><br /><sub><b>Marina Barim do Nascimento</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/PedroSophiaaa"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/106617753?v=4" width="100px;" alt=""/><br /><sub><b>Pedro Henrique Sophia</b></sub></a><br/></td>
    <td align="center"><a href="https://github.com/TiagoMarquesHxH"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/106617887?v=4" width="100px;" alt=""/><br /><sub><b>Pedro Henrique Sophia</b></sub></a><br/></td>
    <td align="center"><a href="https://github.com/guilhermeilum"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/107007032?v=4" width="100px;" alt=""/><br /><sub><b>Pedro Henrique Sophia</b></sub></a><br/></td>
  </tr>
</table>
