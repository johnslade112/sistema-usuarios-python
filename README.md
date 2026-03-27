# 🚀 Sistema de Gerenciamento de Usuários (Python + SQLite)

Sistema de gerenciamento de usuários desenvolvido em Python com foco em práticas de backend, organização em camadas e evolução de arquitetura.

O projeto permite realizar operações completas de CRUD (Create, Read, Delete) com persistência em banco de dados SQLite.

---

## 🎯 Funcionalidades

* ✔ Cadastro de usuários
* ✔ Listagem de usuários
* ✔ Busca de usuário por ID
* ✔ Remoção de usuário
* ✔ Validação de dados (nome, idade e email)
* ✔ Persistência com SQLite

---

## 🧠 Arquitetura do Projeto

O sistema foi estruturado seguindo separação de responsabilidades (modelo de camadas):

```
main.py        → Interface (entrada/saída)
services.py    → Regras de negócio
utils.py       → Validações
database.py    → Acesso ao banco de dados (SQLite)
```

Essa organização facilita manutenção, escalabilidade e aproxima o projeto de um backend real utilizado em empresas.

---

## 💡 Evolução do Projeto

Este projeto foi desenvolvido em duas etapas para demonstrar evolução técnica:

### 🔹 Versão 1 (Inicial)

* Armazenamento em JSON
* Estrutura simples
* Foco em lógica básica

### 🔹 Versão 2 (Atual)

* Migração completa para SQLite
* Separação em camadas (services, utils, database)
* Melhor organização e legibilidade
* Estrutura mais próxima de sistemas reais

👉 Essa evolução demonstra capacidade de refatoração e melhoria contínua do código.

---

## ⚙️ Tecnologias utilizadas

* Python
* SQLite

---

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/seu-usuario/sistema-usuarios-python.git
```

### 2. Acessar a pasta do projeto

```
cd sistema-usuarios-python
```

### 3. Executar o sistema

```
python main.py
```

---

## 📌 Exemplo de uso

Ao executar o sistema, será exibido um menu interativo:

```
1 - Criar usuário
2 - Listar usuários
3 - Buscar usuário
4 - Remover usuário
5 - Sair
```

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de praticar:

* Estruturação de aplicações backend
* Separação de responsabilidades
* Manipulação de banco de dados
* Validação de dados
* Evolução de arquitetura (JSON → SQLite)

---

## 🚀 Próximos passos

* [ ] Implementar atualização de usuário (UPDATE)
* [ ] Criar API com Flask
* [ ] Integrar com banco de dados mais robusto (PostgreSQL)
* [ ] Adicionar testes automatizados

---

## 👨‍💻 Autor

Desenvolvido por **John Slade Herilus**

🔗 LinkedIn:
https://www.linkedin.com/in/john-slade-herilus-199104250/

---

## ⭐ Considerações finais

Este projeto representa a evolução do aprendizado em backend, saindo de uma estrutura simples para uma arquitetura mais organizada e próxima do mercado.

---
