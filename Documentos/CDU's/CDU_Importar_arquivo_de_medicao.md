### Sistema de Monitoramento de Hardware
Integrantes:
    • Daniel Victor
    • Fernando Brüch
    • Luciano Sizilio
    • Rosenildo Pereira
    • Safyra Gurgel

### CDU_05 – “Importar arquivo de medição”

#### 1. Descrição
- O técnico seleciona arquivo de medição no dashboard e o sistema exibe, em outra janela, os diretórios do sistema operacional para que o técnico possa importar o arquivo JSON com os valores de medição. Depois que o técnico escolher o arquivo e selecionar abrir, o sistema fecha a janela e acrescenta os novos dados ao sistema, que serão mostrados no dashboard.

#### 2. Atores
- Técnico

#### 3. Pré-condições
- O arquivo para importar tem que ser no formato json.

#### 4. Pós-condições
- O sistema adiciona os novos dados ao banco e atualiza a tela do dashboard.

#### 5. Fluxo Principal
1. O técnico seleciona a opção arquivo de medição no dashboard.
2. O sistema exibe em outra janela os diretórios do sistema operacional para que o técnico possa importar o arquivo JSON com os valores de medição.
3. O técnico seleciona abrir o arquivo selecionado.
4. O sistema fecha a janela, acrescenta os novos dados ao banco de dados e atualiza a tabela do dashboard.
       
#### 6. Fluxo alternativo
1. O técnico seleciona cancelar. 
2. O sistema fecha a janela e retorna para o dashboard.

#### 7. Situações de erro
- O sistema pode esconder a opção de abrir ou mostrar uma mensagem de erro caso o arquivo escolhido não seja do formato correto.

#### 8. Regras de negócios
- RN07 – O arquivo de medição deve está no formato JSON.

