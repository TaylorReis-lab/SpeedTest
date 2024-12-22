from flask import Flask, render_template_string, stream_with_context, Response
import speedtest
import time

app = Flask(__name__)

# Página HTML com estilo CMD
HTML_PAGE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste de Velocidade - CMD</title>
    <style>
        body {
            margin: 0;
            background-color: black;
            color: white;
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .terminal {
            width: 80%;
            height: 70%;
            background: black;
            border: 2px solid #00ff00;
            padding: 10px;
            overflow-y: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-size: 16px;
        }

        button {
            margin-top: 10px;
            padding: 10px 20px;
            font-size: 16px;
            color: white;
            background-color: #00ff00;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #00cc00;
        }
    </style>
</head>
<body>
    <div class="terminal" id="terminal">
        Inicie o Speed Test...
    </div>
    <button onclick="iniciarTeste()">Iniciar Teste</button>

    <script>
        function iniciarTeste() {
            const terminal = document.getElementById('terminal');
            terminal.textContent = "Executando teste de velocidade...";

            const eventSource = new EventSource('/run-speedtest');
            eventSource.onmessage = function(event) {
                terminal.textContent += event.data;
                terminal.scrollTop = terminal.scrollHeight;
            };

            eventSource.onerror = function() {
                terminal.textContent += "Conexão encerrada.";
                eventSource.close();
            };
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/run-speedtest')
def run_speedtest():
    def generate():
        yield "data: Inicializando Speedtest...\n\n"
        time.sleep(1)

        try:
            st = speedtest.Speedtest()
            yield "data: Obtendo o melhor servidor...\n\n"
            st.get_best_server()

            yield "data: Servidor encontrado! Iniciando teste de download...\n\n"

            download_speed = st.download() / 1_000_000  # Convertendo para Mbps
            yield f"data: Download concluído: {download_speed:.2f} Mbps\n\n"

            yield "data: Iniciando teste de upload...\n\n"
            upload_speed = st.upload() / 1_000_000  # Convertendo para Mbps
            yield f"data: Upload concluído: {upload_speed:.2f} Mbps\n\n"

            ping = st.results.ping
            yield f"data: Latência: {ping:.2f} ms\n\n"
            yield "data: Teste concluído com sucesso!\n\n"

        except Exception as e:
            yield f"data: Erro ao realizar o teste: {str(e)}\n\n"

    return Response(stream_with_context(generate()), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
