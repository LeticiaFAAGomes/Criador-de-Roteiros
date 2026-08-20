# 📚 Criador de Roteiros

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge\&logo=flask\&logoColor=white)](https://flask.palletsprojects.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI-4285F4?style=for-the-badge\&logo=google\&logoColor=white)](https://ai.google.dev/)
[![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge\&logo=markdown\&logoColor=white)](https://www.markdownguide.org/)

Aplicação web desenvolvida em **Python com Flask** que utiliza **Inteligência Artificial (Google Gemini)** para transformar conteúdos de materiais didáticos em **resumos e roteiros de aula personalizados**.

O sistema recebe um arquivo PDF, extrai seu conteúdo, utiliza a IA para gerar um resumo e, a partir das informações fornecidas pelo usuário, cria um roteiro de aula organizado por tópicos e blocos de tempo. Ao final, o roteiro é convertido e disponibilizado em formato **PDF**.

---

## 📌 Sobre o Projeto

O **Criador de Roteiros** foi desenvolvido para auxiliar professores e estudantes na preparação de aulas a partir de materiais já existentes.

A aplicação permite informar:

* 📖 Disciplina;
* 👥 Público-alvo;
* ⏱️ Duração da aula;
* 📄 Material didático em formato PDF.

A partir dessas informações, o sistema utiliza o **Google Gemini** para analisar o conteúdo enviado e produzir:

1. Um **sumário executivo** do material;
2. Um **roteiro de aula personalizado**;
3. Uma divisão da aula em **blocos de tempo**;
4. Os **principais tópicos** do conteúdo;
5. Um breve resumo de cada tópico;
6. Um documento final em **PDF**.

---

## 🚀 Funcionalidades

### 📄 Leitura de PDF

O sistema permite o envio de arquivos PDF e utiliza a biblioteca **PyPDF2** para extrair o texto de todas as páginas do documento.

### 🤖 Geração de resumo com IA

O conteúdo extraído do PDF é enviado ao **Google Gemini**, que gera um sumário executivo direcionado ao público-alvo informado.

### 🧑‍🏫 Criação automática do roteiro

A IA analisa o conteúdo e cria um roteiro de aula considerando:

* Disciplina;
* Público-alvo;
* Duração da aula;
* Principais tópicos do material;
* Resumo previamente gerado.

O roteiro é organizado em blocos de tempo para que a duração total da aula seja contemplada.

### 📝 Formatação em Markdown

O roteiro gerado pela IA utiliza Markdown para estruturar:

* Títulos;
* Subtítulos;
* Listas;
* Seções;
* Conteúdos da aula.

### 📑 Geração de PDF

Após a geração do roteiro, o conteúdo em Markdown é convertido para HTML e posteriormente transformado em PDF utilizando **WeasyPrint**.

### 🌐 Aplicação Web

O sistema possui uma aplicação web desenvolvida utilizando **Flask**, responsável por receber os dados do formulário, processar o PDF e retornar o documento final.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia        | Utilização                                   |
| ----------------- | -------------------------------------------- |
| **Python**        | Linguagem principal                          |
| **Flask**         | Desenvolvimento da aplicação web             |
| **Google Gemini** | Geração de resumos e roteiros utilizando IA  |
| **PyPDF2**        | Extração de texto dos arquivos PDF           |
| **Markdown**      | Estruturação do roteiro                      |
| **WeasyPrint**    | Conversão de HTML para PDF                   |
| **python-dotenv** | Gerenciamento da variável de ambiente da API |
| **HTML/CSS**      | Interface da aplicação                       |

---

## 📂 Estrutura do Projeto

```text
Criador-de-Roteiros/
│
├── app.py
├── index.html
├── requirements.txt
├── .env
├── .gitignore
├── static/
│   ├── script.js
│   └── style.css
└── pdf/
```

## ⚙️ Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

* [Python](https://www.python.org/)
* `pip`
* Uma chave de API do **Google Gemini**

No **Windows**, o WeasyPrint pode exigir a instalação do **GTK3 Runtime**.

---

## 🔑 Configuração da API Gemini

O projeto utiliza uma variável de ambiente chamada `GEMINI_KEY`.

Primeiro, gere uma chave de API através do Google AI Studio:

[Google AI Studio — API Key](https://aistudio.google.com/app/apikey?hl=pt-br)

Depois, crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_KEY=sua_chave_aqui
```

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/LeticiaFAAGomes/Criador-de-Roteiros.git
```

Entre na pasta do projeto:

```bash
cd Criador-de-Roteiros
```

Recomenda-se criar um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure a variável `GEMINI_KEY` no arquivo `.env`.

---

## ▶️ Executando o Projeto

Após configurar o ambiente, execute:

```bash
python app.py
```

O Flask iniciará a aplicação localmente.

Acesse pelo navegador:

```text
http://127.0.0.1:5000
```

---

## 🔄 Fluxo da Aplicação

```text
┌──────────────────────┐
│      Usuário         │
└──────────┬───────────┘
           │
           │ Disciplina
           │ Público-alvo
           │ Duração
           │ PDF
           ▼
┌──────────────────────┐
│       Flask          │
│   Recebe formulário  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       PyPDF2         │
│  Extrai texto do PDF │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Google Gemini     │
│                      │
│  Gera resumo +       │
│  roteiro de aula     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      Markdown        │
│      → HTML          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     WeasyPrint       │
│      HTML → PDF      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    PDF Final         │
│  Roteiro de Aula     │
└──────────────────────┘
```

---

## 🧠 Como a Inteligência Artificial é utilizada

O projeto utiliza o modelo **Gemini 1.5 Flash** para processar o conteúdo extraído do documento.

Primeiramente, o sistema solicita à IA um resumo do material considerando o público-alvo:

```text
Resuma esse texto em um sumário executivo,
para um público [público-alvo].
```

Depois, o sistema utiliza o conteúdo e o resumo para solicitar a criação do roteiro:

```text
Você é um assistente especializado em pedagogia e ensino.
Crie um roteiro de aula para a disciplina [disciplina],
com duração de [duração], destinado ao público [público-alvo].
```

O resultado deve apresentar os principais tópicos do conteúdo, seus respectivos resumos e uma divisão da aula em blocos de tempo.

---

## 📑 Exemplo de Entrada

O usuário pode fornecer:

```text
Disciplina: Engenharia de Software
Público-alvo: Estudantes de graduação
Duração da aula: 120 minutos
Material: capítulo de um livro em PDF
```

A aplicação utilizará essas informações juntamente com o conteúdo do PDF para gerar o roteiro.


