# Cenário visualizar medições
#### Usuário: Técnico ou Supervisor
---
#### CDU_01 Visualizar Dashboard
1. O Técnico ou Supervisor acessa o sistema
2. O sistema retorna o dashboard, ilustrada na figura abaixo, mostrando três sessões principais:
    
    2.1. Uma sidebar esquerda mostrandos os dados básicos do usuário (foto, nome de usuário e setor) e um Menu com as opções Dashboard, Dispositivos, Tipos de Dispositivos, Usuários e Setores;

    2.2. Uma tabela com todos os dispositivos incluindo o setor de cada máquina, a sala e os dados dele como CPU, Memória, Disco, Temperatura do processador e outros. A ordem de disposição desses dados serão pré-configurados conforme o gosto do operador. Ele poderá reposicionar as colunas e ordená-las. Abaixo da tabela tem as opções para o controle de quantos dispositivos serão mostrados por página e a navegação entre elas. Também fica fácil de ver na tabela os dados que estão alarmados, pois a célular alarmada será exibida com a cor do alarme correspondente;

    2.3. Na parte superior da tabela, serão exibidos cards, mostrandos a quantidade de alarmes críticos, e de atenção, a quantidade de dispositivos ligados e o número máximo de máquinas ligadas no dia. Além disso tem as opções de filtros.

![img](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2021.1/sistemamonitoramentohardware/-/raw/master/Documentos/prototipoVisualizarMedicoes/Dashboard_N.png)

###### Ponto de extensão "Visualizar Alarmes", "Visualizar Dispositivo"
----
#### CDU_02 Visualizar Dispositivo
###### Estende "Visualizar Dashboard", "Visualizar Alarmes"
3. O Técnico ou Supervisor seleciona um dispositivo
4. O sistema retorna a página do dispositivo, ilustrada na figura abaixo, que além de mostrar a sua configuração e os dados da sua última medição, fornecerá os gráficos do histórico dos dados. Com eles, o operador analisará os gráficos de cada dado, comparando-os, no mesmo gráfico, com a média das máquinas da sala e do setor. Nessa página terá a opção de real time, onde o sistema passará a coletar os dados do PC a da poucos segundos em vez de cinco minutos por exemplo. Esses tempos de coleta e de real time podem ser configurados.
5. Depois da análise, o técnico seleciona voltar para retornar a página principal.

![img](https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2021.1/sistemamonitoramentohardware/-/raw/master/Documentos/prototipoVisualizarMedicoes/Device_Screen_N.png)
---
#### CDU_03 Visualizar Alarmes
###### Estende "Visualizar Dashboard"
1. O Técnico ou Supervisor seleciona alarmes
2. A página altera a tabela e exibe todos os dispositivos que estão com alarmes, ordenados pelos mais críticos.
###### Ponto de extensão "Visualizar Dispositivo"
&nbsp;
# Cenário Cadastrar Dispositivo
#### Usuário: Técnico ou Supervisor
---
#### CDU_04 Cadastrar Dispositivo
1. Usuário acessa o sistema.
2. Sistema apresenta um menu lateral com opções “Dashboard”, “Dispositivos”, “Usuários”, “Setores” e “Tipos de dispositivo”.
3. Usuário clica na opção “Dispositivos” no menu.
4. Sistema mostra a página de dispositivos com lista de dispositivos cadastrados no sistema , ordenações para a lista, filtros para a lista e um botão “Novo dispositivo”.
5. Usuário clica no botão “Novo dispositivo”.
6. Sistema mostra um modal com um formulário para preenchimento com os campos “nome”, “apelido”, “modelo”, dropdown de “tipo", dropdown de “setor”, dropdown de “sala” e um botão de “Cadastrar”.
7. Usuário preenche o formulário com os dados do dispositivo  e clica no botão “Cadastrar”.
8. Sistema mostra que o cadastro foi bem sucedido e fecha o modal.
&nbsp;
# Cenário Cadastrar Tipos de Dispositivos
#### Técnico ou Supervisor
----
#### CDU_05 Cadastrar Tipos de Dispositivos
1. Usuário acessa o sistema.
2. Sistema apresenta um menu lateral com opções "Dashboard", "Dispositivos", "Tipos de Dispositivos", "Usuários" e "Setores".
3. Usuário clica na opção "Tipos de Dispositivos".
4. Sistema mostra o botão "Novo Tipo" e a lista dos tipos de dispositivos.
5. Usuário clica em "Novo Tipo".
6. Sistema mostra um modal com um formulário para preenchimento com o título "Novo Tipo" com os campos "Nome", "Descrição", "Ícone" e o botão "Cadastrar".
7. Usuário preenche o formulário com os dados do tipo de dispositivo e clica no botão "Cadastrar".
8. Sistema mostra que o cadastro foi bem sucedido e fecha o modal.
&nbsp;
# Cenário Cadastrar Setores e Salas
#### Supervisor
----
#### CDU_06 Cadastar Setores e Salas
1. Usuário acessa o sistema.
2. Sistema apresenta um menu lateral com opções "Dashboard", "Dispositivos", "Tipos de Dispositivos", "Usuários" e "Setores".
3. Usuário clica na opção "Setores".
4. Sistema mostra a lista dos setores com o botão "Novo Setor" e opção de navegar para a página do setor ao clicar nele.
5. Usuário clica em "Novo Setor"
6. Sistema mostra um modal com um formulário para preenchimento com os campos "Nome" e "Descrição".
7. Usuário preenche o formulário e clica no botão "Cadastrar".
8. Sistema mostra que o cadastro foi bem sucedido e fecha o modal.
&nbsp;
# Cenário Cadastrar Dispositivos
#### Técnico ou Supervisor
----
#### CDU_07 Cadastrar Dispositivos
1. Usuário acessa o sistema.
2. Sistema apresenta um menu lateral com opções "Dashboard", "Dispositivos", "Tipos de Dispositivos", "Usuários" e "Setores".
3. Usuário clica na opção "Setores".
4. Sistema mostra página com a lista de dispositivos botão "Novo Dispositivo" e ordenações e filtros para a listagem.
5. Usuário clica em "Novo Dispositivo"
6. Sistema mostra um modal com um formulário para preenchimento com os campos "Nome", "Modelo", dropdown de "Tipo", dropdown de "Setor", dropdown de "Sala" e botão "Cadastrar".
7. Usuário preenche o formulário e clica no botão "Cadastrar".
8. Sistema mostra que o cadastro foi bem sucedido e fecha o modal.
&nbsp;
# Cenário de utilização “Cadastrar parâmetros de medição”
#### Técnico e Supervisor
----
#### CDU_08 Cadastrar parâmetros de medição
1. Técnico ou supervisor acessa o sistema.
2. Sistema apresenta um dashboard e um menu lateral com opções “Dashboard”, “Usuários”, “Dispositivos”, “Tipos de dispositivos” e “Setores”.
3. Usuário clica na opção “Tipos de dispositivos” no menu.
4. Sistema mostra lista de tipos de dispositivos no sistema.
5. Usuário clica em um dos tipos de dispositivos.
6. Sistema mostra informações do tipo de dispositivo e lista de parâmetros com um botão de adição abaixo da lista.
7. Usuário clica no botão de adição.
8. Sistema mostra um modal com um formulário para preenchimento com os campos “Nome”, “Descrição”, "Minimo pra alerta" e "Mínimo pra perigo".
9. Usuário preenche o formulário com os dados do parâmetro de medição e clica no botão “Cadastrar”.
10. Sistema mostra que o cadastro foi bem sucedido e fecha o modal.
