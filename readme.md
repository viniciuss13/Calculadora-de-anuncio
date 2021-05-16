# Calculadora de Anuncios
Aplicação de terminal capaz de calcular informações sobre campanhas
de anúncios, sendo possível adicionar novos anúncios e filtrar relatórios
por cliente e período.

## Compilação
Por ser construído em Python, não há necessidade de compilação, porém é preciso
ter instalado python na máquina. A aplicação foi desenvolvida a utilizar Python 3.8.


## Execução
Para executar a aplicação basta invocar o comando: ```python main.py```  
Este comando inicia a aplicação no terminal, onde será possível escolher entre duas opções:
1. Cadastro de novo anuncio
2. Emissão de relatório dos anúncios

### Cadastro de anúncios
Para cadastrar um anúncio será necessário inserir as seguintes informações:  

- Nome do anuncio
- Nome do cliente
- Data inicial da campanha
- Data final da campanha
- Total investido por dia em reais.

Ao finalizar o cadastro de todas os anúncios que desejar, o usuário será
redirecionado ao menu inicial.


### Emissão de relatórios
Quando estiver a emitir um relatório será possível realizar os seguintes filtros:  

- Nome do cliente
- Data inicial da campanha
- Data final da campanha

Todos os filtros são opcionais, logo poderam ser deixados vazios.

## Observações
Existem alguns pontos de atenção nos preenchimentos dos campos:

- Datas: O padrão de entrada é dd/mm/yyyy, por exemplo, 30/12/2020
- Monetário: O padrão para decimais é centavos separados por '.'.

As informações inseridas na aplicação será persistente até o momento da sua
interrupção, sendo perdidos todos os dados ao final da sua execução.