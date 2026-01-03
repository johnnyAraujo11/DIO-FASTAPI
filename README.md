<h1>Constuindo um API com o FastAPI </h1> 
<h2>WorkoutAPI</h2> 
<p>Esta é uma API de competição de crossfit chamada WorkoutAPI (isso mesmo rs, eu acabei unificando duas coisas que gosto: codar e treinar). É uma API pequena, devido a ser um projeto mais hands-on e simplificado nós desenvolveremos uma API de poucas tabelas, mas com o necessário para você aprender como utilizar o FastAPI.</p>

# Async
# Uma API assíncrona é uma API em que as operações são feitas de forma não bloqueante, permitindo que o cliente continue executando outras tarefas enquanto a operação da API ainda está em andamento

# Modelagem de entidade e relacionamento - MER
![Modelo Entidade Relacionamento](mer.jpg)

# Executar o código

## Criar o projeto:
```
    poetry init nome-da-pasta-do-projeto
```
## abra a pasta que foi criada

## Instale as dependências:
```
    poetry add   "fastapi", "uvicorn", "sqlalchemy", "alembic", "asyncpg", "pydantic-settings", "fastapi-pagination"

```
## Se preferir utilizar o pyenv:
```
    pyenv virtualenv 3.11.4 workoutapi
    pyenv activate workoutapi
    pip install -r requirements.txt

```

# Após instalar o dokcer-compose, execute:
```
    docker-compose up -d
```

# Para subir o banco de dados, caso não tenha o docker-compose instalado, faça a instalação e logo em seguida, execute se estiver no windows, caso contrário, procure como executar no linux:
```
    make create-migrations
```

# E por último execute para subir as tabelas criadas para o banco de dados que executa todas as migrações do Alembic, aplicando as alterações de schema pendentes no banco de dados até a versão mais recente e garante que a estrutura do banco fique sincronizada com os models da aplicação:
```
    make run-migrations
```

# Referências

[FastAPI](https://fastapi.tiangolo.com/)

[Pydantic](https://docs.pydantic.dev/latest/)

[SQLAlchemy](https://docs.sqlalchemy.org/en/20/)

[Alembic](https://alembic.sqlalchemy.org/en/latest/)

[Fastapi-pagination](https://uriyyo-fastapi-pagination.netlify.app/)
