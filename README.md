# API de Registro Simples

## 📖 Descrição

Esta API foi desenvolvida com o objetivo de aplicar e demonstrar conhecimentos em **Clean Architecture**, boas práticas de desenvolvimento e desacoplamento de código. É uma API simples de registro de usuários com foco na independência de frameworks e na flexibilidade de substituição de componentes.

### 🚀 Funcionalidades Principais
- Cadastro de usuários com senhas protegidas utilizando **hashing**.
- Validação de dados com **Pydantic**.
- Manipulação de dados com **SQLAlchemy** e banco de dados **MySQL**.
- Arquitetura **Clean Architecture**:
  - Código desacoplado por meio de **interfaces** e **métodos abstratos**.
  - Facilidade para substituir o banco de dados ou modificar regras de negócio sem alterar outras partes do sistema.
- Implementação de **erros personalizados**, reduzindo a dependência do framework.
- Duas rotas de cadastro de usuário:
  - Uma rota com forte independência do framework.
  - Outra rota desacoplada do banco de dados e dos casos de uso.

---

## 🎯 Motivação

Este projeto foi desenvolvido como um exercício prático para consolidar o conhecimento em:
- Desacoplamento de código através de interfaces e abstrações.
- Aplicação de princípios do **Clean Architecture**.
- Criação de soluções flexíveis e escaláveis.
- Uso de boas práticas para tratamento de erros e validação de dados.

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **FastAPI**: Framework para desenvolvimento de APIs (usado apenas como suporte para rotas).
- **Pydantic**: Validação e serialização de dados.
- **SQLAlchemy**: ORM para manipulação do banco de dados.
- **MySQL**: Banco de dados relacional.
- **Clean Architecture**: Para desacoplamento entre camadas.
- **BCrypt**: Para hash de senhas.
