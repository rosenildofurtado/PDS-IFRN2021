### CDU Cadastrar Dispositivo
#### 1. Descrição
- Usuário cadastra um dispositivo no sistema informando seus dados e deixando-o disponível na visualização de todos dispositivos.

#### 2. Atores
- Técnico
- Supervisor

#### 3. Pré-condições

- Ter o tipo de dispositivo cadastrado

#### 4. Pós-condições

- Ter um novo dispositivo cadastrado no sistema

#### 5. Fluxo Principal

1. Usuário acessa o sistema.
2. Sistema apresenta um menu lateral com opções “Dashboard”, “Dispositivos”, “Tipos de Dispositivos”, “Usuários” e “Setores”.
3. Usuário clica na opção “Dispositivos” no menu.
4. Sistema mostra a página de dispositivos com lista de dispositivos cadastrados no sistema , ordenações para a lista, filtros para a lista e um botão “Novo dispositivo”.
5. Usuário clica no botão “Novo dispositivo”.
6. Sistema mostra um modal com um formulário para preenchimento com os campos “nome”, “modelo”, dropdown de “tipo", dropdown de “setor”, dropdown de “sala” e um botão de “Cadastrar”.
7. Usuário preenche o formulário com os dados do dispositivo e clica no botão “Cadastrar”.
8. Sistema mostra que o cadastro foi bem sucedido e fecha o modal.

#### 6. Fluxos alternativos
#### 7. Situações de erro
#### 8. Regras de Negócio
- RN01 - Código do dispositivo é gerado automaticamente garantindo unicidade