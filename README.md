Teste de Velocidade de Internet com Interface CMD
Este é um projeto simples que permite realizar um teste de velocidade de internet usando a biblioteca speedtest-cli e exibe os resultados em tempo real em uma interface que simula um terminal CMD. O teste exibe informações de download, upload e latência em tempo real, à medida que o teste é executado.

Funcionalidades
Teste de Velocidade de Internet: Medição das velocidades de download, upload e latência.
Interface em Tempo Real: Através de Server-Sent Events (SSE), a interface se comporta como um terminal, exibindo os resultados do teste em tempo real.
Exibição em Formato CMD: As mensagens são exibidas uma abaixo da outra, com o estilo de terminal.
Requisitos
Antes de rodar o projeto, você precisa ter o seguinte instalado:

Python 3.x: Se ainda não tiver o Python instalado, você pode baixá-lo em: https://www.python.org/downloads/
Flask: Framework web para Python.
speedtest-cli: Biblioteca para medir a velocidade da internet.
Como Instalar as Dependências
Clone este repositório ou baixe os arquivos.

Instale as dependências com o comando:

bash
Copiar código
pip install flask speedtest-cli
Estrutura do Projeto
bash
Copiar código
.
├── app.py                  # Arquivo principal do servidor Flask
├── templates
│   └── index.html           # Arquivo HTML com a interface de terminal
└── README.md                # Este arquivo
Como Executar
Iniciar o Servidor Flask:

Navegue até o diretório onde os arquivos estão localizados e execute o comando abaixo para iniciar o servidor Flask.

bash
Copiar código
python app.py
Acessar a Interface:

Abra seu navegador e acesse http://localhost:5000 para visualizar a interface.

Executar o Teste:

Clique no botão "Iniciar Teste" para iniciar o teste de velocidade da internet. O terminal exibirá em tempo real o progresso do teste, com as velocidades de download, upload e a latência (ping).

Como Funciona
Backend (Flask): O servidor Flask gerencia as requisições e executa o teste de velocidade da internet com a biblioteca speedtest-cli. O backend envia os dados de forma incremental para o frontend através de Server-Sent Events (SSE).

Frontend (HTML/CSS/JavaScript): A interface é feita com HTML e CSS para simular um terminal. O JavaScript se conecta ao servidor usando SSE para receber os dados do teste em tempo real e exibi-los na tela.

Fluxo do Teste
O usuário clica em "Iniciar Teste".
O frontend solicita os dados ao servidor através de SSE.
O backend realiza o teste de velocidade e envia os resultados (download, upload, ping) de forma contínua.
O frontend exibe os resultados no formato de terminal, uma linha abaixo da outra, à medida que o teste avança.
Exemplo de Uso
Ao clicar no botão "Iniciar Teste", o terminal exibirá:

arduino
Copiar código
Iniciando Speedtest...
Obtendo o melhor servidor...
Servidor encontrado! Iniciando teste de download...
Download concluído: 100.50 Mbps
Iniciando teste de upload...
Upload concluído: 50.20 Mbps
Latência: 15.30 ms
Teste concluído com sucesso!
Possíveis Melhorias
Design Responsivo: Melhorar a interface para ser mais adaptável a diferentes tamanhos de tela.
Exibição de Mais Detalhes: Incluir mais informações, como o provedor de internet e o nome do servidor utilizado para o teste.
Suporte para Testes Agendados: Permitir que o usuário agende testes automáticos de velocidade.
Contribuindo
Se você quiser contribuir para este projeto, fique à vontade para fazer um fork, criar uma branch, e enviar um pull request com suas alterações. Todos os tipos de contribuições são bem-vindos!

Fork o repositório
Crie uma branch com suas alterações
Faça um commit com suas mudanças
Envie um pull request para a branch principal
Licença
Este projeto está licenciado sob a MIT License - consulte o arquivo LICENSE para mais detalhes.

