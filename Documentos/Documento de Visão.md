#### Documento de Visão
# Sistema de Monitoramento de Hardware
### Integrantes
- Daniel Victor
- Fernando Dantas
- Luciano Sizlio
- Rosenildo Pereira
- Safyra Gurgel

## 1. Descrição do Projeto
#### 1.1. Resumo
O Sistema de Gerenciamento de Hardware provê diversas ferramentas onde é possível visualizar e entender necessidades de dispositivos, utilizando de visualização de dados em tempo real dos equipamentos, organização e tratamento desses dados.
#### 1.2. Clientes
Empresas, instituições de ensino publicas e privadas podem ser beneficiadas com esse projeto, mais especificamente as equipes de TI dessas entidades as quais são responsáveis pela manutenção e supervisão dos dispositivos em laboratórios, setores, salas de aulas ou qualquer outro ambiente que possuam esses equipamentos.
#### 1.3. Problema
Com a alta quantidade de dispostivos em empresas e/ou instituições muitos problemas ocorrem com os variados tipos de dispositivos porém nem todos os usuários desses equipamentos não são capazes de identificar seus possíveis problemas, deixando essa tarefa para um grupo restrito de pessoas como as equipes de TI.
##### 1.3.1 Monitorar computadores
As equipes de TI, em especial do IFRN - Natal Central que foi observada, realiza atendimentos conforme demandas de usuários dos computadores da instituição, muitas dessas demandas estão relacionadas a melhoria do desempenho das máquinas devido a softwares que são utilizados em laboratórios ou computadores específicos mas existem também, muitos usuários na instituição que não possuem noção dessa necessidade de melhorias e não relatam isso a TI, porém do outro lado, a equipe não tem nenhuma ferramenta para monitorar os equipamentos remotamente para que possa perceber em laboratórios e setores, potenciais melhorias que iriam ajudar demasiadamente seus usuários.
##### 1.3.2 Múltiplos dispositivos
No que se refere aos equipamentos de rede, existe atualmente uma diversidade muito grande de dispositivos nas redes aos quais são monitorados por diversos softwares separadamente. Isso pode causar confusões e atrasos na manutenção dos dispositivos.

## 2. Usuários
#### 2.1. Técnicos
Utilizam o sistema para cadastrar e gerenciar os dispositivos, setores e laboratórios, além de visualizar os equipamentos e suas informações.

#### 2.2. Detalhamento dos usuários
Nome |	Representa | Papel 
-- | -- | --
Técnico | Técnico de TI capacitado para visualizar os dados da plataforma | Cadastrar dispositivos e monitorar o uso deles.
Supervisor / Administrador | Servidor ou alguém com um cargo mais elevado dentro do setor de TI | Cadastrar e gerenciar os usuários, setores e laboratórios.

## 3. Escopo
#### 3.1. O que a plataforma é:
- Uma plataforma para visualizar todos os equipamentos e suas informações (Uso de CPU, Memória...);

#### 3.2. O que a plataforma NÃO é:
- Uma ferramenta para acesso remoto aos equipamentos.

#### 3.3. O que a plataforma faz:
- Cadastrar os lugares e ambientes
- Cadastrar os tipos de dispositivos (Ex. Microcomputador, Fonte de Tensão, Armário Fibra, Veículo)
- Cadastrar parâmetros de medição  
(Ex. Para Microcomputadores: CPU, Memória, Disco)
(Ex. Para Fonte de Tensão: Tensão de Entrada, Tensão de Saída)
(Ex. Para Veículos: Preço do automóvel, Localização)
- Cadastrar os dispositivos (cada dispositivo deve receber um id único)
- Visualizar as medições (por lugares/ambientes - valores médios, por dispositivos - valores individuais) permitindo vários tipos de apresentação (gráfico barra, gráfico linha, tabela)
- Mostra os equipamentos da instituição ou empresa separados por setores e/ou laboratórios com seu desempenho em tempo real (se estiver ligado);
- Informa dados dos equipamentos mesmo que desligados (não em tempo real).
- Visualizar as informações de um equipamento em tempo real.

#### 3.4. O que a plataforma NÃO faz:
- Executa tarefas nos equipamentos remotamente;
- Tem acesso aos arquivos dos equipamentos;
- Visualiza a tela dos computadores.
