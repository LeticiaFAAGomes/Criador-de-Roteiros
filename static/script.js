async function resumirTexto() {
  // Envia o formulário para o servidor para resumir o texto e gerar um PDF através do app.py.
  // O servidor processa os dados do formulário e gera um PDF com o resumo do texto.
  const formulario = document.getElementById("form");
  const formularioDados = new FormData(formulario);
  await fetch("/resumir", {
    method: "POST",
    body: formularioDados,
  });
}
