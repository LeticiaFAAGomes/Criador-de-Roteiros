from flask import Flask, request, send_from_directory, send_file
import google.generativeai as genai
import markdown
import os
import PyPDF2
os.environ['PATH']='C:/Program Files/GTK3-Runtime Win64/bin/'+ os.pathsep + os.environ['PATH']
from weasyprint import HTML

"""
Se você estiver executando o projeto no Windows, pode ser necessário instalar o GTK3-Runtime:
https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases

Gerar chave para GEMINI_KEY: https://aistudio.google.com/app/apikey?hl=pt-br
"""

GEMINI_KEY = "INSIRA_SUA_CHAVE"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

app = Flask(__name__)

@app.route('/')
def home():
    """
    Retorna a página inicial do aplicativo.

    Returns:
        file: Arquivo HTML da página inicial.
    """
    return send_from_directory('.', 'index.html')

@app.route('/resumir', methods=['POST'])
def funcoes_texto():
    """
    Recebe todas as funções do app.py e cria um documento completo com resumo e roteiro de aula.

    Args:
        disciplina (str): Disciplina para qual se destina o roteiro.
        publico_alvo (str): Público-alvo.
        pdf (file): Arquivo PDF com o documento de texto.

    Returns:
         file: Documento completo com resumo e roteiro em formato PDF.
    """
    disciplina = request.form.get('disciplina')
    publico_alvo = request.form.get('publico_alvo')
    uploaded = request.files.get('pdf')

    uploaded.save('pdf/roteiro_temp.pdf')
    texto = extrair_texto_pdf('pdf/roteiro_temp.pdf')
    os.remove('pdf/roteiro_temp.pdf')  
    resumo = resumir(texto, "sumário executivo", publico_alvo=publico_alvo)
    roteiro = criar_roteiro(
        documento=texto,
        disciplina=disciplina,
        publico_alvo=publico_alvo,
        resumo=resumo
        )
    html = convert_markdown_to_html(roteiro)
    filename = uploaded.filename
    pdf_path = convert_html_to_pdf(html, filename)
    return send_file(pdf_path, as_attachment=True)

def extrair_texto_pdf(caminho_pdf):
    """
    Extrai o texto de um arquivo PDF.

    Args:
        caminho_pdf (str): Caminho completo para o arquivo PDF.

    Returns:
        str: Texto extraído do PDF.
    """
    with open(caminho_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            texto_pagina = page.extract_text() or ""
            text += texto_pagina.strip()
    return text

def resumir(documento, nivel_detalhe, publico_alvo, foco=None, paragrafos=1):
    prompt = f"Resuma esse texto em um {nivel_detalhe}, para um público {publico_alvo}. "
    if foco:
        prompt += f"Dê especial atenção a {foco}. "

    prompt += f"Limite o resumo a {paragrafos} parágrafos."
    prompt += " Utilize a língua portuguesa (pt-BR)."

    response = model.generate_content([documento, prompt])
    return response.text

def criar_roteiro(
        documento,
        disciplina,
        publico_alvo,
        resumo=None,
        formato="markdown",
        duracao="60 minutos"
        ):
    """
    Cria um documento completo com resumo e roteiro de aula.

    Args:
        documento: Documento de texto em PDF.
        topicos: Tópicos principais.
        disciplina: disciplina para qual se destina o roteiro.
        resumo: Resumo pré-definido (opcional).
        formato: Formato do documento.
        publico_alvo: Público-alvo.
        duracao: Duração estimada da aula.

    Returns:
        str: Documento completo com resumo e roteiro.
    """

    if not resumo:
        prompt_resumo = f"Resuma este documento em um parágrafo: {documento}"
        resumo = model.generate_content(prompt_resumo).text

    prompt_roteiro = f"""
        Você é um assistente especializado em pedagogia e ensino. Vou fornecer
        o texto de um capítulo de um livro. Sua tarefa é criar um roteiro de
        aula para a disciplina {disciplina} a ser ministrada em {duracao} minutos,
        cujo público alvo é {publico_alvo}.
        O roteiro deve apresentar os principais tópicos do capítulo e seus respectivos resumos.
        O resultado deve ser organizado no formato {formato}.

            Estrutura esperada:

            1. Divida a aula em blocos de tempo que cubram os {duracao} minutos.
            2. Identifique e destaque os tópicos principais.
            3. Inclua breves resumos de cada tópico.
            4. Formate o resultado em {formato}, com títulos, subtítulos e listas,
            quando necessário.

            Aqui está o texto do capítulo: {documento}
    """

    roteiro = model.generate_content(prompt_roteiro).text

    documento_completo = f"## Resumo\n{resumo}\n\n## Roteiro\n{roteiro}"
    return documento_completo

def convert_markdown_to_html(markdown_text):
    """
    Converte texto em Markdown para HTML.

    Args:
        markdown_text (str): Texto em Markdown.

    Returns:
         str: Conteúdo HTML equivalente ao texto Markdown.
    """
    html_content = markdown.markdown(markdown_text)
    return html_content

def convert_html_to_pdf(html_content, filename):
    """
    Converte conteúdo HTML para PDF.

    Args:
        html_content (str): Conteúdo HTML.
        filename (str): Nome do arquivo de saída.

    Returns:
        str: Caminho do arquivo PDF gerado.
    """
    output = os.path.join('pdf', os.path.splitext(filename)[0] + "-roteiro.pdf")
    HTML(string=html_content).write_pdf(output)
    print("PDF gerado com sucesso: " + output)
    return output

if __name__ == '__main__':
    app.run(debug=True)
