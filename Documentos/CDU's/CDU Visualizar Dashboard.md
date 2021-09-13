### CDU Visualizar Dashboard
#### 1. Descrição
- O técnico visualiza o dashboard com as últimas medições

#### 2. Atores
- Técnico

#### 3. Pré-condições

- O técnico precisa está logado para ter acesso ao dashboard

#### 4. Pós-condições

- Ter um novo dispositivo cadastrado no sistema

#### 5. Fluxo Principal

1. O técnico acessa a página do dashboard.
2. O sistema retorna a página, ilustrada na figura abaixo, mostrando três sessões principais:
- 2.1. Um quadro na lateral esquerda mostrando os dados do usuário (foto, username e setor) e um Menu com as opções de dashboard, dispositivos, usuários e setores, além das opções de sair e de arquivo de medições. Esse arquivo será usado, inicialmente, para simular a coleta de dados do sistema;
- 2.2. Uma tabela das últimas medições com todos os dispositivos, incluindo o setor de cada máquina, a sala e os dados dele como, CPU, memória, disco, temperatura do processador e outros. A ordem de disposição desses dados serão pré-configurados  conforme o gosto do operador. Ele poderá reposicionar as colunas e ordená-las conforme sua preferência. Abaixo da tabela, tem as opções para o controle de quantos dispositivos serão mostrados por página e a navegação entre elas. Também fica fácil de ver na tabela, os dados que estão alarmados, pois a célula alarmada será exibida com a cor do alarme correspondente;
- 2.3. Na parte superior da tabela, são exibidos “cards”, mostrando os alarmes críticos e de atenção, a quantidade de dispositivos ligados e o número máximo de máquinas ligadas. Além disso, tem as opções dos filtros.
#### 6. Fluxos alternativos
#### 7. Situações de erro
- Ainda não foram identificadas situações de erro porque a página será mostrada mesmo que não tenha nenhum dispositivo cadastrado. Nesse caso, a tabela será mostrada vazia.
#### 8. Regras de Negócio
- RN01 – a tabela inicial que será exibida sempre será a do tipo de dispositivo que o usuário estava visualizando antes de sair da sua última sessão.
- RN02 – a tabela inicial sempre será ordenada conforme estava na última sessão do usuário.
- RN03 – a tabela iniciará mostrando os dados da última leitura e se atualizará a cada medição.
