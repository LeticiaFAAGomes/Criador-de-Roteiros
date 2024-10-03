const campoArquivo = document.getElementById("pdf");
const formulario = document.getElementById("form");

async function resumirTexto() {
  // Envia o formulário para o servidor para resumir o texto e gerar um PDF através do app.py.
  // O servidor processa os dados do formulário e gera um PDF com o resumo do texto.
  const formularioDados = new FormData(formulario);
  await fetch("/resumir", {
    method: "POST",
    body: formularioDados,
  });
}

function carregar() {
  // Mostra a tela de carregamento, seguida da tela de sucesso e, após um tempo, reseta o formulário.
  const telaCarregando = document.getElementById("carregando");
  const telaSucesso = document.getElementById("sucesso");
  if (campoArquivo.files.length > 0) {
    telaCarregando.classList.add("aparecer");
    setTimeout(() => {
      telaCarregando.classList.remove("aparecer");
      telaSucesso.classList.add("aparecer");
      setTimeout(() => {
        telaSucesso.classList.remove("aparecer");
        formulario.reset();
      }, 7000);
    }, 8000);
  }
}
