# API de Gerenciamento de Eventos Acadêmicos

API RESTful desenvolvida com FastAPI para gerenciar eventos acadêmicos (palestras,
workshops, minicursos, seminários, etc), seus participantes e as inscrições entre eles.

O projeto foi desenvolvido para a disciplina de Desenvolvimento de API RESTful, seguindo
a arquitetura MVC (Model, View/Controller, Service) e usando armazenamento em memória
(sem banco de dados).

## Estrutura do projeto

```
projeto/
│
├── main.py
├── requirements.txt
│
├── controller/
│   ├── evento_controller.py
│   ├── participante_controller.py
│   └── inscricao_controller.py
│
├── model/
│   ├── evento.py
│   ├── participante.py
│   └── inscricao.py
│
└── service/
    ├── evento_service.py
    ├── participante_service.py
    └── inscricao_service.py
```

- **controller**: define as rotas e recebe as requisições HTTP.
- **model**: define os dados da aplicação usando Pydantic (validação incluída).
- **service**: contém as regras de negócio (ex: verificar vagas antes de inscrever).

## Instalação

1. Clone o repositório:

```bash
git clone <link-do-repositorio>
cd projeto
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

```bash
uvicorn main:app --reload
```

A API vai subir em `http://127.0.0.1:8000`.

A documentação interativa (Swagger) fica disponível em:

```
http://127.0.0.1:8000/docs
```

## Principais rotas

### Eventos

| Método | Rota                | Descrição                       |
|--------|---------------------|----------------------------------|
| POST   | /eventos             | Cadastra um novo evento         |
| GET    | /eventos             | Lista todos os eventos          |
| GET    | /eventos/{id}        | Consulta um evento específico   |
| PUT    | /eventos/{id}        | Atualiza um evento existente    |
| DELETE | /eventos/{id}        | Remove um evento                |

### Participantes

| Método | Rota                      | Descrição                           |
|--------|---------------------------|--------------------------------------|
| POST   | /participantes             | Cadastra um novo participante       |
| GET    | /participantes             | Lista todos os participantes        |
| GET    | /participantes/{id}        | Consulta um participante específico |
| PUT    | /participantes/{id}        | Atualiza um participante existente  |
| DELETE | /participantes/{id}        | Remove um participante              |

### Inscrições

| Método | Rota                                             | Descrição                                    |
|--------|---------------------------------------------------|-----------------------------------------------|
| POST   | /eventos/{evento_id}/inscricoes/{participante_id}  | Inscreve um participante em um evento         |
| GET    | /eventos/{evento_id}/inscricoes                    | Lista os participantes inscritos no evento    |

## Exemplos de uso

### Cadastrar um evento

`POST /eventos`

```json
{
  "titulo": "Semana de Tecnologia",
  "descricao": "Palestras e workshops sobre tecnologia",
  "data": "2026-10-15",
  "horario": "19:00",
  "local": "Auditório Central",
  "capacidade": 50,
  "categoria": "Palestra"
}
```

Resposta (201):

```json
{
  "id": 1,
  "titulo": "Semana de Tecnologia",
  "descricao": "Palestras e workshops sobre tecnologia",
  "data": "2026-10-15",
  "horario": "19:00",
  "local": "Auditório Central",
  "capacidade": 50,
  "categoria": "Palestra"
}
```

### Cadastrar um participante

`POST /participantes`

```json
{
  "nome": "Maria Silva",
  "email": "maria.silva@email.com",
  "curso": "Ciência da Computação"
}
```

### Inscrever um participante em um evento

`POST /eventos/1/inscricoes/1`

Resposta (201):

```json
{
  "evento": { "id": 1, "titulo": "Semana de Tecnologia", "...": "..." },
  "participante": { "id": 1, "nome": "Maria Silva", "...": "..." }
}
```

### Exemplos de erro

Evento inexistente (404):

```json
{
  "detail": "Evento não encontrado."
}
```

Participante já inscrito (400):

```json
{
  "detail": "Participante já está inscrito neste evento."
}
```

Evento sem vagas (400):

```json
{
  "detail": "Não existem vagas disponíveis para este evento."
}
```

## Observações

- Os dados são armazenados apenas em memória (listas Python), então são perdidos ao
  reiniciar a aplicação. Isso está de acordo com o enunciado da atividade.
- Toda validação de dados (campos obrigatórios, formato de e-mail, capacidade positiva,
  data válida, etc) é feita automaticamente pelo Pydantic nos models.
