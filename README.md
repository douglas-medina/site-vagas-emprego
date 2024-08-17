# Sistema de Gestão de Vagas

## Objetivo

Desenvolver um sistema de gestão de vagas de emprego utilizando **Python 3.11+** e  **Django 5+** . O sistema permitirá que empresas possam criar, editar e excluir vagas, enquanto candidatos poderão se candidatar a essas vagas através de uma interface simples. Além disso, relatórios e gráficos serão gerados para acompanhar as vagas e candidaturas.

## Funcionalidades

### Backend (Django Admin)

* **Cadastro de Vagas** : Empresas podem criar uma ou várias vagas com informações detalhadas.
* **Campos das Vagas** :
  * Nome da Vaga
  * Faixa Salarial:
    * Até 1.000
    * De 1.000 a 2.000
    * De 2.000 a 3.000
    * Acima de 3.000
  * Requisitos
  * Escolaridade Mínima:
    * Ensino Fundamental
    * Ensino Médio
    * Tecnólogo
    * Ensino Superior
    * Pós/MBA/Mestrado
    * Doutorado
* **Gerenciamento de Vagas** : O administrador pode editar e excluir vagas conforme necessário.

### Frontend (Página de Candidatura)

* **Visualização de Vagas** : Candidatos podem visualizar todas as vagas disponíveis, com detalhes como faixa salarial, requisitos e escolaridade mínima.
* **Formulário de Candidatura** : Candidatos podem se candidatar a uma vaga informando:
  * Pretensão Salarial
  * Experiência
  * Última Escolaridade

### Relatórios e Gráficos

* Utilização de **Charts.js** (ou similar) para exibir gráficos que mostram:
  1. Vagas criadas por mês.
  2. Candidatos recebidos por mês.

### Critérios de Avaliação de Candidatos

* Pontuação baseada na compatibilidade do candidato com a vaga:
  * Se dentro da faixa salarial, adiciona 1 ponto.
  * Se dentro ou acima da escolaridade exigida, adiciona 1 ponto.

## Tecnologias Utilizadas

* **Django** : Framework web para o backend.
* **Python** : Linguagem de programação principal.
* **HTML/CSS** : Para a interface da página de candidatura.
* **JavaScript (Charts.js)** : Para gráficos e interatividade na página de relatórios.
* **Banco de Dados** : SQLite para desenvolvimento. PostgreSQL ou MySQL para produção.

## Estrutura do Projeto

1. **Modelos de Dados**
   * **Vaga** : Modelo com os campos necessários para definir uma vaga.
   * **Candidatura** : Modelo para registrar os candidatos e suas informações.
2. **Administração**
   * Configuração do Django Admin para gerenciar as vagas e visualizar candidatos.
3. **Landing Page**
   * **Listagem de Vagas** : Página que exibe todas as vagas disponíveis.
   * **Detalhes da Vaga** : Página que mostra informações detalhadas sobre uma vaga específica.
   * **Formulário de Candidatura** : Página onde o candidato pode se inscrever para uma vaga.
4. **Relatórios e Gráficos**
   * Gráficos dinâmicos para análise de desempenho e recrutamento.

## Passos para Implementação

* [X] **Configuração do Ambiente** :
  * Instalar Django e configurar o projeto inicial.
* [ ] **Desenvolvimento do Backend** :
  * Criar modelos de dados para vagas e candidaturas.
  * Configurar o Django Admin para permitir o gerenciamento das vagas.
* [ ] **Desenvolvimento do Frontend** :
  * Criar a interface para listar e detalhar as vagas.
  * Implementar o formulário de candidatura.
* [ ] **Desenvolvimento de Relatórios** :
  * Implementar gráficos com **Charts.js** para exibir relatórios mensais.
* [ ] **Testes** :
  * Testar a criação, edição e exclusão de vagas no Django Admin.
  * Testar a usabilidade da página de candidatura.
* [ ] **Implantação** :
  * Configurar o projeto para ambiente de produção.
  * Realizar deploy em uma plataforma como Railway, Heroku ou servidor próprio.

## Considerações Finais

Este projeto visa facilitar o processo de recrutamento e seleção, oferecendo um sistema completo de gerenciamento de vagas e acompanhamento de candidatos. Alterações e melhorias contínuas podem ser feitas conforme o projeto evolui.
