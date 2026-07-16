# 🚀 TaskEasy

Sistema de gerenciamento de tarefas desenvolvido com **Django**, permitindo que usuários criem, editem e acompanhem suas tarefas de forma simples e organizada.

O projeto foi desenvolvido com foco em aprendizado de desenvolvimento web utilizando o padrão **MVT (Model-View-Template)** do Django, autenticação de usuários e integração com banco de dados.

---

## 📌 Funcionalidades

✅ Cadastro de usuários  
✅ Login e autenticação de usuários  
✅ Criação de tarefas  
✅ Edição de tarefas  
✅ Alteração de status (Pendente/Concluída)  
✅ Listagem de tarefas do usuário  
✅ Associação de tarefas ao usuário logado  
✅ Interface responsiva utilizando HTML e CSS  

---

## 🛠️ Tecnologias utilizadas

### Backend
- Python
- Django
- SQLite

### Frontend
- HTML5
- CSS3
- Django Templates

### Ferramentas
- Git
- GitHub
- VS Code

---

## 🏗️ Estrutura do projeto

```
taskeasy/
│
├── accounts/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── taskeasy/
│   ├── settings.py
│   └── urls.py
│
├── db.sqlite3
└── manage.py
```

---

## 🗄️ Banco de dados

O projeto utiliza o banco SQLite padrão do Django.

Principais tabelas:

### Usuários

Gerenciada pelo próprio Django:

```
auth_user
```

Armazena:
- Nome
- Email
- Senha criptografada
- Dados de autenticação


### Tarefas

Tabela criada pelo aplicativo `tasks`:

```
tasks_task
```

Campos:

| Campo | Descrição |
|---|---|
| usuario | Usuário responsável pela tarefa |
| titulo | Título da tarefa |
| descricao | Descrição da tarefa |
| concluido | Status da tarefa |
| data_criacao | Data de criação |

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

### 2. Entre na pasta do projeto

```bash
cd taskeasy
```

---

### 3. Instale as dependências

```bash
pip install django
```

---

### 4. Execute as migrações

```bash
python manage.py migrate
```

---

### 5. Crie um usuário administrador (opcional)

```bash
python manage.py createsuperuser
```

---

### 6. Execute o servidor

```bash
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000/
```

---

## 📷 Demonstração

*(Adicione aqui prints do sistema)*

Exemplo:

- Tela de login
- Cadastro de usuário
- Lista de tarefas
- Criação e edição de tarefas

---

## 📚 Conceitos aplicados

Durante o desenvolvimento foram utilizados conceitos importantes do Django:

- Modelagem de banco de dados com Models
- Relacionamento entre tabelas usando ForeignKey
- Views para controle da aplicação
- URLs para roteamento
- Templates Django
- Sistema de autenticação
- Operações CRUD (Create, Read, Update, Delete)

---

## 👨‍💻 Autor

**Luiz Eduardo**

Desenvolvedor em formação, estudando desenvolvimento web, Python e Django.

---

⭐ Se este projeto foi útil ou interessante, deixe uma estrela no repositório!
