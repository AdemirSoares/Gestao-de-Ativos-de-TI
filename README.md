# API de Gestão de Ativos de TI

Projeto desenvolvido para gerenciamento de ativos de Tecnologia da Informação utilizando Python, Flask e PostgreSQL.

O objetivo é aplicar boas práticas de desenvolvimento backend, arquitetura de software, containerização e versionamento, criando uma aplicação web organizada, escalável e preparada para ambientes corporativos.

---

## Objetivo

Desenvolver uma aplicação web capaz de:

- Cadastrar ativos de TI
- Listar ativos cadastrados
- Editar informações dos ativos
- Excluir ativos
- Armazenar os dados em banco PostgreSQL
- Disponibilizar uma API REST para integração com outros sistemas

---

## Funcionalidades

- Dashboard
- Cadastro de ativos
- Listagem de ativos
- Edição de ativos
- Exclusão de ativos
- API REST
- Banco de dados PostgreSQL
- Docker
- Deploy da aplicação

---

## Tecnologias

- Python 3
- Flask
- SQLAlchemy
- PostgreSQL
- HTML5
- CSS3
- Docker
- Git
- GitHub

---

## Estrutura do Projeto

```
gestao-ativos/
│
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── config.py
│
├── .venv/
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

---

## Como executar o projeto

### Clone o repositório

```bash
git clone https://github.com/AdemirSoares/GESTAO-DE-ATIVOS-DE-TI.git
```

### Acesse a pasta

```bash
cd gestao-ativos
```

### Ative o ambiente virtual

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

### Execute a aplicação

```bash
python run.py
```

---

## Autor

**Ademir Soares**

Analista de CyberSecurity | PAM | IAM | Python Developer