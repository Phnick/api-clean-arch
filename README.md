# API RESTful de Cadastro de Usuário

Esta API simples foi construída para realizar operações básicas de cadastro de usuários, incluindo:
- **Cadastro de novos usuários**.
- **Busca de usuários por nome** através de **query params**.
- **Busca de um único usuário** utilizando **path params**.

A aplicação segue uma arquitetura modular e desacoplada, baseada nos princípios SOLID e Clean Code, o que facilita a manutenção, troca de banco de dados ou alterações nas regras de negócio sem afetar o código existente.

## Arquitetura e Princípios

### Modularidade e SOLID
A arquitetura do código foi projetada para ser modular, separando as diferentes responsabilidades da aplicação:
- **Interfaces** (implementadas como classes abstratas em Python) são usadas para desacoplar as camadas superiores das camadas inferiores, permitindo uma flexibilidade maior para mudanças no banco de dados ou nas regras de negócio sem afetar outras partes do sistema.
- **Princípios SOLID** foram aplicados para garantir que o código siga boas práticas de design, tornando-o fácil de entender e manter.

### Exceções Personalizadas
Foram criadas **exceções personalizadas** através de classes herdadas da classe base `Exception`. Isso permite um controle mais claro e específico de erros dentro da aplicação, proporcionando respostas mais significativas para o usuário.

### Resposta com Pydantic
Foi implementado um modelo de resposta utilizando o **Pydantic** para validar e garantir a consistência dos dados. O Pydantic fornece a validação de dados de forma eficiente e clara, garantindo que os dados enviados e recebidos pela API estejam no formato correto.

### Desacoplamento com o Framework
O código foi **totalmente desacoplado** do framework utilizado (no caso, FastAPI). O objetivo foi manter o código independente e fácil de portar para outros frameworks ou até para um sistema sem framework, caso necessário.

### Domain e Interface de Casos de Uso
O conceito de **Domain** foi aplicado para organizar o código, separando a lógica de negócio em um domínio próprio, enquanto as interfaces de **casos de uso** (Use Cases) foram criadas para interagir com as camadas de serviço e repositório. Isso permite que a lógica de negócios seja reutilizável e desacoplada de implementações específicas.

### Clean Code
Foram aplicados conceitos de **Clean Code** para garantir que o código fosse legível, simples e fácil de manter. A clareza nas responsabilidades de cada classe e função foi priorizada, além de garantir que o código fosse facilmente extensível sem comprometer a qualidade.

### Design Patterns
- **Composer**: Utilizado para compor diferentes objetos e serviços da aplicação de forma flexível.
- **Adapter**: Usado para adaptar o código à integração com o framework escolhido, sem precisar modificar a lógica de negócio.

### Redis para Acelerar a Busca
Para otimizar a performance, foi implementado o **Redis** na busca de usuários por nome. Isso permite que a API faça consultas mais rápidas em buscas repetidas, armazenando temporariamente os resultados e evitando consultas constantes ao banco de dados, acelerando o tempo de resposta.

### Celery para Envio de E-mails
O **Celery** foi utilizado para a fila de envio de e-mails de confirmação de cadastro, permitindo que a API processe o envio de e-mails de forma assíncrona, sem bloquear o fluxo principal da aplicação.

### Banco de Dados MySQL
O banco de dados utilizado para armazenar os dados dos usuários é o **MySQL**. A integração foi feita utilizando o **SQLAlchemy**, que é um ORM (Object-Relational Mapper) para facilitar a comunicação com o banco de dados. O uso do **Alembic** permite realizar migrações de banco de dados de forma eficiente.

---

## Tecnologias Utilizadas
- **FastAPI**: Framework para criação de APIs de alto desempenho.
- **SQLAlchemy**: ORM para interagir com o banco de dados relacional MySQL.
- **Alembic**: Ferramenta de migração de banco de dados.
- **Pydantic**: Validação de dados.
- **Celery**: Processamento assíncrono de tarefas (envio de e-mails).
- **Redis**: Armazenamento de cache para otimizar buscas.
- **MySQL**: Banco de dados relacional utilizado para persistência de dados.
