# Sistema de Gestão de Vagas de Trabalho

## Objetivo

Desenvolver um sistema de gestão de vagas de trabalho utilizando o framework Django. O sistema permitirá a criação e gerenciamento de vagas de trabalho através do Django Admin e oferecerá uma landing page para que os usuários possam visualizar, descrever e se candidatar às vagas.

## Funcionalidades

### Backend (Django Admin)

- **Criação de Vagas de Trabalho**
  - **Campos**:
    - Empresa
    - Salário
    - Área
    - Descrição da vaga
  - **Interface**:
    - O administrador poderá adicionar, editar e excluir vagas de trabalho.

### Frontend (Landing Page)

- **Cadastro de Vagas**
  - Usuários poderão visualizar uma lista de vagas disponíveis.
  - Cada vaga incluirá detalhes como salário, área e uma descrição completa.
  - **Ações**:
    - **Ver Vaga**: Exibir detalhes da vaga.
    - **Aplicar**: Formulário para que o usuário se candidate à vaga (ex.: enviar um e-mail ou formulário de candidatura).

## Tecnologias Utilizadas

- **Django**: Framework web para o backend, que facilitará a criação do sistema de gerenciamento e a administração das vagas de trabalho.
- **Python**: Linguagem de programação utilizada no Django.
- **HTML/CSS**: Para o desenvolvimento da landing page.
- **JavaScript**: Para possíveis funcionalidades interativas na landing page.
- **Banco de Dados**: O Django suporta vários bancos de dados, sendo o SQLite o padrão para desenvolvimento. Outros bancos de dados, como PostgreSQL ou MySQL, podem ser utilizados conforme necessário.

## Estrutura do Projeto

1. **Modelo de Dados**
   - **Vaga**: Modelo que incluirá campos para salário, área e descrição.

2. **Administração**
   - Configuração do Django Admin para gerenciar o modelo de vagas.

3. **Landing Page**
   - **Listagem de Vagas**: Página inicial que exibirá todas as vagas disponíveis.
   - **Detalhes da Vaga**: Página para mostrar detalhes completos sobre uma vaga específica.
   - **Formulário de Candidatura**: Página para que o usuário possa se candidatar à vaga.

## Passos a Serem Seguidos

- [ ] **Configuração do Ambiente**
  - Instalar Django e configurar o projeto inicial.

- [ ] **Desenvolvimento do Backend**
  - Criar o modelo de dados para as vagas.
  - Configurar o Django Admin para permitir a criação e gerenciamento das vagas.

- [ ] **Desenvolvimento do Frontend**
  - Criar a landing page para listar as vagas.
  - Desenvolver as páginas de detalhes da vaga e formulário de candidatura.

- [ ] **Testes**
  - Testar a criação e gerenciamento de vagas no Django Admin.
  - Testar a funcionalidade da landing page e do formulário de candidatura.

- [ ] **Implantação**
  - Preparar o projeto para produção.
  - Deploy em um servidor de sua escolha.

## Considerações Finais

Este documento fornece uma visão geral do projeto e estabelece uma base sólida para o desenvolvimento do sistema de gestão de vagas de trabalho. Alterações e melhorias podem ser feitas conforme o projeto avança.

