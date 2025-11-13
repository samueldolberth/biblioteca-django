## SGBooks — Sistema de Gerenciamento de Livros

O **SGBooks** é um sistema web desenvolvido em **Django** com o objetivo de **gerenciar livros e avaliações** de forma simples, rápida e organizada.  
Ideal para quem deseja manter um controle eficiente do acervo literário, registrar avaliações pessoais e, futuramente, gerar relatórios de desempenho de leitura.

> 💡 O foco principal é **usabilidade e organização**, mantendo um design limpo e funcional.

---

## Nova Funcionalidade — Avaliação de Livros

A atualização mais recente do **SGBooks** traz uma **tela de avaliação de livros** totalmente integrada ao sistema.  
Agora, os usuários autenticados podem avaliar livros já cadastrados com **nota e comentário**, fortalecendo o controle de qualidade do acervo.

### Funcionalidades atuais:
- Compatível com livros já existentes no sistema  
- Sistema de **nota (1 a 5)** e **comentário** por livro  
- Mostra **apenas as avaliações do usuário logado**  
- Integração com o banco de dados e validação de autenticação  
- Interface feita com **Bootstrap 5**, visual moderna e responsiva  

---

### Próximas implementações:
- **Dashboard de desempenho** dos livros avaliados  
- **Relatórios** com médias de notas e comentários agregados  
- Exibição de **todas as avaliações** de todos os usuários  
- Estatísticas gerais e gráficos interativos  
- Refinamento visual e melhorias na experiência do usuário  

> 💡 A primeira versão visa garantir o funcionamento completo do fluxo de avaliação.  
> 💡 As próximas atualizações trarão melhorias de análise, visualização e relatórios.

---

## 🖼️ Pré-visualização

### Formulário de Avaliação  
Tela para cadastrar uma nova avaliação com seleção de livro, comentário e nota:

![Formulário de Avaliação](media/img/form_avaliacao.png)

---

### Lista de Avaliações  
Avaliações são exibidas em **cards** limpos e organizados:

![Cards de Avaliações](media/img/cards_avaliacao.png)

> 💡 As imagens devem ser salvas na pasta `/static/img/` ou `/media/img/`, e os caminhos atualizados conforme a estrutura do seu projeto Django.

---

## ⚙️ Instalações Necessárias

Antes de rodar o projeto, instale as dependências principais:

```bash
pip install django-allauth jwt pyjwt request
```

> 💡 Utilize um **ambiente virtual** (`venv`) para manter as dependências isoladas.

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/samueldolberth/biblioteca-django.git
   ```
2. Entre no diretório:
   ```bash
   cd biblioteca-django
   ```
3. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```
4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
5. Acesse no navegador:  
   👉 [http://localhost:8000](http://localhost:8000)

---

## Tecnologias Utilizadas

| Tecnologia | Função |
|-------------|--------|
| **Python 3.x** | Linguagem principal |
| **Django** | Framework web principal |
| **Bootstrap 5** | Estilização e responsividade |
| **SQLite** | Banco de dados padrão |
| **JWT / AllAuth** | Autenticação de usuários |

---

## Autor e Informações do Projeto


| **Desenvolvido por** | **Samuel Dolberth** | <br>
| **Curso** | Análise e Desenvolvimento de Sistemas (ADS) | <br>
| **Unidade Curricular** | Programação Web I | <br>
| **Período de Desenvolvimento** | 2025 | <br>
| **Tecnologias Principais** | Django · Python · Bootstrap 5 · SQLite | <br>
